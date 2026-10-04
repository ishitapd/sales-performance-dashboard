# 🎨 Tableau Dashboard Guide

## Step 1: Connect Data

1. Open Tableau Desktop
2. **Connect** → **Text File** → Select `sample_data.csv`
3. Tableau auto-detects data types — verify:
   - `Order Date` → Date
   - `Sales`, `Profit` → Measure (green)
   - `Region`, `Category` → Dimension (blue)

---

## Step 2: Create Calculated Fields

### Profit Margin %
```
Name: Profit Margin %
Formula: SUM([Profit]) / SUM([Sales])
Format: Percentage, 2 decimal places
```

### Sales Category
```
Name: Sales Tier
Formula:
IF SUM([Sales]) > 1000 THEN "High"
ELSEIF SUM([Sales]) > 500 THEN "Medium"
ELSE "Low"
END
```

### YoY Growth
```
Name: YoY Sales Growth
Formula:
(SUM([Sales]) - LOOKUP(SUM([Sales]), -1)) / ABS(LOOKUP(SUM([Sales]), -1))
```

### LOD — Average Sales per Customer
```
Name: Avg Sales per Customer
Formula:
{ FIXED [Customer Name] : SUM([Sales]) }
```

---

## Step 3: Build Worksheets

### Sheet 1 — Monthly Sales Trend
```
Columns: MONTH(Order Date) [continuous]
Rows: SUM(Sales)
Mark Type: Line
Color: SUM(Profit)
Detail: YEAR(Order Date)
Add Reference Line: Average
```

### Sheet 2 — Region Map
```
Double-click: State
Auto-creates geographic map
Color: SUM(Sales)
Size: SUM(Profit)
Tooltip: Orders, Sales, Profit
Map Layer: Streets
```

### Sheet 3 — Category Performance
```
Columns: SUM(Sales), SUM(Profit)
Rows: Category, Sub-Category
Mark Type: Bar
Color: Profit (red-green diverging)
Sort: Descending by Sales
```

### Sheet 4 — Top 10 Products
```
1. Rows: Product Name
2. Columns: SUM(Sales)
3. Sort: Descending
4. Filter: Product Name → Top → By Field → Top 10 → By SUM(Sales)
5. Mark: Bar, Color by Category
```

### Sheet 5 — KPI Summary
```
Create 4 text marks:
- Total Sales: SUM([Sales]) formatted as currency
- Total Profit: SUM([Profit])
- Profit Margin: [Profit Margin %]
- Total Orders: COUNTD([Order ID])
```

### Sheet 6 — Scatter: Discount vs Profit
```
Columns: AVG(Discount)
Rows: SUM(Profit)
Detail: Sub-Category
Color: Category
Trend Line: Linear (show R²)
```

---

## Step 4: Build Dashboard

```
Dashboard Size: Fixed 1400 x 900px

+------------------------------------------+
|        KPI Summary (Sheet 5)             |
+----------+----------+--------------------+
|  Monthly | Region   |  Category Bars     |
|  Trend   | Map      |  (Sheet 3)         |
| (Sheet 1)| (Sheet 2)|                    |
+----------+----------+--------------------+
|   Top 10 Products (Sheet 4)              |
+------------------------------------------+
```

**Add Filters:**
1. Drag **Region** to Filters shelf → Show Filter
2. Drag **Category** to Filters shelf → Show Filter
3. Drag **Order Date** → Range of Dates
4. Right-click each filter → **Apply to Worksheets → All**

---

## Step 5: Dashboard Actions

1. Dashboard menu → **Actions** → **Add Action**
2. **Filter Action:** Click Region Map → Filters all other sheets
3. **Highlight Action:** Hover on Category Bar → Highlights same category across all sheets
4. **URL Action:** Click Product → Opens product search URL

---

## Step 6: Publish to Tableau Public

1. **Server** → **Tableau Public** → **Save to Tableau Public**
2. Sign in with free Tableau Public account
3. Name: `Sales Performance Dashboard`
4. Copy the public URL and add it to README

---

## ✅ Final Checklist
- [ ] Data connected and field types verified
- [ ] Calculated fields created
- [ ] 6 worksheets built
- [ ] Dashboard assembled (1400×900)
- [ ] Filters connected to all sheets
- [ ] Dashboard actions configured
- [ ] Published to Tableau Public
