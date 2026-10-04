# 📊 Sales Performance & Business Analytics Dashboard

<p align="center">
  <img src="assets/preview-banner.svg" alt="Project Banner" width="100%"/>
</p>

<p align="center">
  <strong>An Executive Retail Analytics & Data Science Solution</strong><br/>
  Created by <strong>Ishita Prasad</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/SQL-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQL"/>
  <img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white" alt="Excel"/>
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI"/>
  <img src="https://img.shields.io/badge/DAX-EC4899?style=for-the-badge&logo=analytics&logoColor=white" alt="DAX"/>
</p>

---

## 📸 Executive Dashboard Preview

<p align="center">
  <img src="assets/dashboard_preview.png" alt="Sales Performance & Business Analytics Dashboard Preview" width="100%" style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);"/>
</p>

---

## 📌 Executive Summary

The **Sales Performance & Business Analytics Dashboard** is an end-to-end data analytics and business intelligence application developed by **Ishita Prasad**. The project extracts actionable business intelligence from retail transaction datasets (Superstore & Kaggle sales data) by combining data engineering in **Python & SQL**, modeling with **DAX & Power Query**, and delivering interactive web analytics through a modern **Dark Glassmorphism Dashboard**.

---

## 🎯 Key Project Highlights & Capabilities

- **Data Engineering & Cleaning:** Cleaned and analyzed retail sales data using **Python, Pandas, SQL, Excel**, and **Power Query** to identify revenue, profit, product, and regional trends.
- **DAX-Based KPI Modeling:** Built an interactive Power BI & Web dashboard with **DAX-based KPIs** for revenue, profit, sales growth, and average order value to support executive business analysis.
- **Interactive Scenario Slicers:** Features dynamic real-time filtering across Region, Category, and Order Year that updates KPI calculations and visualizations instantly.

---

## 🛠️ Data Analytics Stack & Core Competencies

| Competency Layer | Tools & Technologies | Key Applications |
| :--- | :--- | :--- |
| **Data Cleaning & Wrangling** | **Python, Pandas, SQL** | Missing value imputation, data normalization, transaction aggregations |
| **ETL & Data Pipeline** | **Power Query (M Language)** | Data type transformation, custom date tables, automated schema cleanup |
| **Business Logic & Modeling** | **Microsoft Excel, Power BI, DAX** | Calculated measures, Time Intelligence, YoY sales growth, profit margin % |
| **Interactive Visualization** | **HTML5, CSS3, Chart.js** | Dark Glassmorphism UI, real-time dynamic filter slicers, responsive charts |

---

## 📈 Executive Key Performance Indicators (KPIs)

| Metric | Formula / Logic | Business Value | Benchmark Value |
| :--- | :--- | :--- | :---: |
| **Total Revenue** | `SUM(Sales[Sales])` | Overall top-line sales volume | **$2.30M** |
| **Net Profit** | `SUM(Sales[Profit])` | Bottom-line earnings across regions | **$286.4K** |
| **Order Volume** | `DISTINCTCOUNT(Sales[Order ID])` | Transaction volume count | **9,994** |
| **Profit Margin %** | `DIVIDE(Total Profit, Total Revenue)` | Profitability efficiency ratio | **12.47%** |
| **Avg Order Value (AOV)** | `DIVIDE(Total Revenue, Order Volume)` | Mean revenue per order | **$230** |

---

## 🎛️ Interactive Web Dashboard Features

- **🌐 Real-Time Interactive Filter Bar:** Filter analytics by **Region** (*West, East, Central, South*), **Product Category** (*Technology, Furniture, Office Supplies*), and **Year** (*2022, 2023*).
- **📈 Monthly Revenue Trend:** Line chart with gradient fills comparing 2022 vs 2023 MoM revenue trajectory.
- **🗂️ Category Distribution:** Doughnut chart breaking down sales contribution across product categories.
- **🗺️ Regional Performance:** Grouped bar charts comparing Sales Revenue vs Net Profit by region.
- **🏆 Top 10 Products:** Horizontal bar chart highlighting top revenue-generating items.

---

## 📂 Repository Structure

```
sales-performance-dashboard/
├── 📄 README.md                ← Executive project overview & documentation
├── 📁 docs/
│   └── index.html              ← Interactive Glassmorphism Web Dashboard
├── 📁 assets/
│   ├── dashboard_preview.png   ← High-resolution dashboard screenshot
│   └── preview-banner.svg     ← Project SVG banner graphic
├── 📁 datasets/
│   └── sample_data.csv         ← Retail sales dataset
├── 📁 excel/
│   └── sales_analysis.md       ← Excel Pivot Tables & Data Analysis guide
├── 📁 powerbi/
│   ├── dashboard_guide.md      ← Power BI setup & DAX reference
│   └── dax_formulas.md         ← Core DAX formulas reference
└── 📁 tableau/
    └── tableau_guide.md        ← Tableau calculations & worksheets guide
```

---

## 🚀 How to Run the Project Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ishitapd/sales-performance-dashboard.git
   ```

2. **Launch the web dashboard:**
   You can serve `docs/index.html` using any local server:
   ```bash
   npx serve docs
   ```
   Or open `docs/index.html` directly in any web browser.

---

## 👤 Author & Attribution

**Ishita Prasad**
- 🌐 GitHub Profile: [@ishitapd](https://github.com/ishitapd)
- 💼 Role: Data & Business Analyst
