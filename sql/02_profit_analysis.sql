-- ===============================================================================
-- SALES PERFORMANCE & BUSINESS ANALYTICS DASHBOARD
-- SQL Query Module 02: Profitability & Discount Impact Analysis
-- Author: Ishita Prasad (@ishitapd)
-- ===============================================================================

-- Question 1: What is the total profit and profit margin % by Product Category?
SELECT 
    category,
    SUM(sales) AS category_revenue,
    SUM(profit) AS category_profit,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_percent
FROM sales_data
GROUP BY category
ORDER BY category_profit DESC;

-- Question 2: How does discount percentage impact overall profitability and profit margins?
SELECT 
    CASE 
        WHEN discount = 0 THEN '0% (No Discount)'
        WHEN discount > 0 AND discount <= 0.20 THEN '1% - 20% Discount'
        WHEN discount > 0.20 AND discount <= 0.50 THEN '21% - 50% Discount'
        ELSE '> 50% Discount'
    END AS discount_tier,
    COUNT(order_id) AS total_line_items,
    SUM(sales) AS total_sales_inr,
    SUM(profit) AS total_profit_inr,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_percent
FROM sales_data
GROUP BY discount_tier
ORDER BY total_profit_inr DESC;
