# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:29:41 2015

@author: Alex
"""

def DNLLtoICinputVS(modfreq):
    import numpy as np;
    
    modfreq = np.array(modfreq);
    m = -.0007705;
    b = 0.7587;
    
    gaussVS = m*modfreq + b; # linear model defining relationship between mod freq and vs
    return gaussVS
  