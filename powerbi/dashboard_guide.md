# ⚡ Power BI & DAX Guide — Sales Performance & Business Analytics Dashboard

**Author:** Ishita Prasad  
**Project:** Sales Performance & Business Analytics Dashboard

---

## 📌 Power BI Data Pipeline & Modeling

### 1. Data Transformation (Power Query)
```m
let
    Source = Csv.Document(File.Contents("sample_data.csv"),[Delimiter=",", Columns=21, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"Order Date", type date},
        {"Sales", type number},
        {"Profit", type number},
        {"Quantity", Int64.Type}
    }),
    #"Added Profit Margin" = Table.AddColumn(#"Changed Type", "Profit Margin %", each if [Sales] == 0 then 0 else [Profit] / [Sales])
in
    #"Added Profit Margin"
```

### 2. Essential DAX KPI Measures

```dax
// Total Revenue
Total Sales = SUM('Sales'[Sales])

// Net Profit
Total Profit = SUM('Sales'[Profit])

// Total Orders
Total Orders = DISTINCTCOUNT('Sales'[Order ID])

// Profit Margin %
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)

// Average Order Value (AOV)
Avg Order Value = DIVIDE([Total Sales], [Total Orders], 0)

// Year-Over-Year Sales Growth %
Sales YoY Growth % = 
VAR SalesLY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))
RETURN DIVIDE([Total Sales] - SalesLY, SalesLY, 0)
```
