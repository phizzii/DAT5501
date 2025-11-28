import pytest
import pandas as pd
import numpy as np
import os
import matplotlib

# ensure matplotlib doesn’t try to open GUI windows during tests
matplotlib.use("Agg")

# import the script safely
import importlib.util

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "..", "Week5", "asset_price.py")

@pytest.fixture(scope="module")
def rocket_lab_module():
    spec = importlib.util.spec_from_file_location("asset_price", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_csv_loaded_correctly(rocket_lab_module):
    df = rocket_lab_module.rocket_lab_historical_data_df
    assert isinstance(df, pd.DataFrame)
    assert not df.empty, "The CSV file appears to be empty or missing."


def test_date_column_is_datetime(rocket_lab_module):
    df = rocket_lab_module.rocket_lab_historical_data_df
    assert pd.api.types.is_datetime64_any_dtype(df["Date"]), "Date column is not datetime type."


def test_close_last_is_float(rocket_lab_module):
    df = rocket_lab_module.rocket_lab_historical_data_df
    assert pd.api.types.is_float_dtype(df["Close/Last"]), "Close/Last should be float after cleaning."
    assert not df["Close/Last"].isna().any(), "Close/Last has NaN values after cleaning."


def test_sorted_by_date(rocket_lab_module):
    df = rocket_lab_module.rocket_lab_historical_data_df
    sorted_check = df["Date"].is_monotonic_increasing
    assert sorted_check, "DataFrame is not sorted by date ascending."


def test_daily_percent_change_column_exists(rocket_lab_module):
    df = rocket_lab_module.rocket_lab_historical_data_df
    assert "Daily % Change" in df.columns, "Missing 'Daily % Change' column."
    assert not df["Daily % Change"].isna().any(), "Daily % Change column has NaN values."


def test_daily_percent_change_reasonable_range(rocket_lab_module):
    df = rocket_lab_module.rocket_lab_historical_data_df
    max_change = df["Daily % Change"].abs().max()
    assert max_change < 1000, f"Unrealistic daily % change detected: {max_change}%"


def test_standard_deviation_calculated(rocket_lab_module):
    df = rocket_lab_module.rocket_lab_historical_data_df
    std_val = df["Daily % Change"].std()
    assert isinstance(std_val, float)
    assert std_val >= 0, "Standard deviation should be non-negative."
