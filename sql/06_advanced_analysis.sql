-- ===============================================================================
-- SALES PERFORMANCE & BUSINESS ANALYTICS DASHBOARD
-- SQL Query Module 06: Advanced Analytics & RFM Customer Clustering
-- Author: Ishita Prasad (@ishitapd)
-- ===============================================================================

-- Question 1: How do we perform RFM (Recency, Frequency, Monetary) Customer Segmentation in SQL?
WITH MaxDate AS (
    SELECT MAX(str_to_date(order_date, '%m/%d/%Y')) AS max_order_date FROM sales_data
),
RFM_Metrics AS (
    SELECT 
        customer_name,
        DATEDIFF((SELECT max_order_date FROM MaxDate), MAX(str_to_date(order_date, '%m/%d/%Y'))) AS recency_days,
        COUNT(DISTINCT order_id) AS frequency,
        SUM(sales) AS monetary
    FROM sales_data
    GROUP BY customer_name
),
RFM_Scores AS (
    SELECT 
        customer_name,
        recency_days,
        frequency,
        monetary,
        NTILE(3) OVER (ORDER BY recency_days DESC) AS r_score,
        NTILE(3) OVER (ORDER BY frequency ASC) AS f_score,
        NTILE(3) OVER (ORDER BY monetary ASC) AS m_score
    FROM RFM_Metrics
)
SELECT 
    customer_name,
    recency_days,
    frequency,
    monetary AS monetary_inr,
    CONCAT(r_score, f_score, m_score) AS rfm_code,
    CASE 
        WHEN (r_score + f_score + m_score) >= 8 THEN 'Champions (VIPs)'
        WHEN (r_score + f_score + m_score) >= 6 THEN 'Loyal Customers'
        WHEN (r_score + f_score + m_score) >= 4 THEN 'At-Risk Customers'
        ELSE 'Dormant / Lost'
    END AS rfm_segment
FROM RFM_Scores
ORDER BY monetary DESC;
