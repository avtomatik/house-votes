from pathlib import Path

import polars as pl

from house_votes.constants import (COLUMNS, PARTY_ENCODING, TARGET_COLUMN,
                                   VOTE_ENCODING)
from house_votes.paths import DATA_PROCESSED_PATH, DATA_RAW_PATH


def load_raw_data(
    file_path: Path = DATA_RAW_PATH,
) -> pl.DataFrame:
    return pl.read_csv(
        file_path,
        separator="\t",
        encoding="windows-1251",
        has_header=True,
        new_columns=["id", *COLUMNS],
    )


def map_votes(df: pl.DataFrame) -> pl.DataFrame:
    vote_columns = COLUMNS[:-1]
    return df.with_columns(
        pl.col(vote_columns).replace(VOTE_ENCODING).cast(pl.Int8),
        pl.col(TARGET_COLUMN).replace(PARTY_ENCODING).cast(pl.Int8),
    )


def make_dataset(file_path: Path = DATA_RAW_PATH) -> pl.DataFrame:
    return map_votes(load_raw_data(file_path))


def save_dataset(
    df: pl.DataFrame, file_path: Path = DATA_PROCESSED_PATH
) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.write_parquet(file_path)


def load_dataset(file_path: Path = DATA_PROCESSED_PATH) -> pl.DataFrame:
    return pl.read_parquet(file_path)
