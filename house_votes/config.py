#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 12 14:01:05 2025

@author: alexandermikhailov
"""

# =============================================================================
# https://www.kaggle.com/datasets/devvret/congressional-voting-records?select=house-votes-84.names # noqa: E501
# =============================================================================
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / 'data'

FILE_NAME = 'vote.txt'
