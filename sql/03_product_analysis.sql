-- ===============================================================================
-- SALES PERFORMANCE & BUSINESS ANALYTICS DASHBOARD
-- SQL Query Module 03: Product Performance & Ranking Analysis
-- Author: Ishita Prasad (@ishitapd)
-- ===============================================================================

-- Question 1: What are the Top 10 products by Total Revenue?
SELECT 
    product_name,
    category,
    sub_category,
    SUM(sales) AS product_revenue_inr,
    SUM(profit) AS product_profit_inr,
    RANK() OVER (ORDER BY SUM(sales) DESC) AS revenue_rank
FROM sales_data
GROUP BY product_name, category, sub_category
ORDER BY revenue_rank ASC
LIMIT 10;

-- Question 2: Which products generate high revenue (> ₹50,000) but negative profit?
SELECT 
    product_name,
    category,
    SUM(sales) AS revenue_inr,
    SUM(profit) AS profit_inr,
    AVG(discount) AS avg_discount_given
FROM sales_data
GROUP BY product_name, category
HAVING SUM(sales) > 50000 AND SUM(profit) < 0
ORDER BY profit_inr ASC;
