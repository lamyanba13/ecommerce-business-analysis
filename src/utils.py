from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
CLEANED_DATA_DIR = PROJECT_ROOT / "data" / "cleaned"
VISUALS_DIR = PROJECT_ROOT / "visuals"


def ensure_directories() -> None:
    """Create project directories if they do not already exist."""
    for directory in (RAW_DATA_DIR, CLEANED_DATA_DIR, VISUALS_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def load_data(filename: str) -> pd.DataFrame:
    """Load a CSV file from the raw data folder."""
    ensure_directories()
    file_path = RAW_DATA_DIR / filename
    return pd.read_csv(file_path)


def save_dataframe(df: pd.DataFrame, filename: str) -> Path:
    """Save a cleaned DataFrame to the cleaned data folder."""
    ensure_directories()
    file_path = CLEANED_DATA_DIR / filename
    df.to_csv(file_path, index=False)
    return file_path


def save_plot(fig, filename: str) -> Path:
    """Save a matplotlib figure to the visuals folder."""
    ensure_directories()
    file_path = VISUALS_DIR / filename
    fig.savefig(file_path, dpi=300, bbox_inches="tight")
    return file_path


def find_project_root(start_path: Path | None = None) -> Path:
    """Find the project root from the current working location.

    This helps notebooks run reliably whether Jupyter is started from the
    repository root or directly from the notebooks folder.
    """
    start = (start_path or Path.cwd()).resolve()
    for candidate in (start, *start.parents):
        if (candidate / "src").exists() and (candidate / "data").exists():
            return candidate
    raise FileNotFoundError("Could not locate the project root.")
