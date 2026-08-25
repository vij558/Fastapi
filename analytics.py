import pandas as pd
import numpy as np


FILE_NAME = "Supermart Grocery Sales - Retail Analytics Dataset.csv"


# =========================================================
# LOAD DATA
# =========================================================

def load_data():
    df = pd.read_csv(FILE_NAME)

    # Handle mixed date formats
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="mixed",
        errors="coerce"
    )

    return df


# =========================================================
# 1. SUMMARY
# =========================================================

def get_summary():
    df = load_data()

    sales = df["Sales"].to_numpy()
    profit = df["Profit"].to_numpy()

    return {
        "total_orders": len(df),
        "total_sales": float(df["Sales"].sum()),
        "average_sales": float(df["Sales"].mean()),
        "total_profit": float(df["Profit"].sum()),
        "average_profit": float(df["Profit"].mean()),
        "maximum_sale": float(np.max(sales)),
        "minimum_sale": float(np.min(sales)),
        "sales_standard_deviation": float(np.std(sales))
    }


# =========================================================
# 2. SALES BY CATEGORY
# =========================================================

def get_category_sales():
    df = load_data()

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return {
        category: float(sales)
        for category, sales in category_sales.items()
    }


# =========================================================
# 3. SALES BY REGION
# =========================================================

def get_region_sales():
    df = load_data()

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return {
        region: float(sales)
        for region, sales in region_sales.items()
    }


# =========================================================
# 4. TOP 5 CITIES BY SALES
# =========================================================

def get_top_cities():
    df = load_data()

    top_cities = (
        df.groupby("City")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    return {
        city: float(sales)
        for city, sales in top_cities.items()
    }