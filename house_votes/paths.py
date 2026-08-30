from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
##############################################################################=
# https://www.kaggle.com/datasets/devvret/congressional-voting-records?select=house-votes-84.names # noqa: E501
##############################################################################=
FILE_NAME = "vote.txt"
DATA_RAW_PATH = DATA_DIR / "raw" / FILE_NAME
DATA_PROCESSED_PATH = DATA_DIR / "processed" / "house_votes.parquet"
