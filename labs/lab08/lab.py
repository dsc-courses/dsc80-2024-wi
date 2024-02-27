# lab.py


import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels.api as sm
from pathlib import Path
from sklearn.preprocessing import Binarizer, QuantileTransformer, FunctionTransformer

import warnings
warnings.filterwarnings('ignore')


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def best_transformation():
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def create_ordinal(df):
    ...


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def create_one_hot(df):
    ...


def create_proportions(df):
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def create_quadratics(df):
    ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def comparing_performance():
    # create a model per variable => (variable, R^2, RMSE) table
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


class TransformDiamonds(object):
    
    def __init__(self, diamonds):
        self.data = diamonds
        
    # Question 6.1
    def transform_carat(self, data):
        ...
    
    # Question 6.2
    def transform_to_quantile(self, data):
        ...
    
    # Question 6.3
    def transform_to_depth_pct(self, data):
        ...
