# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:04:01 2015

@author: Alex
"""

def MSO_ICinputVS(modfreq):
    import numpy as np;
    
    modfreq = np.array(modfreq);
    a =       58.71;
    b =    0.008962;
    c =       4.438;

    gaussVSMSO = (modfreq+a)/(1+np.exp(b*modfreq+c));
    return gaussVSMSO
