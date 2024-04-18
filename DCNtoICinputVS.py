# -*- coding: utf-8 -*-
"""
Created on Tue May 26 11:33:37 2015

@author: Alex
"""

def DCNtoICinputVS(modfreq):
    import numpy as np
    import random as rnd
    import matplotlib.pyplot as plt
    a1 =     0.06353;
    b1 =       882.4;
    c1 =       854.9;
    a2 =      0.4923;
    b2 =       187.7;
    c2 =       381.7;
    modfreq = np.array(modfreq);
    gaussVS = a1 * np.exp(-((modfreq-b1)/c1)**2)+a2*np.exp(-((modfreq-b2)/c2)**2);
    return(gaussVS)

