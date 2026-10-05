# ⚡ Power BI Implementation & Dashboard Guide

**Project:** Sales Performance & Business Analytics Dashboard  
**Author:** Ishita Prasad (@ishitapd)

---

## 📌 1. Power Query ETL Pipeline

```m
let
    Source = Csv.Document(File.Contents("sample_data.csv"),[Delimiter=",", Columns=18, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"Order Date", type date},
        {"Ship Date", type date},
        {"Sales", type number},
        {"Profit", type number},
        {"Quantity", Int64.Type},
        {"Discount", type number}
    }),
    #"Added Profit Margin" = Table.AddColumn(#"Changed Type", "Profit Margin %", each if [Sales] == 0 then 0 else [Profit] / [Sales])
in
    #"Added Profit Margin"
```

---

## 📌 2. Star Schema Data Model Architecture

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

- **Fact Table:** `FactSales` (Grain: 1 row per transaction line item).
- **Dimension Tables:**
  - `DimDate` (Calendar Date, Year, Month, Month-Year, Quarter, Weekday).
  - `DimCustomer` (Customer ID, Customer Name, Segment).
  - `DimProduct` (Product ID, Product Name, Category, Sub-Category).
  - `DimRegion` (Region ID, Zone Name, City, State).

---

## 📌 3. Power BI Report Pages Layout

- **Page 1 — Executive Overview:** Top 5 KPI Cards, Revenue YoY Trend, Category Donut, Regional Bar Chart.
- **Page 2 — Sales & Profitability Analysis:** Discount vs Profit Scatter Plot, Loss-making Products Table.
- **Page 3 — Customer Analytics & RFM Segmentation:** Customer RFM Score Cards, Spend Deciles.
- **Page 4 — Regional & Product Analysis:** City/State Matrix, Top 10 Revenue Products.
- **Page 5 — Statistical Sales Forecasting:** 12-Month Moving Average Trend & Historical YoY Comparisons.

---

## 📌 4. How to Create `Sales_Performance.pbix` in Power BI Desktop

1. Open **Power BI Desktop** → Click **Get Data** → Select **Text/CSV**.
2. Select `datasets/sample_data.csv` and click **Transform Data**.
3. Apply Power Query M transformations above and click **Close & Apply**.
4. In Model View, establish 1:N relationships between `DimDate[Date]` and `FactSales[Order Date]`.
5. Create DAX measures from `powerbi/dax_measures.md`.
6. Save file as `Sales_Performance.pbix`.
