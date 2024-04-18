# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:30:29 2015

@author: Alex
"""

def LSO_ICinputVS(freq):
    import numpy as np;
    
    a = -1.525e-015;
    b =       17.56;
    c =      0.6912;

    vs = a*(np.log(freq))**b+c;
    return vs
    
    