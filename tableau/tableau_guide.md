# 🎨 Tableau Guide — Sales Performance & Business Analytics Dashboard

**Author:** Ishita Prasad  
**Project:** Sales Performance & Business Analytics Dashboard

---

## 📌 Tableau Visualizations & Calculations

### 1. Key Calculated Fields
- **Profit Margin %**: `SUM([Profit]) / SUM([Sales])`
- **YoY Growth**: `(SUM([Sales]) - LOOKUP(SUM([Sales]), -1)) / ABS(LOOKUP(SUM([Sales]), -1))`

### 2. Sheet Setup
- **Monthly Revenue Trend**: Month of Order Date vs. Sales & Profit.
- **Category Donut Chart**: Sales breakdown by Technology, Furniture, Office Supplies.
- **Regional Performance**: Grouped Sales & Profit by Region.
- **Top 10 Products**: Filtered by Top 10 Sales revenue.
