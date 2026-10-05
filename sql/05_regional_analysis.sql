-- ===============================================================================
-- SALES PERFORMANCE & BUSINESS ANALYTICS DASHBOARD
-- SQL Query Module 05: Regional & Geographical Zone Analysis
-- Author: Ishita Prasad (@ishitapd)
-- ===============================================================================

-- Question 1: What is total sales, profit, and order count across Indian Retail Zones?
SELECT 
    region AS retail_zone,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(sales) AS zone_revenue_inr,
    SUM(profit) AS zone_profit_inr,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_percent
FROM sales_data
GROUP BY region
ORDER BY zone_revenue_inr DESC;

-- Question 2: What are the Top 3 cities by revenue within each Indian Retail Zone?
WITH CityRankings AS (
    SELECT 
        region AS retail_zone,
        city,
        state,
        SUM(sales) AS city_sales_inr,
        RANK() OVER (PARTITION BY region ORDER BY SUM(sales) DESC) AS city_rank
    FROM sales_data
    GROUP BY region, city, state
)
SELECT 
    retail_zone,
    city,
    state,
    city_sales_inr,
    city_rank
FROM CityRankings
WHERE city_rank <= 3
ORDER BY retail_zone, city_rank ASC;
