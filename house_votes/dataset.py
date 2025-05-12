#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 00:07:27 2025

@author: alexandermikhailov
"""

import pandas as pd
from config import DATA_DIR, FILE_NAME

kwargs = {
    'filepath_or_buffer': DATA_DIR.joinpath('raw').joinpath(FILE_NAME),
    'sep': '\t',
    'index_col': 0,
    'encoding': 'cp1251',
}

df = pd.read_csv(**kwargs)
df.replace(['да', 'нет'], [1, 0], inplace=True)
print(df.describe())
df.info()
