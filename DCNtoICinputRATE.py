# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:20:51 2015

@author: Alex
"""

def DCNtoICinputRATE(modfreq,ap,bp,cp):
    import numpy as np;
    #a =      -308.9; 
    #b =    -0.01862;  
    #c =       359.8; 
    a = ap
    b = bp
    c = cp
    modfreq = np.array(modfreq)
    modRATE = a*modfreq**b+c
    return modRATE
