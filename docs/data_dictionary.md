# 📖 Data Dictionary — Sales Performance & Business Analytics Dashboard

**Author:** Ishita Prasad (@ishitapd)

---

| Column Name | Description | Data Type | Business Meaning |
| :--- | :--- | :--- | :--- |
| `Row ID` | Unique line-item sequence number | Integer | Row identifier |
| `Order ID` | Unique transaction receipt code | String (VARCHAR) | Identifies customer checkout order |
| `Order Date` | Date when order was placed | Date (YYYY-MM-DD) | Transaction timestamp |
| `Ship Date` | Date when order was dispatched | Date (YYYY-MM-DD) | Logistics dispatch timestamp |
| `Ship Mode` | Shipping service tier selected | Categorical String | First Class, Second Class, Standard |
| `Customer Name` | Name of purchasing customer | String | Individual/Corporate buyer |
| `Segment` | Customer market segment | Categorical String | Consumer, Corporate, Home Office |
| `Region` | Geographic retail zone | Categorical String | West, East, Central, South Zones |
| `City` | City of delivery location | String | Retail destination city |
| `State` | State/province of delivery | String | Geographic state location |
| `Payment` | Payment method used | Categorical String | UPI, Cards, EMI, COD |
| `Category` | High-level product classification | Categorical String | Technology, Furniture, Office Supplies |
| `Sub-Category` | Detailed product sub-type | Categorical String | Phones, Chairs, Storage, Binders |
| `Product Name` | Full commercial product title | String | SKUs sold |
| `Sales` | Gross revenue amount in INR (₹) | Decimal/Float | Top-line transaction dollar value |
| `Quantity` | Number of units purchased | Integer | Unit volume |
| `Discount` | Promotional discount percentage | Float (0.0 to 0.8) | Price reduction percentage |
| `Profit` | Net earnings/loss in INR (₹) | Decimal/Float | Bottom-line profit contribution |
