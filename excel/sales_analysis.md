# 📗 Excel Data Analysis Workflow

**Project:** Sales Performance & Business Analytics Dashboard  
**Author:** Ishita Prasad (@ishitapd)

---

## 📌 Excel Workbook Structure & Pivot Tables

### 1. Data Cleaning in Excel
- Import `datasets/sample_data.csv` into Table `SalesTable`.
- Format `Order Date` and `Ship Date` as `YYYY-MM-DD`.
- Insert column `Shipping Days`: `=[@[Ship Date]] - [@[Order Date]]`.
- Insert column `Profit Margin %`: `=[@[Profit]] / [@[Sales]]`.

### 2. Pivot Tables Built
1. **Pivot 1: Monthly Sales & Profit Trend**: Rows = Order Date (Grouped by Year & Month), Values = Sum of Sales, Sum of Profit.
2. **Pivot 2: Region Performance**: Rows = Region, Values = Sum of Sales, Sum of Profit, Profit Margin %.
3. **Pivot 3: Top 10 Products**: Rows = Product Name (Filtered to Top 10 by Sales), Values = Sum of Sales.
4. **Pivot 4: Category Breakdown**: Rows = Category, Sub-Category, Values = Sum of Sales, Count of Orders.

### 3. Formulas Demonstrated
```excel
=SUM(SalesTable[Sales])
=AVERAGE(SalesTable[Sales])
=XLOOKUP([@[Sub-Category]], CategoryLookupTable[Sub-Category], CategoryLookupTable[Category])
```
