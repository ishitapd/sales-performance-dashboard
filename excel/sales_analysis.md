# 📗 Excel Analysis Guide — Sales Performance & Business Analytics Dashboard

**Author:** Ishita Prasad  
**Project:** Sales Performance & Business Analytics Dashboard

---

## 📌 Executive Data Analysis Workflow

### 1. Data Cleaning & Power Query Setup
- Import `datasets/sample_data.csv` via Excel Power Query (`Data` → `Get Data` → `From Text/CSV`).
- Transform Data Types:
  - `Order Date`, `Ship Date` → `Date`
  - `Sales`, `Profit`, `Discount` → `Currency / Decimal`
  - `Quantity` → `Whole Number`
- Remove duplicates and null values.

### 2. Core Pivot Table Specifications

| Pivot Table | Rows | Values | Primary Visualization |
|:---|:---|:---|:---|
| **Monthly Revenue Trend** | `Order Date` (Month & Year) | `Sum of Sales`, `Sum of Profit` | Area / Line Chart with YoY comparisons |
| **Regional Sales Breakdown** | `Region` | `Sum of Sales`, `Sum of Profit` | Grouped Bar Chart |
| **Top 10 Revenue Products** | `Product Name` (Top 10 Filter) | `Sum of Sales` | Horizontal Bar Chart |
| **Category Distribution** | `Category`, `Sub-Category` | `Sum of Sales`, `Profit Margin %` | Donut Chart |

### 3. Key Excel Measures & Formulas

```excel
// Profit Margin Percentage
=SUM([Profit]) / SUM([Sales])

// Average Order Value (AOV)
=AVERAGE([Sales])

// Year-over-Year (YoY) Sales Growth
=(SUM(Sales_2023) - SUM(Sales_2022)) / SUM(Sales_2022)
```
