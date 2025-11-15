import pandas as pd
import numpy as np

# ============================================================
# Homework 17 — Pandas Exercises
# ============================================================

# ---------------- Homework 1 ----------------
print("Homework 1\n")

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# 1. Rename columns
df.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True)
print("Renamed columns:\n", df.columns, "\n")

# 2. Print first 3 rows
print("First 3 rows:\n", df.head(3), "\n")

# 3. Mean age
mean_age = df['age'].mean()
print("Mean age:", mean_age, "\n")

# 4. Select only 'first_name' and 'city'
print("Name and City columns:\n", df[['first_name', 'city']], "\n")

# 5. Add 'Salary' column with random values
np.random.seed(0)  # for reproducibility
df['salary'] = np.random.randint(3000, 7000, size=len(df))
print("DataFrame with Salary:\n", df, "\n")

# 6. Summary statistics
print("Summary statistics:\n", df.describe(), "\n")


# ---------------- Homework 2 ----------------
print("Homework 2\n")

sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

# Max
print("Maximum Sales and Expenses:\n", sales_and_expenses[['Sales','Expenses']].max(), "\n")

# Min
print("Minimum Sales and Expenses:\n", sales_and_expenses[['Sales','Expenses']].min(), "\n")

# Mean
print("Average Sales and Expenses:\n", sales_and_expenses[['Sales','Expenses']].mean(), "\n")


# ---------------- Homework 3 ----------------
print("Homework 3\n")

expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# Set 'Category' as index
expenses.set_index('Category', inplace=True)

# Maximum expense per category
print("Maximum expense per category:\n", expenses.max(axis=1), "\n")

# Minimum expense per category
print("Minimum expense per category:\n", expenses.min(axis=1), "\n")

# Average expense per category
print("Average expense per category:\n", expenses.mean(axis=1), "\n")
