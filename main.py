from fastapi import FastAPI

from analytics import (
    get_summary,
    get_category_sales,
    get_region_sales,
    get_top_cities
)


app = FastAPI(
    title="Supermart Sales Analytics API",
    description="Simple data analysis using Pandas, NumPy and FastAPI",
    version="1.0.0"
)


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():
    return {
        "message": "Sales Analytics API is working!"
    }


# =========================================================
# SUMMARY
# =========================================================

@app.get("/analytics/summary")
def analytics_summary():
    return get_summary()


# =========================================================
# CATEGORY SALES
# =========================================================

@app.get("/analytics/category")
def analytics_category():
    return get_category_sales()


# =========================================================
# REGION SALES
# =========================================================

@app.get("/analytics/region")
def analytics_region():
    return get_region_sales()


# =========================================================
# TOP 5 CITIES
# =========================================================

@app.get("/analytics/top-cities")
def analytics_top_cities():
    return get_top_cities()