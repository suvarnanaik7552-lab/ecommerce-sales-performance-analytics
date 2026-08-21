# E-commerce Sales Performance Analytics

## 📌 Project Overview

This project analyzes e-commerce sales data to identify important business trends, customer behavior, product performance, sales drivers, and delivery performance.

The analysis was developed using **Python, Pandas, and Matplotlib**. The project follows a complete data analytics workflow:

**Data Loading → Data Cleaning → Data Quality Validation → KPI Calculation → Business Analysis → Visualization → Exporting Results**

The goal of this project is to transform raw e-commerce transaction data into meaningful business insights that can support better decision-making.

---

## 🎯 Business Objectives

The project answers important business questions such as:

* How much total revenue was generated?
* How many orders and customers were recorded?
* What is the Average Order Value?
* Which product categories generate the highest sales?
* Which products and brands perform best?
* Which customers generate the most revenue?
* Which states contribute the most sales?
* Which payment methods generate the most sales?
* How do sales change over time?
* How do discounts relate to sales?
* How does order quantity affect sales?
* What is the average delivery time?
* Which categories have longer delivery times?
* What is the relationship between shipping cost and delivery time?
* What factors are associated with higher sales?

---

## 🗂️ Dataset

The dataset contains **10,000 e-commerce transactions** and **21 columns**.

### Main Data Fields

| Column           | Description                       |
| ---------------- | --------------------------------- |
| `order_id`       | Unique order identifier           |
| `order_date`     | Date when the order was placed    |
| `ship_date`      | Date when the order was shipped   |
| `delivery_date`  | Date when the order was delivered |
| `order_status`   | Current order status              |
| `customer_id`    | Unique customer identifier        |
| `customer_name`  | Customer name                     |
| `country`        | Customer country                  |
| `state`          | Customer state                    |
| `city`           | Customer city                     |
| `product_id`     | Product identifier                |
| `product_name`   | Product name                      |
| `category`       | Product category                  |
| `sub_category`   | Product sub-category              |
| `brand`          | Product brand                     |
| `quantity`       | Quantity ordered                  |
| `unit_price`     | Price per unit                    |
| `discount`       | Discount applied                  |
| `shipping_cost`  | Shipping cost                     |
| `total_sales`    | Total sales amount                |
| `payment_method` | Payment method                    |

---

## 🛠️ Tools & Technologies

* **Python**
* **Pandas**
* **Matplotlib**
* **CSV**
* **Data Cleaning**
* **Exploratory Data Analysis (EDA)**
* **Business Analysis**
* **Data Visualization**
* **Statistical/Correlation Analysis**

---

## 🔄 Project Workflow

### 1. Data Loading

The project loads the CSV dataset using Pandas and automatically determines the project directory using Python's `os` module.

This makes the project easier to run without hardcoding an absolute file path.

---

### 2. Data Cleaning & Preparation

The project performs several data-quality checks and cleaning operations:

* Checks duplicate records
* Removes duplicate rows
* Converts date columns into datetime format
* Checks missing values in important business columns
* Removes records missing essential information
* Checks invalid numerical values
* Removes invalid sales, quantity, price, and shipping records
* Calculates delivery days
* Creates a monthly analysis column

These steps help ensure that the analysis is based on cleaner and more reliable data.

---

### 3. Data Quality Validation

After cleaning, the project performs a final validation by checking:

* Final number of rows
* Number of rows removed
* Number of columns
* Remaining duplicates
* Remaining missing values
* Valid delivery records

---

## 📊 KPI Analysis

The project calculates the following key performance indicators:

* **Total Sales**
* **Total Orders**
* **Total Customers**
* **Average Order Value (AOV)**
* **Average Delivery Days**
* **Total Quantity Sold**
* **Average Items per Order**
* **Repeat Customer Percentage**

## The KPI summary is also exported as a CSV file for further reporting.

## 👥 Customer Analysis

Customer analysis includes:

* Orders per customer
* Repeat customer count
* Repeat customer percentage
* Top 10 customers by sales

This helps identify high-value customers and understand customer purchasing behavior.

---

## 🛍️ Product & Category Analysis

The project analyzes sales performance across:

* Categories
* Sub-categories
* Products
* Brands

It identifies the top-performing categories, products, and brands based on total sales.

---

## 🌎 Geographic Analysis

Sales performance is analyzed by state to identify the highest-performing geographic markets.

The project generates a **Top 10 States by Sales** analysis.

---

## 💳 Payment Analysis

The project evaluates sales performance by payment method and calculates the percentage contribution of each payment method to total sales.

---

## 📅 Time-Based Analysis

