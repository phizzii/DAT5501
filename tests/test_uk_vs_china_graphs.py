import pandas as pd
import numpy as np
import pytest

# creating dataframe for le tests
@pytest.fixture
def deaths_df():
    return pd.DataFrame({
        "location_name": ["United Kingdom", "China", "United Kingdom", "China"],
        "year": [2011, 2011, 2019, 2019],
        "cause_name": ["Neurological disorders", "Mental disorders",
                       "Neurological disorders", "Mental disorders"],
        "val": [1000, 2000, 1500, 3000],
        "measure_id": [1,1,1,1],
        "location_id": [1,1,1,1],
        "sex_id": [1,1,1,1],
        "age_id": [1,1,1,1],
        "cause_id": [1,1,1,1],
        "metric_id": [1,1,1,1],
        "upper": [0,0,0,0],
        "lower": [0,0,0,0],
    })


@pytest.fixture
def working_hours_df():
    return pd.DataFrame({
        "Entity": ["United Kingdom", "China", "China", "United Kingdom"],
        "Year": [2010, 2011, 2019, 2017],
        "Working hours per worker": [1500, 2000, 1800, 1600]
    })


def test_drop_unnecessary_columns(deaths_df):
    result = deaths_df.drop(columns=[
        'measure_id','location_id','sex_id','age_id','cause_id','metric_id','upper','lower'
    ])

    assert "measure_id" not in result.columns
    assert "val" in result.columns   # ensure essential data still present
    assert len(result) == len(deaths_df)


def test_filter_years_2011_2019(deaths_df):
    df = deaths_df.drop(columns=['measure_id','location_id','sex_id','age_id',
                                 'cause_id','metric_id','upper','lower'])
    mask = df["year"] >= 2011
    filtered = df[mask]

    assert filtered["year"].min() >= 2011
    assert len(filtered) == len(df)    # none were < 2011 in fixture


def test_filter_countries_working_hours(working_hours_df):
    mask = working_hours_df["Entity"].isin(["United Kingdom", "China"])
    filtered = working_hours_df[mask]

    assert set(filtered["Entity"].unique()) <= {"United Kingdom", "China"}
    assert len(filtered) == len(working_hours_df)


def test_filter_working_hours_years(working_hours_df):
    df2 = working_hours_df[working_hours_df["Entity"].isin(["United Kingdom", "China"])]
    mask = df2["Year"] >= 2011
    filtered = df2[mask]

    assert filtered["Year"].min() >= 2011
    assert len(filtered) == 3  # based on fixture


def test_neuro_and_mental_filters(deaths_df):
    df_clean = deaths_df.drop(columns=[
        'measure_id','location_id','sex_id','age_id','cause_id','metric_id','upper','lower'
    ])
    mask_years = df_clean["year"] >= 2011
    df_years = df_clean[mask_years]

    neuro = df_years[df_years["cause_name"] == "Neurological disorders"]
    mental = df_years[df_years["cause_name"] == "Mental disorders"]

    assert set(neuro["cause_name"].unique()) == {"Neurological disorders"}
    assert set(mental["cause_name"].unique()) == {"Mental disorders"}
    assert len(neuro) == 2   # based on fixture
    assert len(mental) == 2
