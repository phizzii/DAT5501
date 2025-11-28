import os
import pandas as pd
import pytest
import sys
import matplotlib.pyplot as plt

# allow importing from parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from small_projects import graphs_barmet_education

@pytest.fixture
def sample_csvs(tmp_path):
    # create sample CSV files to test with."""
    df = pd.DataFrame({
        "year": [2009, 2010, 2011, 2012],
        "average point score": [650, 700, 720, 740],
        "16-18 entered for L3": [200, 220, 250, 270],
        "% achieving at least 2 L3 qualifications (per candidate)": [70, 72, 74, 76],
    })
    path1 = tmp_path / "csvGCSE.csv"
    path2 = tmp_path / "gcse_results.csv"
    df.to_csv(path1, index=False)
    df.to_csv(path2, index=False)
    return str(path1), str(path2)


def test_main_returns_expected_stats(sample_csvs):
    # make sure mean/median and dataset stats are computed correctly."""
    csv1, csv2 = sample_csvs
    result = graphs_barmet_education.main(csv1, csv2, show_plots=False)

    assert isinstance(result, dict)
    assert "mean" in result and "median" in result
    assert round(result["mean"], 2) == pytest.approx(702.5, 0.1)
    assert round(result["median"], 2) == pytest.approx(710, 0.1)
    assert result["num_rows"] == 4


def test_main_handles_missing_file(tmp_path):
    # check that missing file raises FileNotFoundError
    fake_path = tmp_path / "does_not_exist.csv"
    with pytest.raises(FileNotFoundError):
        graphs_barmet_education.main(str(fake_path), str(fake_path), show_plots=False)


def test_main_creates_plots(sample_csvs):
    # make sure main function generates Matplotlib figures (without showing them)."""
    csv1, csv2 = sample_csvs

    # clear any existing figures
    plt.close("all")

    # run main with show_plots=False
    graphs_barmet_education.main(csv1, csv2, show_plots=False)

    # check that at least one figure was created
    fig_nums = plt.get_fignums()
    assert len(fig_nums) >= 1, "No matplotlib figures were created by main()"

    # optional: check figure count matches expected number of plots (3 total)
    assert len(fig_nums) == 3, f"Expected 3 figures, got {len(fig_nums)}"