"""
===============================================================================
SALES PERFORMANCE & BUSINESS ANALYTICS DASHBOARD
Phase 2: Exploratory Data Analysis (EDA) Workflow
Author: Ishita Prasad (@ishitapd)
===============================================================================
"""

import pandas as pd
import numpy as np

def run_eda():
    df = pd.read_csv('../datasets/sample_data.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Sales'] = pd.to_numeric(df['Sales'])
    df['Profit'] = pd.to_numeric(df['Profit'])
    df['Year'] = df['Order Date'].dt.year

    print("--- 1. CATEGORY PERFORMANCE EDA ---")
    cat_summary = df.groupby('Category').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Total_Quantity=('Quantity', 'sum'),
        Order_Count=('Order ID', 'nunique')
    )
    cat_summary['Profit_Margin_%'] = (cat_summary['Total_Profit'] / cat_summary['Total_Sales']) * 100
    print(cat_summary.round(2))
    
    print("\n-------------------------------------------------------------------------------")
    print("WHAT DOES THIS MEAN FOR THE BUSINESS?")
    print("-------------------------------------------------------------------------------")
    print("Technology dominates sales revenue (₹11,02,143.84) with a strong 25.19% profit margin.")
    print("Furniture generates substantial sales (₹5,34,089.08) but delivers a weak 7.13% profit margin due to high logistics costs and steep discounts.")
    print("-------------------------------------------------------------------------------\n")

    print("--- 2. INDIAN RETAIL ZONE EDA ---")
    reg_summary = df.groupby('Region').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Order_Count=('Order ID', 'nunique')
    )
    reg_summary['Profit_Margin_%'] = (reg_summary['Total_Profit'] / reg_summary['Total_Sales']) * 100
    print(reg_summary.round(2))

    print("\n-------------------------------------------------------------------------------")
    print("WHAT DOES THIS MEAN FOR THE BUSINESS?")
    print("-------------------------------------------------------------------------------")
    print("West Zone is the revenue leader (₹7,68,772.80 | 19.58% margin) followed by East Zone (₹6,33,583.20 | 26.41% margin).")
    print("South Zone exhibits the lowest performance (₹2,39,046.52 | 4.42% margin), identifying a key market for promotional restructuring.")
    print("-------------------------------------------------------------------------------\n")

    print("--- 3. YEAR-OVER-YEAR (YoY) TREND EDA ---")
    yoy_summary = df.groupby('Year').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Order_Count=('Order ID', 'nunique')
    )
    yoy_summary['Profit_Margin_%'] = (yoy_summary['Total_Profit'] / yoy_summary['Total_Sales']) * 100
    print(yoy_summary.round(2))

if __name__ == '__main__':
    run_eda()
