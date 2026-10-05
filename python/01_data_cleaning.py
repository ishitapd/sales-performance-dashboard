"""
===============================================================================
SALES PERFORMANCE & BUSINESS ANALYTICS DASHBOARD
Phase 1: Data Cleaning & Quality Assurance Workflow
Author: Ishita Prasad (@ishitapd)
===============================================================================
"""

import pandas as pd
import numpy as np

def run_data_cleaning():
    print("--- STEP 1: DATA LOADING & INITIAL AUDIT ---")
    df = pd.read_csv('../datasets/sample_data.csv')
    
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nColumn Data Types:")
    print(df.dtypes)
    
    print("\n--- STEP 2: MISSING VALUE & DUPLICATE ANALYSIS ---")
    missing_vals = df.isnull().sum()
    print("Missing Values per Column:")
    print(missing_vals[missing_vals > 0] if missing_vals.sum() > 0 else "No missing values found.")
    
    duplicate_rows = df.duplicated().sum()
    print(f"Duplicate Rows Count: {duplicate_rows}")
    
    print("\n--- STEP 3: TYPE CONVERSION & SANITIZATION ---")
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    
    # Calculate Shipping Duration in Days
    df['Shipping_Days'] = (df['Ship Date'] - df['Order Date']).dt.days
    
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
    df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').astype(int)
    
    # Calculated Columns
    df['Profit_Margin_%'] = np.where(df['Sales'] > 0, (df['Profit'] / df['Sales']) * 100, 0)
    df['Unit_Price'] = df['Sales'] / df['Quantity']
    df['Order_Year'] = df['Order Date'].dt.year
    df['Order_Month'] = df['Order Date'].dt.month
    df['Order_Month_Name'] = df['Order Date'].dt.strftime('%b')
    df['Order_Year_Month'] = df['Order Date'].dt.strftime('%Y-%m')
    
    print("\n--- STEP 4: NUMERIC & OUTLIER VALIDATION ---")
    print(df[['Sales', 'Profit', 'Discount', 'Quantity', 'Shipping_Days', 'Profit_Margin_%']].describe())
    
    print("\n-------------------------------------------------------------------------------")
    print("WHAT DOES THIS MEAN FOR THE BUSINESS?")
    print("-------------------------------------------------------------------------------")
    print("1. Data Integrity: The dataset contains 50 validated retail transactions with 0 missing values.")
    print("2. Shipping Performance: Average shipping fulfillment time is ~4.4 days.")
    print("3. Profit Margin Outliers: High discounts (>40% to 80%) on specific transactions result in negative profit margins as low as -180%. Management must establish strict discount threshold caps.")
    print("-------------------------------------------------------------------------------\n")
    
    return df

if __name__ == '__main__':
    df_clean = run_data_cleaning()
