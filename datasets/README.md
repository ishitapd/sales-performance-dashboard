# 📂 Datasets

## Dataset 1: Indian Retail Sample (`sample_data.csv`)

Local file used by this repo. Values are **INR**. Geography is Indian zones/cities. Checkout mix includes UPI, cards, COD and EMI.

### Columns
| Column | Type | Description |
|--------|------|-------------|
| Row ID | Integer | Unique row identifier |
| Order ID | String | Unique order identifier (`IN-YYYY-…`) |
| Order Date | Date | Date of order placement |
| Ship Date | Date | Date of shipment |
| Ship Mode | String | Shipping category |
| Customer Name | String | Customer full name |
| Segment | String | Consumer / Corporate / Home Office |
| Region | String | East / West / North / South |
| City | String | Indian city |
| State | String | Indian state / UT |
| Payment | String | UPI / Cards / COD / EMI |
| Category | String | Furniture / Office Supplies / Technology |
| Sub-Category | String | Product sub-category |
| Product Name | String | India-market product name |
| Sales | Float | Revenue in INR (₹) |
| Quantity | Integer | Units ordered |
| Discount | Float | Discount applied (0–1) |
| Profit | Float | Net profit in INR (₹) |

The Kaggle Superstore file below is a larger raw source if you want to rebuild the model. Convert USD → INR and map US regions to Indian zones before using it in this dashboard.

---

## Optional: Kaggle Superstore (raw USD source)

- **Download:** https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
- **File:** `Sample - Superstore.csv`
- **Size:** ~2.5 MB | 9,994 rows

### Columns
| Column | Type | Description |
|--------|------|-------------|
| Row ID | Integer | Unique row identifier |
| Order ID | String | Unique order identifier |
| Order Date | Date | Date of order placement |
| Ship Date | Date | Date of shipment |
| Ship Mode | String | Shipping category |
| Customer ID | String | Unique customer ID |
| Customer Name | String | Customer full name |
| Segment | String | Consumer / Corporate / Home Office |
| Country | String | Country (United States) |
| City | String | City of delivery |
| State | String | State of delivery |
| Postal Code | Integer | ZIP code |
| Region | String | East / West / Central / South |
| Product ID | String | Unique product identifier |
| Category | String | Furniture / Office Supplies / Technology |
| Sub-Category | String | 17 sub-categories |
| Product Name | String | Full product name |
| Sales | Float | Revenue in USD |
| Quantity | Integer | Units ordered |
| Discount | Float | Discount applied (0–1) |
| Profit | Float | Net profit in USD |

---

## Dataset 2: Kaggle Sales Data

- **Download:** https://www.kaggle.com/datasets/kyanyoga/sample-sales-data
- **File:** `sales_data_sample.csv`
- **Size:** ~0.5 MB | 2,823 rows

### Columns
| Column | Type | Description |
|--------|------|-------------|
| ORDERNUMBER | Integer | Order number |
| QUANTITYORDERED | Integer | Quantity ordered |
| PRICEEACH | Float | Price per unit |
| ORDERLINENUMBER | Integer | Line in order |
| SALES | Float | Total sales amount |
| ORDERDATE | Date | Order date |
| STATUS | String | Shipped / Cancelled / On Hold |
| PRODUCTLINE | String | Product category |
| MSRP | Integer | Manufacturer suggested retail price |
| PRODUCTCODE | String | Product code |
| CUSTOMERNAME | String | Customer name |
| COUNTRY | String | Customer country |
| DEALSIZE | String | Small / Medium / Large |

---

## 📥 How to Download

1. Create a free account at [kaggle.com](https://www.kaggle.com)
2. Click the download links above
3. Extract the CSV files
4. Place them in this `datasets/` folder
5. Use them directly in Excel / Power BI / Tableau
