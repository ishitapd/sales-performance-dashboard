# 🔬 Analytical Methodology & Pipeline Architecture

**Author:** Ishita Prasad (@ishitapd)

---

## 📌 1. End-to-End Analytical Pipeline

```
Raw Transaction CSV (datasets/sample_data.csv)
                      │
                      ▼
   Python Pandas Cleaning & Outlier Audit
                      │
                      ▼
       SQL Querying & Business Logic
                      │
                      ▼
 Power Query Transformations & Star Schema Modeling
                      │
                      ▼
     DAX Measures & Time Intelligence Metrics
                      │
                      ▼
 Interactive Executive Dashboard & Insights Delivery
```

---

## 📌 2. RFM Customer Segmentation Methodology

Customers are evaluated across 3 normalized dimensions:
1. **Recency (R):** Days elapsed since the customer's last order.
2. **Frequency (F):** Total count of unique orders placed.
3. **Monetary Value (M):** Cumulative monetary revenue spend (INR ₹).

Each metric is scored using 3-tier quantile binning (1 to 3), creating 4 strategic clusters:
- **Champions (Score >= 8):** Top spending, highly frequent buyers.
- **Loyal Customers (Score >= 6):** Steady repeat purchasers.
- **At-Risk Customers (Score >= 4):** High historical spend, but long recency elapsed.
- **Dormant / Lost (Score < 4):** Low engagement and low monetary contribution.

---

## 📌 3. Time-Series Sales Forecasting Methodology

- **Approach:** 12-Month Moving Average & Seasonal YoY Projection.
- **Evaluation Metric:** Evaluated using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) against historical 2022-2023 sales baseline.
- **Application:** Projects Q4 festive surge revenue bounds to optimize supply chain inventory.
