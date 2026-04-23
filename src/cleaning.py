from __future__ import annotations

import pandas as pd


EXPECTED_COLUMNS = [
    "Order ID",
    "Order Date",
    "Customer ID",
    "Product Name",
    "Category",
    "Sales",
    "Quantity",
    "Discount",
    "Profit",
    "Region",
]


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize whitespace in column names."""
    cleaned = df.copy()
    cleaned.columns = [column.strip() for column in cleaned.columns]
    return cleaned


def validate_required_columns(df: pd.DataFrame) -> None:
    """Raise an error if expected columns are missing."""
    missing = [column for column in EXPECTED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def clean_ecommerce_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare an e-commerce dataset for analysis."""
    cleaned = standardize_column_names(df)
    validate_required_columns(cleaned)

    cleaned = cleaned.drop_duplicates().copy()
    cleaned["Order Date"] = pd.to_datetime(cleaned["Order Date"], errors="coerce")

    numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]
    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    # Keep only records with the minimum business-critical fields required
    # for downstream KPI and trend analysis.
    cleaned = cleaned.dropna(subset=["Order ID", "Order Date", "Customer ID", "Product Name"])

    for column in ["Category", "Region"]:
        cleaned[column] = cleaned[column].astype(str).str.strip()

    cleaned["Year"] = cleaned["Order Date"].dt.year
    cleaned["Month"] = cleaned["Order Date"].dt.month
    cleaned["Month Name"] = cleaned["Order Date"].dt.month_name()
    cleaned["Profit Margin"] = cleaned["Profit"] / cleaned["Sales"].replace(0, pd.NA)

    return cleaned.reset_index(drop=True)


def missing_value_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return a quick summary of missing values."""
    return pd.DataFrame(
        {
            "missing_count": df.isna().sum(),
            "missing_percent": (df.isna().mean() * 100).round(2),
        }
    ).sort_values("missing_count", ascending=False)
