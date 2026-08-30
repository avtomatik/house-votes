from house_votes.constants import COLUMNS
from house_votes.dataset import make_dataset


def test_vote_encoding():
    df = make_dataset()
    vote_columns = COLUMNS[:-1]
    assert all(df[column].is_in([-1, 0, 1]).all() for column in vote_columns)
