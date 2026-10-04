# 📐 Complete DAX Formula Reference

## Core KPIs

```dax
Total Sales = SUM('Sales'[Sales])
Total Profit = SUM('Sales'[Profit])
Total Orders = DISTINCTCOUNT('Sales'[Order ID])
Total Quantity = SUM('Sales'[Quantity])
Avg Order Value = DIVIDE([Total Sales], [Total Orders], 0)
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0) * 100
```

## Time Intelligence

```dax
Sales LY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('DateTable'[Date]))
YoY % = DIVIDE([Total Sales] - [Sales LY], [Sales LY], 0) * 100
MTD = CALCULATE([Total Sales], DATESMTD('DateTable'[Date]))
QTD = CALCULATE([Total Sales], DATESQTD('DateTable'[Date]))
YTD = CALCULATE([Total Sales], DATESYTD('DateTable'[Date]))
```

## Ranking

```dax
Product Rank = RANKX(ALL('Sales'[Product Name]), [Total Sales], , DESC, DENSE)
Top 10 = IF([Product Rank] <= 10, [Total Sales], BLANK())
Top 5 Customers = RANKX(ALL('Sales'[Customer Name]), [Total Sales], , DESC, DENSE)
```

## Conditional

```dax
Profit Status = IF([Total Profit] >= 0, "Profitable", "Loss")
Discount Band =
    SWITCH(
        TRUE(),
        'Sales'[Discount] = 0, "No Discount",
        'Sales'[Discount] <= 0.2, "Low (≤20%)",
        'Sales'[Discount] <= 0.4, "Medium (21-40%)",
        "High (>40%)"
    )
```
