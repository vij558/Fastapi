import pandas as pd
import numpy as np

# =========================================================
# 1. LOAD DATASET
# =========================================================

FILE_NAME = "Supermart Grocery Sales - Retail Analytics Dataset.csv"

df = pd.read_csv(FILE_NAME)

print("========================================")
print("       SUPERMART SALES ANALYSIS")
print("========================================")

print("\n===== DATASET INFORMATION =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# =========================================================
# 2. SHOW COLUMNS
# =========================================================

print("\n===== COLUMNS =====")
print(df.columns.tolist())


# =========================================================
# 3. FIRST 5 ROWS
# =========================================================

print("\n===== FIRST 5 ROWS =====")
print(df.head())


# =========================================================
# 4. CHECK MISSING VALUES
# =========================================================

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


# =========================================================
# 5. BASIC SALES ANALYSIS USING PANDAS
# =========================================================

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()

total_profit = df["Profit"].sum()
average_profit = df["Profit"].mean()

print("\n===== BASIC ANALYSIS =====")
print("Total Sales   :", round(total_sales, 2))
print("Average Sales :", round(average_sales, 2))
print("Total Profit  :", round(total_profit, 2))
print("Average Profit:", round(average_profit, 2))


# =========================================================
# 6. NUMPY ANALYSIS
# =========================================================

sales = df["Sales"].to_numpy()
profits = df["Profit"].to_numpy()

print("\n===== NUMPY ANALYSIS =====")

print("Maximum Sale           :", np.max(sales))
print("Minimum Sale           :", np.min(sales))
print("Sales Standard Deviation:",
      round(np.std(sales), 2))

print("Maximum Profit         :", np.max(profits))
print("Minimum Profit         :", np.min(profits))
print("Profit Standard Deviation:",
      round(np.std(profits), 2))


# =========================================================
# 7. SALES BY CATEGORY
# =========================================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY CATEGORY =====")
print(category_sales)


# =========================================================
# 8. PROFIT BY CATEGORY
# =========================================================

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== PROFIT BY CATEGORY =====")
print(category_profit)


# =========================================================
# 9. TOP 5 CITIES BY SALES
# =========================================================

top_cities = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n===== TOP 5 CITIES BY SALES =====")
print(top_cities)


# =========================================================
# 10. TOP 5 SUB-CATEGORIES
# =========================================================

top_subcategories = (
    df.groupby("Sub Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n===== TOP 5 SUB-CATEGORIES =====")
print(top_subcategories)


# =========================================================
# 11. SALES BY REGION
# =========================================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY REGION =====")
print(region_sales)


# =========================================================
# 12. DATE ANALYSIS
# =========================================================

# IMPORTANT:
# The Kaggle dataset contains mixed date formats such as:
# 11-08-2017
# 06-12-2017
# 4/15/2018
#
# Therefore we use format="mixed".

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed",
    errors="coerce"
)

# Check if any dates failed
invalid_dates = df["Order Date"].isna().sum()

print("\n===== DATE CHECK =====")
print("Invalid dates:", invalid_dates)


# =========================================================
# 13. SALES BY YEAR
# =========================================================

df["Year"] = df["Order Date"].dt.year

yearly_sales = (
    df.groupby("Year")["Sales"]
    .sum()
    .sort_index()
)

print("\n===== SALES BY YEAR =====")
print(yearly_sales)


# =========================================================
# 14. FINAL MESSAGE
# =========================================================

print("\n========================================")
print("       ANALYSIS COMPLETED")
print("========================================")