"""
Test goes here
"""

from mylib.lib import (
    load_dataset,
    get_mean,
    get_median,
    get_std,
    get_min,
    get_max,
    get_quantile,
)


data = "https://raw.githubusercontent.com/fivethirtyeight/data/master/murder_2016/murder_2015_final.csv"


# test the dataset can be read correctly:
def test_load_dataset():
    test_df = load_dataset(data)
    test_df.describe()
    assert test_df is not None


# test all of the statistical descriptive functions:
def test_mean():
    assert round(get_mean(load_dataset(data), "2014_murders"), 6) == 65.746988


def test_median():
    assert round(get_median(load_dataset(data), "2014_murders"), 6) == 32.000000


def test_std():
    assert round(get_std(load_dataset(data), "2014_murders"), 6) == 79.011244


def test_min():
    assert round(get_min(load_dataset(data), "2014_murders"), 6) == 0.000000


def test_max():
    assert round(get_max(load_dataset(data), "2014_murders"), 6) == 411.000000


def test_quantile():
    assert round(get_quantile(load_dataset(data), "2014_murders", 0.25), 6) == 19.500000
    assert round(get_quantile(load_dataset(data), "2014_murders", 0.5), 6) == 32.000000
    assert round(get_quantile(load_dataset(data), "2014_murders", 0.75), 6) == 82.000000


if __name__ == "__main__":
    test_load_dataset()
    test_mean()
    test_median()
    test_std()
    test_min()
    test_max()
    test_quantile()
