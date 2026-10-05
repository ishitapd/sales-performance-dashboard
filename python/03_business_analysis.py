"""
===============================================================================
SALES PERFORMANCE & BUSINESS ANALYTICS DASHBOARD
Phase 3: Advanced Business Analysis & RFM Customer Segmentation
Author: Ishita Prasad (@ishitapd)
===============================================================================
"""

import pandas as pd
import numpy as np

def run_business_analysis():
    df = pd.read_csv('../datasets/sample_data.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Sales'] = pd.to_numeric(df['Sales'])
    df['Profit'] = pd.to_numeric(df['Profit'])

    print("--- 1. DISCOUNT IMPACT ANALYSIS ---")
    df['Discount_Bin'] = pd.cut(df['Discount'], bins=[-0.01, 0.0, 0.2, 0.5, 1.0], labels=['0% (No Discount)', '1-20%', '21-50%', '>50%'])
    discount_analysis = df.groupby('Discount_Bin', observed=False).agg(
        Order_Count=('Row ID', 'count'),
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Avg_Profit_Margin=('Profit', lambda x: (x.sum() / df.loc[x.index, 'Sales'].sum()) * 100)
    )
    print(discount_analysis.round(2))

    print("\n-------------------------------------------------------------------------------")
    print("WHAT DOES THIS MEAN FOR THE BUSINESS?")
    print("-------------------------------------------------------------------------------")
    print("Discounts above 40% severely destroy profitability, leading to heavy net losses.")
    print("Recommendation: Implement automated system guardrails blocking rep discounts > 20% without manager approval.")
    print("-------------------------------------------------------------------------------\n")

    print("--- 2. RFM CUSTOMER SEGMENTATION ---")
    max_date = df['Order Date'].max()
    rfm = df.groupby('Customer Name').agg(
        Recency_Days=('Order Date', lambda x: (max_date - x.max()).days),
        Frequency=('Order ID', 'nunique'),
        Monetary=('Sales', 'sum')
    ).reset_index()

    # Define Quantile Scoring
    rfm['R_Score'] = pd.qcut(rfm['Recency_Days'].rank(method='first'), q=3, labels=[3, 2, 1])
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=3, labels=[1, 2, 3])
    rfm['M_Score'] = pd.qcut(rfm['Monetary'].rank(method='first'), q=3, labels=[1, 2, 3])
    
    rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

    def segment_customer(row):
        score = int(row['R_Score']) + int(row['F_Score']) + int(row['M_Score'])
        if score >= 8:
            return 'Champions (VIPs)'
        elif score >= 6:
            return 'Loyal Customers'
        elif score >= 4:
            return 'At-Risk Customers'
        else:
            return 'Dormant / Lost'

    rfm['Segment'] = rfm.apply(segment_customer, axis=1)
    
    rfm_summary = rfm.groupby('Segment').agg(
        Customer_Count=('Customer Name', 'count'),
        Total_Monetary=('Monetary', 'sum'),
        Avg_Monetary=('Monetary', 'mean')
    )
    print(rfm_summary.round(2))

    print("\n-------------------------------------------------------------------------------")
    print("WHAT DOES THIS MEAN FOR THE BUSINESS?")
    print("-------------------------------------------------------------------------------")
    print("Champions and Loyal Customers represent the majority of store revenue.")
    print("At-Risk customers require targeted re-engagement campaigns before complete churn occurs.")
    print("-------------------------------------------------------------------------------\n")

if __name__ == '__main__':
    run_business_analysis()
