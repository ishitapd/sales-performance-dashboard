-- ===============================================================================
-- SALES PERFORMANCE & BUSINESS ANALYTICS DASHBOARD
-- SQL Query Module 04: Customer Revenue & Concentration Analysis
-- Author: Ishita Prasad (@ishitapd)
-- ===============================================================================

-- Question 1: Who are the top 10 customers by total monetary spend?
SELECT 
    customer_name,
    segment,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(sales) AS total_customer_spend_inr,
    SUM(profit) AS total_customer_profit_inr,
    RANK() OVER (ORDER BY SUM(sales) DESC) AS customer_rank
FROM sales_data
GROUP BY customer_name, segment
ORDER BY customer_rank ASC
LIMIT 10;

-- Question 2: What percentage of total company revenue is contributed by the Top 10% of customers?
WITH CustomerSpend AS (
    SELECT 
        customer_name,
        SUM(sales) AS customer_sales,
        NTILE(10) OVER (ORDER BY SUM(sales) DESC) AS spend_decile
    FROM sales_data
    GROUP BY customer_name
)
SELECT 
    spend_decile,
    COUNT(customer_name) AS customer_count,
    SUM(customer_sales) AS decile_sales_inr,
    ROUND((SUM(customer_sales) / (SELECT SUM(sales) FROM sales_data)) * 100, 2) AS percent_of_total_revenue
FROM CustomerSpend
GROUP BY spend_decile
ORDER BY spend_decile ASC;
