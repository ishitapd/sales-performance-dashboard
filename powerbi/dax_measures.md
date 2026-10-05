# 📐 DAX Measures Reference Catalog

**Project:** Sales Performance & Business Analytics Dashboard  
**Author:** Ishita Prasad (@ishitapd)

---

## 📌 Executive Core KPIs

### 1. Total Revenue
- **DAX Formula:**
  ```dax
  Total Revenue = SUM(FactSales[Sales])
  ```
- **What it Calculates:** Sum of gross revenue across all transactions.
- **Why it is Useful:** Primary top-line financial indicator.
- **Used In:** Executive KPI Card, Revenue Trend Line Chart, Regional Bar Chart.

### 2. Total Profit
- **DAX Formula:**
  ```dax
  Total Profit = SUM(FactSales[Profit])
  ```
- **What it Calculates:** Net earnings after subtracting product COGS and discounts.
- **Why it is Useful:** Evaluates true operational profitability.
- **Used In:** Executive KPI Card, Profit by Category Donut Chart.

### 3. Profit Margin %
- **DAX Formula:**
  ```dax
  Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)
  ```
- **What it Calculates:** Percentage of sales retained as net profit.
- **Why it is Useful:** Prevents volume bias by measuring margin efficiency.
- **Used In:** Executive KPI Card, Category Profitability Table.

### 4. Order Count
- **DAX Formula:**
  ```dax
  Order Count = DISTINCTCOUNT(FactSales[Order ID])
  ```
- **What it Calculates:** Unique checkout receipts.
- **Why it is Useful:** Tracks transaction volume growth.
- **Used In:** Executive KPI Card.

### 5. Average Order Value (AOV)
- **DAX Formula:**
  ```dax
  Average Order Value = DIVIDE([Total Revenue], [Order Count], 0)
  ```
- **What it Calculates:** Average spending per transaction.
- **Why it is Useful:** Key metric for basket size optimization.
- **Used In:** Executive KPI Card.

---

## 📌 Time Intelligence Measures

### 6. Revenue LY (Same Period Last Year)
- **DAX Formula:**
  ```dax
  Revenue LY = 
  CALCULATE(
      [Total Revenue],
      SAMEPERIODLASTYEAR(DimDate[Date])
  )
  ```
- **What it Calculates:** Revenue generated in the exact corresponding period of the previous calendar year.
- **Why it is Useful:** Benchmark for Year-over-Year comparison.

### 7. Revenue YoY %
- **DAX Formula:**
  ```dax
  Revenue YoY % = 
  VAR CurrentSales = [Total Revenue]
  VAR PriorSales = [Revenue LY]
  RETURN DIVIDE(CurrentSales - PriorSales, PriorSales, 0)
  ```
- **What it Calculates:** Percentage growth in revenue compared to last year.
- **Why it is Useful:** Identifies acceleration or deceleration in sales.

### 8. YTD Revenue
- **DAX Formula:**
  ```dax
  YTD Revenue = CALCULATE([Total Revenue], DATESYTD(DimDate[Date]))
  ```
- **What it Calculates:** Cumulative revenue from Jan 1 of current year to selected date.

### 9. Month-over-Month (MoM) Growth %
- **DAX Formula:**
  ```dax
  MoM Growth % = 
  VAR CurrentMonthSales = [Total Revenue]
  VAR PrevMonthSales = CALCULATE([Total Revenue], DATEADD(DimDate[Date], -1, MONTH))
  RETURN DIVIDE(CurrentMonthSales - PrevMonthSales, PrevMonthSales, 0)
  ```
- **What it Calculates:** Sequential growth rate month over month.
