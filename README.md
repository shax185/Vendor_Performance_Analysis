# Vendor Performance Analysis End-to-End Data Pipeline

This project provides a comprehensive data pipeline to evaluate and optimize vendor and inventory performance using **Python**, **SQL**, and **PowerBI**. It enables data-driven decision-making by analyzing vendor profitability, inventory turnover, and sales efficiency.

## 🚀 Project Overview

The pipeline is designed to:
- Ingest and process vendor-related data from multiple sources
- Generate performance summaries using SQL
- Perform exploratory data analysis (EDA) including outlier detection
- Analyze profitability and vendor efficiency
- Visualize insights through interactive PowerBI dashboards

## 🔧 Features

- Automated data ingestion with logging
- SQL-based vendor performance summary generation
- Data cleaning and enhancement for analysis
- Outlier detection and EDA
- Profitability and margin analysis
- PowerBI dashboard for strategic insights

## 📊 Pipeline Steps

1. **Data Ingestion Using Python**
   - Connect to PostgreSQL database
   - Extract and merge data from multiple tables
   - Log each step of the process

2. **SQL Summary for Vendor Performance**
   - Use CTEs to aggregate freight, purchase, and sales data
   - Merge summaries to create a comprehensive vendor view

3. **EDA with Outlier Detection & Analysis**
   - Clean and transform data
   - Detect anomalies in sales, purchases, and margins

4. **Profit Analysis**
   - Calculate gross profit, profit margin, stock turnover
   - Evaluate sales-to-purchase ratios

## 🎯 Dashboard Objectives

- Identify underperforming brands for strategic action
- Pinpoint vendors with low stock turnover or losses
- Leverage bulk purchasing insights to reduce unit cost
- Validate profitability differences statistically between vendor tiers
- Reduce risk from vendor over-dependence

## 📈 PowerBI Visualizations

- Top vendors by sales and margin
- Inventory turnover heatmap
- Sales vs. Purchase ratios
- High-margin but low-volume brands

---
<img width="1011" height="654" alt="Screenshot 2025-08-26 091504" src="https://github.com/user-attachments/assets/4f9a8d3b-5ff4-4e54-abd9-fbb9fbb34e77" />

<img width="1855" height="877" alt="Screenshot 2025-08-26 091221" src="https://github.com/user-attachments/assets/ad0b72c7-b159-4bcd-9e4b-db020f6f8d25" />

<img width="1853" height="859" alt="Screenshot 2025-08-26 091144" src="https://github.com/user-attachments/assets/52580299-9b1c-41fe-8c2d-fb5c8459bc91" />
