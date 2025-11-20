import pandas as pd
import matplotlib
matplotlib.use("Agg") # so the graphs don't open during tests (it failed once for some other code doing that)
import matplotlib.pyplot as plt
import pytest

@pytest.fixture
def us_df():
    # loading eleciton dataset once for all tests and making sure it can be read correctly
    return pd.read_csv("datasets/us_election_dataset.csv", sep=";")

def test_dataframe_loads(us_df):
    # making sure the dataframe loads and has the expected columns
    assert not us_df.empty, "dataframe should not be empty"
    expected_cols = {"candidate", "fraction_votes"}
    assert expected_cols.issubset(us_df.columns), "missing required columns"

def test_fraction_votes_range(us_df):
    # check fraction is valid
    assert us_df["fraction_votes"].between(0,1).all(), \
         "fraction votes should be between 0 and 1"
    
