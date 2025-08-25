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

