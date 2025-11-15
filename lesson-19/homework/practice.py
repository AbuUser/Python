import pandas as pd
import sqlite3

# ============================================================
# Homework 19 — Sales, Customer Orders, Population Salary Analysis
# ============================================================

# ---------------- Homework 1: Sales Data ----------------
print("Homework 1: Sales Data Analysis\n")

sales_df = pd.read_csv("task\\sales_data.csv")

# 1. Group by Category
category_stats = sales_df.groupby('Category').agg(
    total_quantity=pd.NamedAgg(column='Quantity', aggfunc='sum'),
    avg_price=pd.NamedAgg(column='Price', aggfunc='mean'),
    max_quantity=pd.NamedAgg(column='Quantity', aggfunc='max')
)
print("Category-wise aggregate stats:\n", category_stats, "\n")

# 2. Top-selling product in each category
top_products = sales_df.groupby(['Category', 'Product']).agg(
    total_quantity=pd.NamedAgg(column='Quantity', aggfunc='sum')
).reset_index()

top_products_per_category = top_products.loc[top_products.groupby('Category')['total_quantity'].idxmax()]
print("Top-selling product per category:\n", top_products_per_category, "\n")

# 3. Date with highest total sales
sales_df['TotalSale'] = sales_df['Quantity'] * sales_df['Price']
top_sales_date = sales_df.groupby('Date')['TotalSale'].sum().idxmax()
print("Date with highest total sales:", top_sales_date, "\n")


# ---------------- Homework 2: Customer Orders ----------------
print("Homework 2: Customer Orders\n")

orders_df = pd.read_csv("task\\customer_orders.csv")

# 1. Customers with at least 20 orders
orders_count = orders_df.groupby('CustomerID').size()
customers_20plus = orders_count[orders_count >= 20].index
customers_filtered = orders_df[orders_df['CustomerID'].isin(customers_20plus)]
print("Customers with at least 20 orders:\n", customers_filtered['CustomerID'].unique(), "\n")

# 2. Customers with average price per unit > $120
avg_price_per_customer = orders_df.groupby('CustomerID')['Price'].mean()
high_value_customers = avg_price_per_customer[avg_price_per_customer > 120].index
print("Customers with avg price per unit > $120:\n", high_value_customers, "\n")

# 3. Total quantity and total price per product, filter total quantity >= 5
product_stats = orders_df.groupby('Product').agg(
    total_quantity=pd.NamedAgg(column='Quantity', aggfunc='sum'),
    total_price=pd.NamedAgg(column='Price', aggfunc=lambda x: (x*orders_df.loc[x.index,'Quantity']).sum())
)
products_filtered = product_stats[product_stats['total_quantity'] >= 5]
print("Products with total quantity >= 5:\n", products_filtered, "\n")


# ---------------- Homework 3: Population Salary Analysis ----------------
print("Homework 3: Population Salary Analysis\n")

# Connect to SQLite database
conn = sqlite3.connect("task\\population.db")

# Read population table into Pandas
pop_df = pd.read_sql("SELECT * FROM population", conn)

# Read Salary Band definitions
salary_band_df = pd.read_excel("task\\population salary analysis.xlsx")

# Merge salary bands with population to classify salaries
pop_df['SalaryBand'] = pd.cut(
    pop_df['Salary'],
    bins=salary_band_df['Min'].tolist() + [salary_band_df['Max'].max()],
    labels=salary_band_df['Category'],
    right=True
)

# Overall population measures by SalaryBand
salary_analysis = pop_df.groupby('SalaryBand')['Salary'].agg(
    avg_salary='mean',
    median_salary='median',
    count='count'
)
salary_analysis['percentage'] = (salary_analysis['count'] / salary_analysis['count'].sum()) * 100
print("Salary analysis by SalaryBand:\n", salary_analysis, "\n")

# Measures by State and SalaryBand
state_salary_analysis = pop_df.groupby(['State','SalaryBand'])['Salary'].agg(
    avg_salary='mean',
    median_salary='median',
    count='count'
).reset_index()

state_salary_analysis['percentage'] = state_salary_analysis.groupby('State')['count'].apply(lambda x: x/x.sum()*100)
print("Salary analysis by State and SalaryBand:\n", state_salary_analysis, "\n")

# Close connection
conn.close()
