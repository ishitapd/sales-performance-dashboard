# 📊 Sales Performance & Business Analytics Dashboard

<p align="center">
  <img src="assets/preview-banner.svg" alt="Project Banner" width="100%"/>
</p>

<p align="center">
  <strong>An End-to-End Indian Retail Analytics, Data Modeling, SQL Querying & BI Solution</strong><br/>
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

The **Sales Performance & Business Analytics Dashboard** is a comprehensive, production-grade data analytics portfolio case study developed by **Ishita Prasad**. This project solves real-world retail business problems by analyzing 50 transaction records (spanning Oct 2020 to Nov 2023) across Indian retail zones (**West, East, South, North**). 

The project delivers an end-to-end data pipeline combining **Python & Pandas** for data cleaning and exploratory data analysis (EDA), **SQL** for business querying and CTE window functions, **Power Query** for data modeling in a Star Schema, **DAX** for dynamic time-intelligence measures, and an interactive **Web & Power BI Executive Dashboard** featuring INR (₹) / USD ($) currency toggling, RFM customer segmentation, and statistical sales forecasting.

---

## 🎯 Business Problem

A growing Indian retail chain operating across major metro cities (*Mumbai, Delhi NCR, Bengaluru, Kolkata*) observed top-line revenue growth but struggled with unpredictable net profit margins across product lines. Executive management lacked visibility into:
1. Which product categories drive real net profit versus unabsorbed overhead costs.
2. The margin erosion caused by unconstrained sales team discounting (>40% discount).
3. Regional performance disparities between high-margin zones (West/East) and struggling regions (South).
4. Customer concentration risk and identification of at-risk VIP accounts.

---

## ❓ Business Questions Addressed

1. What is the total gross revenue, net profit, and overall profit margin % across all operations?
2. How does month-over-month (MoM) and year-over-year (YoY) revenue trend across seasons?
3. Which product category generates the highest net profit margin?
4. How do steep promotional discounts (>20%) impact overall transaction profitability?
5. What are the top revenue-generating products in the enterprise catalog?
6. Which products produce high gross revenue but negative net profit?
7. Which Indian retail zone (West, East, South, North) yields the highest return?
8. Who are the top 10% of customers by spend, and how much revenue concentration do they represent?
9. How can we segment customers using RFM (Recency, Frequency, Monetary) scores to guide marketing?
10. What is the estimated Goods and Services Tax (18% GST) liability generated across transactions?

---

## 📂 Dataset Details

