# 📐 DAX Formulas Reference — Sales Performance & Business Analytics Dashboard

**Author:** Ishita Prasad  
**Project:** Sales Performance & Business Analytics Dashboard

---

## DAX Measures Collection

### Executive KPIs
```dax
Total Sales = SUM(Sales[Sales])
Total Profit = SUM(Sales[Profit])
Total Orders = DISTINCTCOUNT(Sales[Order ID])
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)
Avg Order Value = DIVIDE([Total Sales], [Total Orders], 0)
```

### Time Intelligence
```dax
YTD Sales = CALCULATE([Total Sales], DATESYTD('DateTable'[Date]))
Sales LY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('DateTable'[Date]))
YoY Growth % = DIVIDE([Total Sales] - [Sales LY], [Sales LY], 0)
```
