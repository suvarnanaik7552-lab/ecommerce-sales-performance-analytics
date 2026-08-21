# ============================================================
# ECOMMERCE SALES PERFORMANCE ANALYTICS
# ============================================================

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 2. PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(
    BASE_DIR,
    "amazon_sales_dataset.csv"
)

CHARTS_DIR = os.path.join(
    BASE_DIR,
    "charts"
)

OUTPUTS_DIR = os.path.join(
    BASE_DIR,
    "outputs"
)


# Create output folders if they don't exist
os.makedirs(CHARTS_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)


# ============================================================
# 3. LOAD DATA
# ============================================================

df = pd.read_csv(DATA_FILE)

print("\nData loaded successfully.")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]:,}")

# ============================================================
# 4. DATA CLEANING & PREPARATION
# ============================================================

print("\n" + "=" * 55)
print("DATA CLEANING & PREPARATION")
print("=" * 55)

# ------------------------------------------------------------
# 4.1 Check original dataset size
# ------------------------------------------------------------

original_rows = len(df)

print(f"\nOriginal rows: {original_rows:,}")


# ------------------------------------------------------------
# 4.2 Check duplicate rows
# ------------------------------------------------------------

duplicate_rows = df.duplicated().sum()

print(f"Duplicate rows found: {duplicate_rows:,}")


# Remove duplicate rows

if duplicate_rows > 0:
    df = df.drop_duplicates().copy()

print(f"Rows after duplicate removal: {len(df):,}")


# ------------------------------------------------------------
# 4.3 Convert date columns
# ------------------------------------------------------------

date_columns = [
    "order_date",
    "ship_date",
    "delivery_date"
]

for column in date_columns:

    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )


# ------------------------------------------------------------
# 4.4 Check missing values in important columns
# ------------------------------------------------------------

important_columns = [
    "order_id",
    "customer_id",
    "order_date",
    "total_sales",
    "quantity",
    "unit_price",
    "category"
]

missing_values = df[important_columns].isnull().sum()

print("\nMissing values in important columns:")
print(missing_values)


# ------------------------------------------------------------
# 4.5 Remove rows missing essential business information
# ------------------------------------------------------------

df = df.dropna(
    subset=[
        "order_id",
        "customer_id",
        "order_date",
        "total_sales",
        "quantity"
    ]
).copy()


# ------------------------------------------------------------
# 4.6 Check invalid numerical values
# ------------------------------------------------------------

negative_sales = (
    df["total_sales"] < 0
).sum()

invalid_quantity = (
    df["quantity"] <= 0
).sum()

negative_unit_price = (
    df["unit_price"] < 0
).sum()

negative_shipping = (
    df["shipping_cost"] < 0
).sum()


print("\nInvalid numerical values:")

print(
    f"Negative sales: {negative_sales:,}"
)

print(
    f"Invalid quantity: {invalid_quantity:,}"
)

print(
    f"Negative unit price: {negative_unit_price:,}"
)

print(
    f"Negative shipping cost: {negative_shipping:,}"
)


# ------------------------------------------------------------
# 4.7 Remove invalid business records
# ------------------------------------------------------------

df = df[
    (df["total_sales"] >= 0) &
    (df["quantity"] > 0) &
    (df["unit_price"] >= 0) &
    (df["shipping_cost"] >= 0)
].copy()


# ------------------------------------------------------------
# 4.8 Calculate delivery days
# ------------------------------------------------------------

df["delivery_days"] = (
    df["delivery_date"] -
    df["order_date"]
).dt.days


# ------------------------------------------------------------
# 4.9 Create valid delivery dataset
# ------------------------------------------------------------

delivery_df = df[
    df["delivery_days"] >= 0
].copy()


# ------------------------------------------------------------
# 4.10 Create month column
# ------------------------------------------------------------

df["month"] = (
    df["order_date"]
    .dt.to_period("M")
)


# ============================================================
# 5. FINAL DATA QUALITY CHECK
# ============================================================

print("\n" + "=" * 55)
print("FINAL DATA QUALITY CHECK")
print("=" * 55)

print(
    f"\nFinal rows: {len(df):,}"
)

print(
    f"Rows removed: "
    f"{original_rows - len(df):,}"
)

