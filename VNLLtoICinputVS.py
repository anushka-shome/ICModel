# -*- coding: utf-8 -*-
"""
Created on Fri May 29 12:41:05 2015

@author: Alex
"""

def VNLLtoICinputVS(modfreq):
    import numpy as np;
    modfreq = np.array(modfreq);
    
    a =       66.93;
    b = -1.032e+005;
    c =     -0.8961;
    d =      -18.06;
    e =      -65.95;

    gaussVS = a*np.exp(modfreq/b) + c*np.exp(modfreq/d) + e;
    return gaussVS
