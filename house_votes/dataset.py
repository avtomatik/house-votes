#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 00:07:27 2025

@author: alexandermikhailov
"""

from pathlib import Path

import pandas as pd

from .config import RAW_DATA_PATH
from .constants import ENGLISH_COLUMNS, PARTY_MAPPING, VOTE_MAPPING


def load_raw_data(file_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(file_path, sep='\t', index_col=0, encoding='cp1251')
    df.index.name = 'id'
    return df


def map_votes(df: pd.DataFrame) -> pd.DataFrame:
    vote_cols = df.columns[:-1]
    class_col = df.columns[-1]
    df[vote_cols] = df[vote_cols].map(VOTE_MAPPING.get)
    df[class_col] = df[class_col].map(PARTY_MAPPING)
    return df


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns=dict(zip(df.columns, ENGLISH_COLUMNS)))


def make_dataset() -> pd.DataFrame:
    return load_raw_data().pipe(map_votes).pipe(rename_columns)
