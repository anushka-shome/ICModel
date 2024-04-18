# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:28:52 2015

@author: Alex
"""

def LSO_ICinputRATE(freq):
    import numpy as np;
    rates = np.ones((1,len(freq)))*25;
    return rates