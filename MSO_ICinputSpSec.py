# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:19:02 2015

@author: Alex
"""

def MSO_ICinputSpSec(modfreq):
    import numpy as np;
    
    modfreq = np.array(modfreq);
    a =       99.16;
    b =   -0.006737;
    c =      -98.12;
    d =   -0.006713;
    
    spcycleMSO = a*np.exp(b*modfreq) + c*np.exp(d*modfreq);
    
    return(spcycleMSO)