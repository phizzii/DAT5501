import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pytest

# import functions from my script
from Week8and9.daily_price_change_sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    split_array,
    run_sorting_algorithm
)


@pytest.fixture
def df():
    # load Rocket Lab dataset once for all tests
    return pd.read_csv("datasets/HistoricalData_1761069203394.csv")

def test_csv_loads(df):
    # loading and cleaning sets
    assert not df.empty, "Dataframe should not be empty"
    assert {"Date", "High", "Low"}.issubset(df.columns)


def test_price_cleaning(df):
    # making sure the dollar signs are removed otherwise the type is set to NaN
    df["High"] = df["High"].str.removeprefix("$").astype(float)
    df["Low"] = df["Low"].str.removeprefix("$").astype(float)

    assert df["High"].dtype == float
    assert df["Low"].dtype == float
    assert (df["High"] >= df["Low"]).all(), "High >= Low should be true for all rows"


def test_price_change_column(df):
    df["High"] = df["High"].str.removeprefix("$").astype(float)
    df["Low"] = df["Low"].str.removeprefix("$").astype(float)
    df["Price Change"] = df["High"] - df["Low"]

    assert "Price Change" in df.columns
    assert (df["Price Change"] >= 0).all()


@pytest.mark.parametrize("sort_fn", [bubble_sort, insertion_sort, merge_sort, quick_sort])
def test_sort_functions_basic(sort_fn):
    # making sure sorting functions correctly sort a small sample
    arr = np.array([5, 3, 1, 4, 2], dtype=float)
    sorted_arr = sort_fn(arr.copy())

    assert sorted_arr == pytest.approx(sorted(arr)), f"{sort_fn.__name__} failed"


@pytest.mark.parametrize("sort_fn", [bubble_sort, insertion_sort, merge_sort, quick_sort])
def test_sort_empty_array(sort_fn):
    arr = np.array([], dtype=float)
    sorted_arr = sort_fn(arr.copy())
    assert len(sorted_arr) == 0


@pytest.mark.parametrize("sort_fn", [bubble_sort, insertion_sort, merge_sort, quick_sort])
def test_sort_single_element(sort_fn):
    arr = np.array([42.0], dtype=float)
    sorted_arr = sort_fn(arr.copy())
    assert sorted_arr == pytest.approx([42.0])


def test_split_array():
    arr = np.arange(10)
    left, right = split_array(arr)
    assert len(left) + len(right) == len(arr)

@pytest.mark.parametrize("algorithm", ["bubble_sort", "insertion_sort", "merge_sort", "quick_sort"])
def test_timing_function(algorithm):
    sample_arr = np.array([3.0, 1.0, 2.0])
    t = run_sorting_algorithm(algorithm, sample_arr)

    assert isinstance(t, float)
    assert t >= 0.0


def test_timing_sorted_builtin():
    sample_arr = np.array([3.0, 1.0, 2.0])
    t = run_sorting_algorithm("sorted", sample_arr)
    assert isinstance(t, float)