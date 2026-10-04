# ⚡ Power BI Dashboard Guide

## Step 1: Connect Data

1. Open Power BI Desktop
2. **Home** → **Get Data** → **Text/CSV**
3. Load `sample_data.csv` (or Superstore CSV)
4. Click **Transform Data** → Power Query Editor opens

---

## Step 2: Power Query Transformations

```m
// Change Order Date to Date type
#"Changed Type" = Table.TransformColumnTypes(Source,{{
    "Order Date", type date
}})

// Add Month-Year column
#"Added Month Year" = Table.AddColumn(#"Changed Type", "Month-Year",
    each Date.ToText([Order Date], "MMM yyyy"), type text)

// Add Profit Margin column
#"Added Profit Margin" = Table.AddColumn(#"Added Month Year",
    "Profit Margin %",
    each if [Sales] = 0 then 0 else [Profit] / [Sales] * 100,
    type number)

// Remove duplicates on Order ID
#"Removed Duplicates" = Table.Distinct(#"Added Profit Margin",
    {"Row ID"})
```

---

## Step 3: DAX Measures

```dax
// ── KPI Measures ──────────────────────────────

Total Sales = SUM('Sales'[Sales])

Total Profit = SUM('Sales'[Profit])

Total Orders = DISTINCTCOUNT('Sales'[Order ID])

Avg Order Value = DIVIDE([Total Sales], [Total Orders], 0)

Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0) * 100

Total Quantity = SUM('Sales'[Quantity])

// ── Time Intelligence ──────────────────────────

Sales LY =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR('DateTable'[Date])
)

YoY Growth % =
DIVIDE([Total Sales] - [Sales LY], [Sales LY], 0) * 100

MTD Sales =
CALCULATE([Total Sales], DATESMTD('DateTable'[Date]))

QTD Sales =
CALCULATE([Total Sales], DATESQTD('DateTable'[Date]))

YTD Sales =
CALCULATE([Total Sales], DATESYTD('DateTable'[Date]))

// ── Ranking ──────────────────────────────────

Product Rank by Sales =
RANKX(
    ALL('Sales'[Product Name]),
    [Total Sales],
    ,
    DESC,
    DENSE
)

Top 10 Products =
IF([Product Rank by Sales] <= 10, [Total Sales], BLANK())

// ── Category Analysis ────────────────────────

Category Sales % =
DIVIDE(
    [Total Sales],
    CALCULATE([Total Sales], ALL('Sales'[Category])),
    0
) * 100

Discount Impact =
SUMX(
    'Sales',
    'Sales'[Sales] * 'Sales'[Discount]
)
```

---

## Step 4: Create Date Table

```dax
DateTable =
CALENDAR(
    MIN('Sales'[Order Date]),
    MAX('Sales'[Order Date])
)

// Add columns to DateTable:
Year = YEAR('DateTable'[Date])
Month = MONTH('DateTable'[Date])
Month Name = FORMAT('DateTable'[Date], "MMMM")
Quarter = "Q" & QUARTER('DateTable'[Date])
Month-Year = FORMAT('DateTable'[Date], "MMM YYYY")
Weekday = FORMAT('DateTable'[Date], "dddd")
```

---

## Step 5: Dashboard Pages

### Page 1 — Executive Summary
- 5 KPI Cards: Total Sales, Profit, Orders, AOV, Margin %
- Line chart: Monthly Sales Trend
- Donut chart: Sales by Category
- Bar chart: Sales by Region
- Slicer: Year, Quarter

### Page 2 — Product Analysis
- Top 10 Products bar chart (using `Top 10 Products` measure)
- Sub-Category scatter plot (Sales vs Profit)
- Matrix: Category → Sub-Category drill-down
- Slicer: Category, Region

### Page 3 — Regional Analysis
- Map visual: Sales by State
- Table: Region → City → Sales, Profit, Orders
- Small multiples: Sales by Region over time
- Slicer: Region, Segment

### Page 4 — Profitability
- Waterfall chart: Profit by Category
- Scatter: Discount vs Profit (correlation)
- Conditional table: Sub-categories with loss (red/green)
- Gauge: Overall Profit Margin vs Target (15%)

---

## ✅ Final Checklist
- [ ] Data loaded and transformed in Power Query
- [ ] Date table created and marked
- [ ] All DAX measures created
- [ ] Relationships set up correctly
- [ ] 4 report pages created
- [ ] Slicers and filters added
- [ ] Published to Power BI Service