print(
    f"Final columns: {df.shape[1]:,}"
)

print(
    f"Remaining duplicate rows: "
    f"{df.duplicated().sum():,}"
)

print(
    f"Remaining missing values: "
    f"{df.isnull().sum().sum():,}"
)

print(
    f"Valid delivery records: "
    f"{len(delivery_df):,}"
)

print("=" * 55)



# ============================================================
# 6. KPI CALCULATIONS
# ============================================================

total_sales = df["total_sales"].sum()

total_orders = df["order_id"].nunique()

total_customers = df["customer_id"].nunique()

total_quantity = df["quantity"].sum()

average_order_value = (
    total_sales / total_orders
)

average_items_per_order = (
    total_quantity / total_orders
)

average_delivery_days = (
    delivery_df["delivery_days"].mean()
)


# ============================================================
# 7. CUSTOMER ANALYSIS
# ============================================================

orders_per_customer = (
    total_orders /
    total_customers
)

customer_order_counts = (
    df["customer_id"]
    .value_counts()
)

repeat_customers = (
    customer_order_counts > 1
).sum()

repeat_customer_percentage = (
    repeat_customers /
    total_customers *
    100
)


top_customers = (
    df.groupby("customer_name")["total_sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


# ============================================================
# 8. CATEGORY ANALYSIS
# ============================================================

category_sales = (
    df.groupby("category")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)

category_quantity = (
    df.groupby("category")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

category_avg_sales = (
    df.groupby("category")["total_sales"]
    .mean()
    .sort_values(ascending=False)
)

category_discount = (
    df.groupby("category")["discount"]
    .mean()
    .sort_values(ascending=False)
)

category_shipping = (
    df.groupby("category")["shipping_cost"]
    .mean()
    .sort_values(ascending=False)
)


# ============================================================
# 9. SUB-CATEGORY ANALYSIS
# ============================================================

subcat_sales = (
    df.groupby("sub_category")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)

subcat_quantity = (
    df.groupby("sub_category")["quantity"]
    .sum()
    .sort_values(ascending=False)
)


# ============================================================
# 10. PRODUCT ANALYSIS
# ============================================================

top_products = (
    df.groupby("product_name")["total_sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


# ============================================================
# 11. BRAND ANALYSIS
# ============================================================

top_brands = (
    df.groupby("brand")["total_sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


# ============================================================
# 12. STATE ANALYSIS
# ============================================================

top_states = (
    df.groupby("state")["total_sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


# ============================================================
# 13. PAYMENT ANALYSIS
# ============================================================

payment_sales = (
    df.groupby("payment_method")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)

payment_percentage = (
    payment_sales /
    total_sales *
    100
)


# ============================================================
# 14. MONTHLY ANALYSIS
# ============================================================

monthly_sales = (
    df.groupby("month")["total_sales"]
    .sum()
)

monthly_orders = (
    df.groupby("month")["order_id"]
    .nunique()
)

monthly_average_sales = (
    df.groupby("month")["total_sales"]
    .mean()
)


# ============================================================
# 15. ORDER STATUS ANALYSIS
# ============================================================

order_status_sales = (
    df.groupby("order_status")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)


# ============================================================
# 16. DISCOUNT ANALYSIS
# ============================================================

average_discount = (
    df["discount"].mean()
)

discount_sales = (
    df.groupby("discount")["total_sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


# ============================================================
# 17. SHIPPING ANALYSIS
# ============================================================

average_shipping_cost = (
    df["shipping_cost"].mean()
)

total_shipping_cost = (
    df["shipping_cost"].sum()
)


# ============================================================
# 18. DELIVERY ANALYSIS
# ============================================================

minimum_delivery_days = (
    delivery_df["delivery_days"].min()
)

maximum_delivery_days = (
    delivery_df["delivery_days"].max()
)

category_delivery = (
    delivery_df
    .groupby("category")["delivery_days"]
    .mean()
    .sort_values(ascending=False)
)

payment_delivery = (
    delivery_df
    .groupby("payment_method")["delivery_days"]
    .mean()
    .sort_values(ascending=False)
)


# ============================================================
# 19. PRICE & QUANTITY ANALYSIS
# ============================================================

average_unit_price = (
    df["unit_price"].mean()
)

maximum_unit_price = (
    df["unit_price"].max()
)

quantity_sales = (
    df.groupby("quantity")["total_sales"]
    .sum()
)

quantity_average_sales = (
    df.groupby("quantity")["total_sales"]
    .mean()
)


# ============================================================
# 20. CORRELATION ANALYSIS
# ============================================================

correlation = df[
    [
        "quantity",
        "unit_price",
        "discount",
        "shipping_cost",
        "total_sales"
    ]
].corr()


# ============================================================
# 21. KPI SUMMARY
# ============================================================

print("\n" + "=" * 55)
print("KPI SUMMARY")
print("=" * 55)

print(
    f"Total Sales: ₹{total_sales:,.2f}"
)

print(
    f"Total Orders: {total_orders:,}"
)

print(
    f"Total Customers: {total_customers:,}"
)

print(
    f"Average Order Value: ₹{average_order_value:,.2f}"
)

print(
    f"Average Delivery Days: "
    f"{average_delivery_days:.2f}"
)

print(
    f"Total Quantity Sold: "
    f"{total_quantity:,}"
)

print(
    f"Average Items per Order: "
    f"{average_items_per_order:.2f}"
)

print(
    f"Repeat Customer %: "
    f"{repeat_customer_percentage:.2f}%"
)

print("=" * 55)


# ============================================================
# 22. SAVE KPI SUMMARY
# ============================================================

kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Orders",
        "Total Customers",
        "Average Order Value",
        "Average Delivery Days",
        "Total Quantity Sold",
        "Average Items per Order",
        "Repeat Customer Percentage"
    ],

    "Value": [
        total_sales,
        total_orders,
        total_customers,
        average_order_value,
        average_delivery_days,
        total_quantity,
        average_items_per_order,
        repeat_customer_percentage
    ]
})


kpi_file = os.path.join(
    OUTPUTS_DIR,
    "kpi_summary.csv"
)

kpi_summary.to_csv(
    kpi_file,
    index=False
)


# ============================================================
# 23. SAVE ANALYSIS TABLES
# ============================================================

category_sales.to_csv(
    os.path.join(
        OUTPUTS_DIR,
        "category_sales.csv"
    )
)

monthly_sales.to_csv(
    os.path.join(
        OUTPUTS_DIR,
        "monthly_sales.csv"
    )
)

top_products.to_csv(
    os.path.join(
        OUTPUTS_DIR,
        "top_products.csv"
    )
)

top_customers.to_csv(
    os.path.join(
        OUTPUTS_DIR,
        "top_customers.csv"
    )
)

top_brands.to_csv(
    os.path.join(
        OUTPUTS_DIR,
        "top_brands.csv"
    )
)

top_states.to_csv(
    os.path.join(
        OUTPUTS_DIR,
        "top_states.csv"
    )
)


# ============================================================
# 24. CHART FUNCTION
# ============================================================

def save_bar_chart(
    data,
    title,
    xlabel,
    ylabel,
    filename,
    rotation=0
):

    plt.figure(figsize=(10, 6))

    data.plot(kind="bar")

    plt.title(title)

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.xticks(
        rotation=rotation
    )

    plt.tight_layout()

    filepath = os.path.join(
        CHARTS_DIR,
        filename
    )

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# ============================================================
# 25. BAR CHARTS
# ============================================================

save_bar_chart(
    monthly_sales,
    "Monthly Sales",
    "Month",
    "Total Sales",
    "monthly_sales.png"
)


save_bar_chart(
    category_sales,
    "Sales by Category",
    "Category",
    "Total Sales",
    "category_sales.png"
)


save_bar_chart(
    payment_sales,
    "Sales by Payment Method",
    "Payment Method",
    "Total Sales",
    "payment_sales.png"
)


save_bar_chart(
    subcat_sales,
    "Sales by Sub-Category",
    "Sub-Category",
    "Total Sales",
    "subcategory_sales.png",
    45
)


save_bar_chart(
    top_states,
    "Top 10 States by Sales",
    "State",
    "Total Sales",
    "top_states.png",
    45
)


save_bar_chart(
    top_customers,
    "Top 10 Customers by Sales",
    "Customer",
    "Total Sales",
    "top_customers.png",
    45
)


save_bar_chart(
    top_products,
    "Top 10 Products by Sales",
    "Product",
    "Total Sales",
    "top_products.png",
    45
)


save_bar_chart(
    top_brands,
    "Top 10 Brands by Sales",
    "Brand",
    "Total Sales",
    "top_brands.png",
    45
)


save_bar_chart(
    category_delivery,
    "Average Delivery Time by Category",
    "Category",
    "Average Delivery Days",
    "category_delivery.png"
)


save_bar_chart(
    payment_delivery,
    "Average Delivery Time by Payment Method",
    "Payment Method",
    "Average Delivery Days",
    "payment_delivery.png"
)


save_bar_chart(
    quantity_sales,
    "Total Sales by Order Quantity",
    "Quantity",
    "Total Sales",
    "quantity_sales.png"
)


save_bar_chart(
    quantity_average_sales,
    "Average Sales by Order Quantity",
    "Quantity",
    "Average Sales",
    "quantity_average_sales.png"
)


save_bar_chart(
    discount_sales,
    "Top 10 Discount Levels by Sales",
    "Discount",
    "Total Sales",
    "discount_sales.png",
    45
)


# ============================================================
# 26. SCATTER CHART FUNCTION
# ============================================================

def save_scatter_chart(
    x,
    y,
    title,
    xlabel,
    ylabel,
    filename
):

    plt.figure(figsize=(10, 6))

    plt.scatter(
        x,
        y,
        alpha=0.5
    )

    plt.title(title)

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.tight_layout()

    filepath = os.path.join(
        CHARTS_DIR,
        filename
    )

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# ============================================================
# 27. SCATTER CHARTS
# ============================================================

save_scatter_chart(
    df["discount"],
    df["total_sales"],
    "Sales vs Discount",
    "Discount",
    "Total Sales",
    "sales_vs_discount.png"
)


save_scatter_chart(
    df["quantity"],
    df["total_sales"],
    "Quantity vs Total Sales",
    "Quantity",
    "Total Sales",
    "quantity_vs_sales.png"
)


save_scatter_chart(
    df["unit_price"],
    df["total_sales"],
    "Unit Price vs Total Sales",
    "Unit Price",
    "Total Sales",
    "unit_price_vs_sales.png"
)


save_scatter_chart(
    delivery_df["shipping_cost"],
    delivery_df["delivery_days"],
    "Shipping Cost vs Delivery Time",
    "Shipping Cost",
    "Delivery Days",
    "shipping_vs_delivery.png"
)


# ============================================================
# 28. HISTOGRAM FUNCTION
# ============================================================

def save_histogram(
    data,
    title,
    xlabel,
    ylabel,
    filename,
    bins=20
):

    plt.figure(figsize=(10, 6))

    plt.hist(
        data,
        bins=bins
    )

    plt.title(title)

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.tight_layout()

    filepath = os.path.join(
        CHARTS_DIR,
        filename
    )

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# ============================================================
# 29. HISTOGRAMS
# ============================================================

save_histogram(
    delivery_df["delivery_days"],
    "Delivery Days Distribution",
    "Delivery Days",
    "Number of Orders",
    "delivery_days_distribution.png"
)


save_histogram(
    df["total_sales"],
    "Total Sales Distribution",
    "Total Sales",
    "Number of Orders",
    "sales_distribution.png",
    30
)


# ============================================================
# 30. FINAL OUTPUT
# ============================================================

print("\n" + "=" * 55)
print("BUSINESS ANALYSIS SUMMARY")
print("=" * 55)

print("\nTop Categories:")
print(category_sales)

print("\nTop Products:")
print(top_products)

print("\nTop Customers:")
print(top_customers)

print("\nTop Brands:")
print(top_brands)

print("\nTop States:")
print(top_states)

print("\nPayment Method Sales:")
print(payment_sales)

print("\nCorrelation Matrix:")
print(correlation)

print("\n" + "=" * 55)

print("Analysis completed successfully!")

print(
    f"\nCharts saved to:\n{CHARTS_DIR}"
)

print(
    f"\nAnalysis outputs saved to:\n{OUTPUTS_DIR}"
)

print("=" * 55)