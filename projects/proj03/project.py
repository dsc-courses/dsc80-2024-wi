# project.py


import pandas as pd
import numpy as np
from pathlib import Path
import re
import requests
import time


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def get_book(url):
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def tokenize(book_string):
    ...


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


class UniformLM(object):


    def __init__(self, tokens):

        self.mdl = self.train(tokens)
        
    def train(self, tokens):
        ...
    
    def probability(self, words):
        ...
        
    def sample(self, M):
        ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


class UnigramLM(object):
    
    def __init__(self, tokens):

        self.mdl = self.train(tokens)
    
    def train(self, tokens):
        ...
    
    def probability(self, words):
        ...
        
    def sample(self, M):
        ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


class NGramLM(object):
    
    def __init__(self, N, tokens):
        # You don't need to edit the constructor,
        # but you should understand how it works!
        
        self.N = N

        ngrams = self.create_ngrams(tokens)

        self.ngrams = ngrams
        self.mdl = self.train(ngrams)

        if N < 2:
            raise Exception('N must be greater than 1')
        elif N == 2:
            self.prev_mdl = UnigramLM(tokens)
        else:
            self.prev_mdl = NGramLM(N-1, tokens)

    def create_ngrams(self, tokens):
        ...
        
    def train(self, ngrams):
        # N-Gram counts C(w_1, ..., w_n)
        ...
        
        # (N-1)-Gram counts C(w_1, ..., w_(n-1))
        ...

        # Create the conditional probabilities
        ...
        
        # Put it all together
        ...
    
    def probability(self, words):
        ...
    

    def sample(self, M):
        # Use a helper function to generate sample tokens of length `length`
        ...
        
        # Transform the tokens to strings
        ...
