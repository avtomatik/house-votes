#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 00:07:27 2025

@author: alexandermikhailov
"""

from pathlib import Path

import pandas as pd

# =============================================================================
# https://www.kaggle.com/datasets/devvret/congressional-voting-records?select=house-votes-84.names # noqa: E501
# =============================================================================
FILE_NAME = 'vote.txt'

kwargs = {
    'filepath_or_buffer': (
        Path(__file__).parent.parent
        .joinpath('data')
        .joinpath('raw')
        .joinpath(FILE_NAME)
    ),
    'sep': '\t',
    # 'names': ,
    'index_col': 0,
    'encoding': 'cp1251',
}

df = pd.read_csv(**kwargs)
df.replace(['да', 'нет'], [1, 0], inplace=True)
print(df.describe())
df.info()