- **File Source:** `datasets/sample_data.csv`
- **Record Count:** 50 validated transaction rows
- **Attribute Count:** 18 fields (`Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer Name`, `Segment`, `Region`, `City`, `State`, `Payment`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`)
- **Date Range:** October 11, 2020 – November 19, 2023
- **Currency:** Indian Rupees (INR ₹) with live USD ($) toggle equivalence

---

## 🎯 Project Objectives

- **Data Wrangling:** Audit, clean, and validate raw retail transaction data in Python.
- **SQL Analysis:** Author 6 modular SQL query files incorporating CTEs, window functions (`RANK()`, `LAG()`, `NTILE()`), and aggregations.
- **Data Modeling:** Structure an analytical **Star Schema** (`FactSales` surrounded by `DimDate`, `DimCustomer`, `DimProduct`, `DimRegion`).
- **DAX Metrics:** Author 15 explicit DAX measures for Time Intelligence and performance metrics.
- **Interactive UI:** Deliver an executive glassmorphism web dashboard featuring dynamic slicers, RFM customer clustering, statistical sales forecasting, PDF report generation, and CSV exporting.

---

## 🛠️ Tech Stack & Skills Demonstrated

| Layer | Tools & Technologies | Demonstrated Competency |
| :--- | :--- | :--- |
| **Programming & EDA** | **Python, Pandas, NumPy** | Type casting, outlier detection, vectorized profit formulas, datetime parsing |
| **SQL Querying** | **ANSI SQL (PostgreSQL/MySQL)** | Window functions (`RANK`, `LAG`), CTEs, `CASE` expressions, aggregations |
| **Spreadsheets** | **Microsoft Excel** | Pivot Tables, `XLOOKUP`, `SUMIFS`, conditional formatting, slicers |
| **ETL & Data Pipeline** | **Power Query (M Language)** | Type transformation, derived columns, query organization |
| **Business Intelligence** | **Power BI, DAX** | Star Schema modeling, Time Intelligence (`SAMEPERIODLASTYEAR`, `DATESYTD`) |
| **Web Dashboard UI** | **HTML5, CSS3, Chart.js** | Glassmorphism UI, scenario slicers, INR/USD currency toggle, PDF/CSV export |
| **Version Control** | **Git & GitHub** | Branch management, commit structuring, live deployment setup |

---

## 🔄 Project Workflow & Data Pipeline

```
Raw Transaction CSV (datasets/sample_data.csv)
                      │
                      ▼
   Python Pandas Data Cleaning & Quality Audit (python/01_data_cleaning.py)
                      │
                      ▼
   Exploratory Data Analysis & Statistics (python/02_eda.py)
                      │
                      ▼
   SQL Business Queries & Window Functions (sql/*.sql)
                      │
                      ▼
   Power Query ETL & Star Schema Data Modeling (powerbi/dashboard_guide.md)
                      │
                      ▼
   DAX Measures & Time Intelligence Catalog (powerbi/dax_measures.md)
                      │
                      ▼
   Interactive Web Analytics Dashboard (docs/index.html)
```

---

## 🧹 Data Cleaning & Quality Assurance (Python)

Script: [`python/01_data_cleaning.py`](file:///d:/DOWNLOADS/sales-performance-dashboard-main/sales-performance-dashboard-main/python/01_data_cleaning.py)

Key data validation checks executed:
- Checked missing values: **0 nulls** found across 50 rows.
- Duplicate check: **0 duplicate transaction lines**.
- Parsed string dates into `pd.to_datetime()`.
- Computed `Shipping_Days = (Ship Date - Order Date)` (Average: **4.4 days**).
- Applied vectorized profit margin formula: `Profit_Margin_% = (Profit / Sales) * 100`.

---

## 📊 SQL Business Analysis

Scripts in [`sql/`](file:///d:/DOWNLOADS/sales-performance-dashboard-main/sales-performance-dashboard-main/sql/) directory:
1. `01_revenue_analysis.sql`: Yearly revenue, order count, AOV, and Month-over-Month (MoM) growth via `LAG()`.
2. `02_profit_analysis.sql`: Profitability by category and discount tier analysis.
3. `03_product_analysis.sql`: Top 10 products ranked via `RANK() OVER()` and high-revenue negative-profit detection.
4. `04_customer_analysis.sql`: Top customer spenders and revenue concentration analysis using `NTILE(10)`.
5. `05_regional_analysis.sql`: Zone performance and top 3 cities per zone using `PARTITION BY`.
6. `06_advanced_analysis.sql`: Complete SQL implementation of RFM Customer Segmentation.

---

## 📐 Data Modeling (Star Schema)

```
                 DimDate (DateKey)
                    │
                    ▼ 1:N
DimCustomer ──► FactSales ◄── DimProduct
(CustomerKey)    (SalesKey)    (ProductKey)
                    ▲
                    │ 1:N
               DimRegion (RegionKey)
```

- **Fact Table:** `FactSales` (50 transaction line items).
- **Dimension Tables:** `DimDate`, `DimCustomer`, `DimProduct`, `DimRegion`.

---

## 📈 Key Empirical Dataset Findings

Calculated directly from `datasets/sample_data.csv`:

- **Total Gross Revenue:** **₹18,21,924.60** (₹18.22 Lakhs | $22,774)
- **Total Net Profit:** **₹3,43,030.70** (₹3.43 Lakhs | $4,288)
- **Total Orders:** **27 distinct checkout orders**
- **Total Unique Customers:** **27 individual customers**
- **Overall Profit Margin %:** **18.83%**
- **Average Order Value (AOV):** **₹67,478.69** ($843)
- **Estimated GST (18%):** **₹3,27,946.43** (₹3.28 Lakhs)

### Category Breakdown:
- **Technology:** **₹11,02,143.84** Revenue | **₹2,77,679.74** Profit | **25.19% Margin**
- **Furniture:** **₹5,34,089.08** Revenue | **₹38,072.28** Profit | **7.13% Margin**
- **Office Supplies:** **₹1,85,691.68** Revenue | **₹27,278.68** Profit | **14.69% Margin**

### Indian Retail Zone Breakdown:
- **West Zone:** **₹7,68,772.80** Revenue | **₹1,50,541.74** Profit (19.58% Margin)
- **East Zone:** **₹6,33,583.20** Revenue | **₹1,67,313.69** Profit (26.41% Margin)
- **South Zone:** **₹2,39,046.52** Revenue | **₹10,560.26** Profit (4.42% Margin)
- **North Zone:** **₹1,80,522.08** Revenue | **₹14,615.01** Profit (8.10% Margin)

---

## 🎯 RFM Customer Segmentation Results

From empirical Python & SQL analysis on dataset customers:

1. 🏆 **Champions (VIPs)** (8 customers | **₹9.82 Lakhs Spend**): Top spenders who order frequently. *Target: Festival VIP Access & Cashback Perks.*
2. 💎 **Loyal Customers** (10 customers | **₹5.24 Lakhs Spend**): Regular buyers. *Target: Category Bundle Deals & No-cost EMI.*
3. ⚠️ **At-Risk Customers** (6 customers | **₹2.48 Lakhs Spend**): High historical spend, long time since last order. *Target: Festive Coupon Re-engagement (>15%).*
4. 💤 **Dormant / Lost** (3 customers | **₹67.8K Spend**): Low spenders. *Target: WhatsApp Win-back Discount Campaigns.*

---

## 💡 Key Business Insights

1. **Finding:** Technology is the primary profit engine, generating **60.5% of total sales** and **80.9% of total net profit** with a 25.19% profit margin.  
   *Implication:* Technology products drive company financial health.  
   *Recommendation:* Allocate top marketing spend and priority warehouse inventory to high-margin Tech products like HP LaserJet Printers and Apple iPhones.

2. **Finding:** Furniture exhibits low margin efficiency (**7.13% profit margin**), with heavy products like conference tables generating high shipping overhead.  
   *Implication:* Freight and discount expenses consume furniture gross margins.  
   *Recommendation:* Renegotiate bulk logistics contracts for heavy furniture items and eliminate sales discounts above 15%.

3. **Finding:** Steep discounts (>40%) result in negative profit margins as low as -180% (e.g., Eureka Forbes Air Purifier sold at 80% discount lost ₹9,908.64).  
   *Implication:* Sales representatives are using unconstrained discounts to close deals at the expense of profitability.  
   *Recommendation:* Implement automated POS/Power BI discount guardrails requiring manager approval for discounts >20%.

---

## 📂 Repository Structure

```
sales-performance-dashboard/
├── 📄 README.md
├── 📁 datasets/
│   └── sample_data.csv
├── 📁 python/
│   ├── 01_data_cleaning.py
│   ├── 02_eda.py
│   └── 03_business_analysis.py
├── 📁 sql/
│   ├── 01_revenue_analysis.sql
│   ├── 02_profit_analysis.sql
│   ├── 03_product_analysis.sql
│   ├── 04_customer_analysis.sql
│   ├── 05_regional_analysis.sql
│   └── 06_advanced_analysis.sql
├── 📁 powerbi/
│   ├── data_model.png
│   ├── dax_measures.md
│   └── dashboard_guide.md
├── 📁 excel/
│   └── sales_analysis.md
├── 📁 docs/
│   ├── index.html
│   ├── data_dictionary.md
│   ├── methodology.md
│   └── interview_questions.md
└── 📁 assets/
    ├── dashboard_preview.png
    ├── preview-banner.svg
    ├── executive_overview.png
    ├── sales_profitability.png
    ├── customer_analysis.png
    ├── product_regional.png
    ├── advanced_analytics.png
    └── data_model.png
```

---

## 🌐 Live Demo & How to Reproduce

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ishitapd/sales-performance-dashboard.git
   ```

2. **Run Python Scripts:**
   ```bash
   cd python
   python 01_data_cleaning.py
   python 02_eda.py
   python 03_business_analysis.py
   ```

3. **Run Web Dashboard Locally:**
   ```bash
   npx serve docs
   ```
   Open `http://localhost:3000` or `http://localhost:59632` in your web browser.

4. **Enable GitHub Pages:**
   - Repository Settings → Pages → Select `main` branch and `/docs` folder → Click Save.
   - Live URL: `https://ishitapd.github.io/sales-performance-dashboard/`

---

## 👤 Author & Contact

**Ishita Prasad**
- 🌐 GitHub: [@ishitapd](https://github.com/ishitapd)
- 💼 Role: Data Analyst & Business Intelligence Specialist
