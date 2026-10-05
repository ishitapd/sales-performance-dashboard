-- ===============================================================================
-- SALES PERFORMANCE & BUSINESS ANALYTICS DASHBOARD
-- SQL Query Module 01: Revenue Analysis
-- Author: Ishita Prasad (@ishitapd)
-- Database Engine Compatibility: PostgreSQL / SQLite / MySQL / SQL Server
-- ===============================================================================

-- Question 1: What is the total revenue, order count, and AOV by Year?
SELECT 
    EXTRACT(YEAR FROM str_to_date(order_date, '%m/%d/%Y')) AS order_year,
    SUM(sales) AS total_revenue_inr,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(sales) / COUNT(DISTINCT order_id), 2) AS average_order_value_inr
FROM sales_data
GROUP BY order_year
ORDER BY order_year ASC;

-- Question 2: What is the Month-over-Month (MoM) revenue trend and growth rate for 2023?
WITH MonthlySales AS (
    SELECT 
        EXTRACT(MONTH FROM str_to_date(order_date, '%m/%d/%Y')) AS month_num,
        DATE_FORMAT(str_to_date(order_date, '%m/%d/%Y'), '%b') AS month_name,
        SUM(sales) AS monthly_revenue
    FROM sales_data
    WHERE EXTRACT(YEAR FROM str_to_date(order_date, '%m/%d/%Y')) = 2023
    GROUP BY month_num, month_name
)
SELECT 
    month_name,
    monthly_revenue,
    LAG(monthly_revenue, 1) OVER (ORDER BY month_num) AS prev_month_revenue,
    ROUND(
        ((monthly_revenue - LAG(monthly_revenue, 1) OVER (ORDER BY month_num)) / 
        NULLIF(LAG(monthly_revenue, 1) OVER (ORDER BY month_num), 0)) * 100, 2
    ) AS mom_growth_percent
FROM MonthlySales
ORDER BY month_num ASC;
