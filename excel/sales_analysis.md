# 📊 Excel Sales Analysis Guide

## Step 1: Import Data

1. Open Excel → **Data tab** → **Get Data** → **From Text/CSV**
2. Select `datasets/sample_data.csv` (or full Superstore CSV)
3. Click **Transform Data** to open Power Query Editor
4. Set correct data types:
   - `Order Date`, `Ship Date` → Date
   - `Sales`, `Discount`, `Profit` → Decimal Number
   - `Quantity` → Whole Number
5. Click **Close & Load**

---

## Step 2: Create Pivot Tables

### 📌 Pivot Table 1 — Monthly Sales
| Setting | Value |
|---------|-------|
| Rows | Order Date (grouped by Month & Year) |
| Values | Sum of Sales, Sum of Profit |
| Filter | Region, Category |

**Steps:**
1. Click inside your data → Insert → PivotTable
2. Drag `Order Date` to Rows → Right-click → Group → Months + Years
3. Drag `Sales` and `Profit` to Values
4. Insert a **Line Chart** from the pivot table

---

### 📌 Pivot Table 2 — Region-wise Sales
| Setting | Value |
|---------|-------|
| Rows | Region |
| Columns | Category |
| Values | Sum of Sales |

**Visualization:** Clustered Bar Chart

---

### 📌 Pivot Table 3 — Top 10 Products
```
1. Rows: Product Name
2. Values: Sum of Sales
3. Sort: Descending by Sales
4. Right-click Row Labels → Filter → Top 10
```
**Visualization:** Horizontal Bar Chart

---

### 📌 Pivot Table 4 — Category Performance
| Setting | Value |
|---------|-------|
| Rows | Category, Sub-Category |
| Values | Sum of Sales, Sum of Profit, Count of Order ID |

---

## Step 3: Key Excel Formulas

```excel
// Profit Margin %
=Profit/Sales

// Total Sales KPI
=SUM(Table1[Sales])

// YoY Growth
=(ThisYear - LastYear) / LastYear

// VLOOKUP for Category
=VLOOKUP([@[Sub-Category]], CategoryTable, 2, FALSE)

// Dynamic Top N filter
=LARGE(SalesRange, ROW(A1))
```

---

## Step 4: Dashboard Layout

```
+------------------+------------------+------------------+
|  💰 Total Sales  |  📦 Total Orders |  💹 Profit Margin|
|    $2,297,201    |      9,994       |     12.47%       |
+------------------+------------------+------------------+
|                                                        |
|        📈 Monthly Sales Trend (Line Chart)             |
|                                                        |
+------------------------+---------------------------------+
|  🗺️ Region Sales       |  🏆 Top 10 Products            |
|  (Pie/Donut Chart)     |  (Horizontal Bar Chart)        |
+------------------------+---------------------------------+
|                                                        |
|        📦 Category Performance (Clustered Bar)         |
|                                                        |
+--------------------------------------------------------+
```

---

## Step 5: Add Slicers

1. Click PivotTable → PivotTable Analyze → **Insert Slicer**
2. Add slicers for: **Region**, **Category**, **Segment**, **Year**
3. Connect slicers to all pivot tables:
   - Right-click slicer → **Report Connections**
   - Check all pivot tables

---

## ✅ Final Checklist
- [ ] Data imported and cleaned
- [ ] 4 Pivot Tables created
- [ ] Monthly Sales line chart
- [ ] Region-wise bar chart
- [ ] Top 10 products chart
- [ ] Category performance chart
- [ ] KPI cards added
- [ ] Slicers connected to all pivots
- [ ] Dashboard tab formatted and polished