Monthly analysis is performed to understand sales trends over time.

The project calculates:

* Monthly sales
* Monthly orders
* Monthly average sales

---

## 🚚 Delivery & Shipping Analysis

The project calculates:

* Average delivery days
* Minimum delivery days
* Maximum delivery days
* Average delivery time by category
* Average delivery time by payment method
* Total shipping cost
* Average shipping cost

It also analyzes the relationship between shipping cost and delivery time.

---

## 📈 Correlation Analysis

Correlation analysis is performed between:

* Quantity
* Unit Price
* Discount
* Shipping Cost
* Total Sales

This helps identify relationships between numerical business variables.

---

## 📊 Visualizations

The project automatically generates multiple visualizations using Matplotlib.

### Bar Charts

* Monthly Sales
* Sales by Category
* Sales by Payment Method
* Sales by Sub-Category
* Top 10 States by Sales
* Top 10 Customers by Sales
* Top 10 Products by Sales
* Top 10 Brands by Sales
* Average Delivery Time by Category
* Average Delivery Time by Payment Method
* Total Sales by Order Quantity
* Average Sales by Order Quantity
* Top Discount Levels by Sales

### Scatter Plots

* Sales vs Discount
* Quantity vs Total Sales
* Unit Price vs Total Sales
* Shipping Cost vs Delivery Time

### Histograms

* Delivery Days Distribution
* Total Sales Distribution

The charts are automatically saved as high-resolution PNG files.

---

## 📁 Project Structure

```text
ecommerce-sales-performance-analytics/
│
├── amazon_sales_dataset.csv
├── ecommerce_sales_analysis.py
├── README.md
│
├── charts/
│   ├── monthly_sales.png
│   ├── category_sales.png
│   ├── payment_sales.png
│   ├── subcategory_sales.png
│   ├── top_states.png
│   ├── top_customers.png
│   ├── top_products.png
│   ├── top_brands.png
│   ├── category_delivery.png
│   ├── payment_delivery.png
│   ├── quantity_sales.png
│   ├── quantity_average_sales.png
│   ├── discount_sales.png
│   ├── sales_vs_discount.png
│   ├── quantity_vs_sales.png
│   ├── unit_price_vs_sales.png
│   ├── shipping_vs_delivery.png
│   ├── delivery_days_distribution.png
│   └── sales_distribution.png
│
└── outputs/
    ├── kpi_summary.csv
    ├── category_sales.csv
    ├── monthly_sales.csv
    ├── top_products.csv
    ├── top_customers.csv
    ├── top_brands.csv
    └── top_states.csv
```

The Python script automatically creates the `charts` and `outputs` directories if they do not already exist.

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### Step 2: Open the project folder

```bash
cd ecommerce-sales-performance-analytics
```

### Step 3: Install required libraries

```bash
pip install pandas matplotlib
```

### Step 4: Run the analysis

```bash
python ecommerce_sales_analysis.py
```

### Step 5: View the results

After execution:

* Check the `charts/` folder for visualizations.
* Check the `outputs/` folder for analysis tables and KPI results.

The script prints the final business analysis summary and confirms where charts and output files have been saved.

---

## 💡 Key Business Insights

The analysis can be used to identify:

* Revenue-generating product categories
* High-value customers
* Top-performing products and brands
* Strong geographic markets
* Popular payment methods
* Monthly sales trends
* Customer repeat-purchase behavior
* Delivery performance
* Shipping-cost patterns
* Relationships between discounts, quantity, price, and sales

---

## 🎯 Business Value

This project demonstrates how raw transactional data can be transformed into business-focused information.

The analysis can help an e-commerce business:

* Monitor sales performance
* Identify high-value customers
* Understand product demand
* Evaluate delivery performance
* Monitor shipping costs
* Identify high-performing markets
* Track important KPIs
* Support data-driven business decisions

---

## 🚀 Future Improvements

Possible future enhancements include:

* Building an interactive **Power BI dashboard**
* Adding SQL-based analysis
* Creating automated KPI reporting
* Adding customer segmentation
* Performing sales forecasting
* Adding profitability analysis
* Creating a more detailed cohort/retention analysis
* Deploying the analysis as an interactive dashboard

---

## 👩‍💻 Skills Demonstrated

**Python | Pandas | Matplotlib | Data Cleaning | EDA | KPI Analysis | Business Analysis | Data Visualization | Statistical Analysis | Data Quality Validation**

---

## 📌 Project Outcome

This project demonstrates an end-to-end approach to **e-commerce sales performance analytics**, from raw data preparation to KPI calculation, business analysis, visualization, and automated output generation.
