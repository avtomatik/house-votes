import argparse
from pathlib import Path

from house_votes.dataset import make_dataset, save_dataset
from house_votes.paths import DATA_PROCESSED_PATH, DATA_RAW_PATH


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build the canonical House Votes dataset."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DATA_RAW_PATH,
        help=f"Raw vote file (default: {DATA_RAW_PATH})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DATA_PROCESSED_PATH,
        help=f"Processed Parquet file (default: {DATA_PROCESSED_PATH})",
    )
    args = parser.parse_args()
    df = make_dataset(args.input)
    save_dataset(df, args.output)
    print(f"Processed {df.height:,} observations.")
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
