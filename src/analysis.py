from __future__ import annotations

import numpy as np
import pandas as pd


def business_summary(df: pd.DataFrame) -> dict[str, float]:
    """Return top-level business metrics."""
    total_orders = df["Order ID"].nunique()
    total_sales = float(df["Sales"].sum())
    total_profit = float(df["Profit"].sum())
    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "total_quantity": float(df["Quantity"].sum()),
        "total_orders": float(total_orders),
        "average_discount": float(df["Discount"].mean()),
        "average_order_value": float(np.divide(total_sales, total_orders)) if total_orders else 0.0,
        "profit_margin": float(np.divide(total_profit, total_sales)) if total_sales else 0.0,
    }


def sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales and profit by category."""
    return (
        df.groupby("Category", as_index=False)
        .agg(
            sales=("Sales", "sum"),
            profit=("Profit", "sum"),
            quantity=("Quantity", "sum"),
        )
        .sort_values("sales", ascending=False)
    )


def sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales and profit by region."""
    return (
        df.groupby("Region", as_index=False)
        .agg(
            sales=("Sales", "sum"),
            profit=("Profit", "sum"),
            orders=("Order ID", "nunique"),
        )
        .sort_values("sales", ascending=False)
    )


def top_products_by_sales(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Return the best-selling products."""
    return (
        df.groupby("Product Name", as_index=False)
        .agg(sales=("Sales", "sum"), profit=("Profit", "sum"))
        .sort_values("sales", ascending=False)
        .head(top_n)
    )


def monthly_performance(df: pd.DataFrame) -> pd.DataFrame:
    """Return monthly sales and profit trends."""
    monthly = (
        df.assign(Month_Start=df["Order Date"].dt.to_period("M").dt.to_timestamp())
        .groupby("Month_Start", as_index=False)
        .agg(sales=("Sales", "sum"), profit=("Profit", "sum"), orders=("Order ID", "nunique"))
        .sort_values("Month_Start")
    )
    return monthly


def discount_profit_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize profitability by discount level."""
    analysis = df.copy()
    # Group discounts into business-friendly ranges so the effect of
    # discounting on profitability is easier to explain to stakeholders.
    analysis["Discount Band"] = pd.cut(
        analysis["Discount"],
        bins=[-0.01, 0.0, 0.1, 0.2, 0.3, 1.0],
        labels=["0%", "1-10%", "11-20%", "21-30%", "30%+"],
    )
    return (
        analysis.groupby("Discount Band", as_index=False, observed=False)
        .agg(
            sales=("Sales", "sum"),
            profit=("Profit", "sum"),
            average_profit=("Profit", "mean"),
        )
        .sort_values("Discount Band")
    )
