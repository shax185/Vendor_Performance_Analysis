import psycopg2
import pandas as pd
import logging
import os
from sqlalchemy import create_engine

# Create logs directory if it doesn't exist
# os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/get_vendor_summary.log", 
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s", 
    filemode="a"
)

def ingest_db(df, table_name, engine):
    """Ingest the dataframe into a PostgreSQL table."""
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Data ingested into table '{table_name}' successfully.")
    except Exception as e:
        logging.error(f"Failed to ingest data into '{table_name}': {e}")

def create_vendor_summary(conn):
    """Generate vendor summary by merging multiple tables."""
    try:
        query = """
        WITH FreightSummary AS (
            SELECT 
                VendorNumber, 
                SUM(Freight) AS FreightCost 
            FROM vendor_invoice 
            GROUP BY VendorNumber
        ), 
        
        PurchaseSummary AS (
            SELECT 
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                p.PurchasePrice,
                pp.Price AS ActualPrice,
                pp.Volume,
                SUM(p.Quantity) AS TotalPurchaseQuantity,
                SUM(p.Dollars) AS TotalPurchaseDollars
            FROM purchases p
            JOIN purchase_prices pp
                ON p.Brand = pp.Brand
            WHERE p.PurchasePrice > 0
            GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
        ), 
        
        SalesSummary AS (
            SELECT 
                VendorNo,
                Brand,
                SUM(SalesQuantity) AS TotalSalesQuantity,
                SUM(SalesDollars) AS TotalSalesDollars,
                SUM(SalesPrice) AS TotalSalesPrice,
                SUM(ExciseTax) AS TotalExciseTax
            FROM sales
            GROUP BY VendorNo, Brand
        ) 
        
        SELECT 
            ps.VendorNumber,
            ps.VendorName,
            ps.Brand,
            ps.Description,
            ps.PurchasePrice,
            ps.ActualPrice,
            ps.Volume,
            ps.TotalPurchaseQuantity,
            ps.TotalPurchaseDollars,
            ss.TotalSalesQuantity,
            ss.TotalSalesDollars,
            ss.TotalSalesPrice,
            ss.TotalExciseTax,
            fs.FreightCost
        FROM PurchaseSummary ps
        LEFT JOIN SalesSummary ss 
            ON ps.VendorNumber = ss.VendorNo 
            AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary fs 
            ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC
        """
        df = pd.read_sql_query(query, conn)
        logging.info("Vendor summary created successfully.")
        return df
    except Exception as e:
        logging.error(f"Error creating vendor summary: {e}")
        raise

def clean_data(df):
    """Clean and enhance the vendor summary data."""
    try:
        df['Volume'] = df['Volume'].astype(float)
        df.fillna(0, inplace=True)
        df['VendorName'] = df['VendorName'].str.strip()
        df['Description'] = df['Description'].str.strip()

        df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
        df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars']) * 100
        df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
        df['SalesToPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']

        logging.info("Data cleaned and enhanced successfully.")
        return df
    except Exception as e:
        logging.error(f"Error cleaning data: {e}")
        raise

if __name__ == '__main__':
    try:
        # PostgreSQL connection setup
        conn = psycopg2.connect(
            dbname="Inventory",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/Inventory")

        logging.info("Starting vendor summary process...")

        summary_df = create_vendor_summary(conn)
        logging.debug(f"Summary preview:\n{summary_df.head()}")

        clean_df = clean_data(summary_df)
        logging.debug(f"Cleaned data preview:\n{clean_df.head()}")

        ingest_db(clean_df, 'vendor_sales_summary', engine)

        logging.info("Vendor summary process completed successfully.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            logging.info("Database connection closed.")