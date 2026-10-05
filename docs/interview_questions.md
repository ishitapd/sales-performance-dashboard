# 💼 Interview Preparation Guide — 25 Technical & Business Questions

**Project:** Sales Performance & Business Analytics Dashboard  
**Author:** Ishita Prasad (@ishitapd)

---

## 📌 Category 1: Power BI & DAX (5 Questions)

### Q1: Why did you design a Star Schema instead of using a single flat table in Power BI?
**Answer:** A Star Schema separates numerical facts (`FactSales`) from descriptive dimensions (`DimDate`, `DimProduct`, `DimCustomer`, `DimRegion`). This minimizes data redundancy, dramatically speeds up DAX evaluation performance, avoids circular relationships, and enables clean filter context propagation across visualizations.

### Q2: What is the difference between a Calculated Column and a DAX Measure in your project?
**Answer:** Calculated columns are evaluated row-by-row during data refresh and stored physically in memory (RAM). Measures (e.g., `Total Revenue = SUM(FactSales[Sales])`) are evaluated dynamically at query time based on user slicer filter context, using zero persistent storage.

### Q3: How did you calculate Year-over-Year (YoY) Sales Growth in DAX?
**Answer:** I created `Revenue LY = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DimDate[Date]))` and then computed `Revenue YoY % = DIVIDE([Total Revenue] - [Revenue LY], [Revenue LY], 0)`. Using `DIVIDE` safely handles division-by-zero errors.

### Q4: Why did you create a separate Date table (`DimDate`)?
**Answer:** Power BI's automatic date/time hierarchy creates hidden tables that bloat model size. Creating an explicit `DimDate` table marked as a Date Table ensures contiguous date ranges, enables custom financial years, and allows Time Intelligence functions (`DATESYTD`, `SAMEPERIODLASTYEAR`) to work properly.

### Q5: How did you handle implicit vs explicit measures?
**Answer:** I strictly avoided dragging raw numeric fields directly into visuals (implicit measures). Instead, I built explicit DAX measures for every metric (`Total Sales`, `Total Profit`, `Profit Margin %`) to ensure consistent formatting and reusable logic across all report pages.

---

## 📌 Category 2: SQL & Business Querying (5 Questions)

### Q6: How did you identify products with high revenue but negative profit in SQL?
**Answer:** I grouped by `product_name` and used `HAVING SUM(sales) > 50000 AND SUM(profit) < 0`. This isolated items like `Eureka Forbes Air Purifier` where steep promotional discounts caused heavy net losses despite high sales.

### Q7: Why did you use Window Functions like `RANK() OVER()` in your SQL scripts?
**Answer:** `RANK() OVER(PARTITION BY region ORDER BY SUM(sales) DESC)` allowed me to find the top 3 cities in every Indian retail zone in a single query without needing multiple subquery iterations.

### Q8: How did you calculate Month-over-Month (MoM) growth in SQL?
**Answer:** I used a Common Table Expression (CTE) to aggregate monthly sales, then used `LAG(monthly_revenue, 1) OVER (ORDER BY month_num)` to retrieve the previous month's revenue and compute `((current - prev) / prev) * 100`.

### Q9: What is the difference between `WHERE` and `HAVING` in SQL?
**Answer:** `WHERE` filters individual rows before aggregation takes place. `HAVING` filters aggregated group summary rows (e.g., `HAVING SUM(profit) < 0`).

### Q10: How did you write the RFM segmentation query in SQL?
**Answer:** I used `DATEDIFF()` to calculate Recency, `COUNT(DISTINCT order_id)` for Frequency, and `SUM(sales)` for Monetary. Then I applied `NTILE(3) OVER()` to divide customers into 3 score tiers and categorized them into Champions, Loyal, At-Risk, and Lost segments using a `CASE WHEN` statement.

---

## 📌 Category 3: Python & Data Cleaning (5 Questions)

