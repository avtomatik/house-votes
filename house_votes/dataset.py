#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 00:07:27 2025

@author: alexandermikhailov
"""

import pandas as pd

from .config import DATA_DIR, FILE_NAME
from .constants import ENGLISH_COLUMNS, PARTY_MAPPING, VOTE_MAPPING

file_path = DATA_DIR / 'raw' / FILE_NAME

df = pd.read_csv(file_path, sep='\t', index_col=0, encoding='cp1251')

vote_cols = df.columns[:-1]
class_col = df.columns[-1]
df[vote_cols] = df[vote_cols].map(VOTE_MAPPING.get)
df[class_col] = df[class_col].map(PARTY_MAPPING)

df.index.name = 'id'
df.columns = ENGLISH_COLUMNS

print(df.head())
df.info()
print(df.describe())
