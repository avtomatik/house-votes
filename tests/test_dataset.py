import polars as pl

from house_votes.constants import COLUMNS
from house_votes.dataset import make_dataset


def test_make_dataset():
    df = make_dataset()
    assert df.shape == (150, 18)
    assert df.columns == ["id", *COLUMNS]
    assert df["id"].dtype == pl.Int64
    assert df["Party"].is_in([0, 1]).all()