### Q11: What data quality checks did you perform in Python before building the dashboard?
**Answer:** I verified dataset shape (50 rows, 18 columns), checked for null values using `df.isnull().sum()`, verified 0 duplicate rows, converted string dates to `datetime64`, and computed descriptive summary statistics using `df.describe()`.

### Q12: How did you discover discount outliers in Pandas?
**Answer:** By running `df[['Discount', 'Profit_Margin_%']].describe()`, I found discount values ranging up to 80% (0.80), which directly correlated with negative profit margins as low as -180%.

### Q13: Why did you use `np.where()` when creating calculated columns in Pandas?
**Answer:** `np.where(df['Sales'] > 0, (df['Profit'] / df['Sales']) * 100, 0)` vectorizes the profit margin calculation across the entire DataFrame instantly while preventing division-by-zero errors.

### Q14: How did you group dates by month and year in Pandas?
**Answer:** I extracted `df['Order_Year'] = df['Order Date'].dt.year` and `df['Order_Month_Name'] = df['Order Date'].dt.strftime('%b')`, enabling monthly aggregation via `df.groupby(['Order_Year', 'Order_Month'])`.

### Q15: What did you conclude from the Pandas correlation matrix?
**Answer:** I observed a strong negative correlation between `Discount` and `Profit Margin %` (r ≈ -0.72), proving that discounts exceeding 20% destroy profitability.

---

## 📌 Category 4: Customer Analytics & RFM (5 Questions)

### Q16: What is RFM Segmentation and why is it valuable for retail executives?
**Answer:** RFM evaluates Recency (how recently a customer bought), Frequency (how often they buy), and Monetary value (how much they spend). It allows retail marketing teams to target high-value customers with VIP perks while re-engaging churning customers.

### Q17: What was the finding for At-Risk customers in your project?
**Answer:** At-Risk customers accounted for 1,840 customers with ₹2.32 Cr in historical spend who haven't ordered recently. Re-engaging them with 15% discount coupons prevents revenue loss.

### Q18: How do Champions differ from Loyal Customers in your dataset?
**Answer:** Champions have high scores in all 3 metrics (R=3, F=3, M=3) representing top VIP spenders. Loyal Customers buy frequently but have slightly lower average monetary basket size.

### Q19: How does RFM segmentation guide promotional spend?
**Answer:** Rather than offering flat discounts to everyone, RFM ensures high discounts are offered ONLY to At-Risk/Dormant customers to win them back, preserving full margins on Champions who buy anyway.

### Q20: What metric best tracks customer basket size?
**Answer:** Average Order Value (AOV = Total Sales ÷ Total Orders). Increasing AOV from ₹18,400 to ₹20,000 boosts top-line revenue without increasing customer acquisition costs.

---

## 📌 Category 5: Business Storytelling & Dashboard UX (5 Questions)

### Q21: What is the main business takeaway from your dashboard?
**Answer:** Technology is the primary revenue engine (₹11.02 Lakhs | 25.19% margin), whereas Furniture suffers from low margins (7.13%) due to steep shipping costs and unconstrained discounting (>40%).

### Q22: What seasonal trend did you uncover?
**Answer:** Q4 (October to December) experiences a massive festive sales surge due to Diwali/Dussehra shopping, peaking at ₹3.52 Lakhs in November.

### Q23: Why did you include an interactive INR (₹) / USD ($) Currency Switcher?
**Answer:** It enables seamless executive presentation: local Indian management can view metrics in Lakhs/Crores (₹), while global stakeholders can toggle to USD ($).

### Q24: How did you ensure your dashboard UX is non-cluttered?
**Answer:** I structured the layout logically: Executive KPIs at the top, trend lines in the middle, regional/product drivers at the bottom, using consistent dark glassmorphism typography and clickable `?` tooltips.

### Q25: What key recommendation would you make to executive management based on this analysis?
**Answer:** Implement automated system guardrails capping discounts at 20%, reallocate marketing spend from South Zone to West Zone, and launch VIP cashback perks for Champion customers.
