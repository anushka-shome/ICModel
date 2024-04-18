# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:42:10 2015

@author: Alex
"""

def LSOspcycle(freq):
    import numpy as np;
    
    a =       32.89;
    b =     -0.1411;
    c =       5.632;    
    d =    -0.01539;

    freq = np.array(freq);
    spcycle = a*np.exp(b*freq) + c*np.exp(d*freq);
    
    return spcycle
