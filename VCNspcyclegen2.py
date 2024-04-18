# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:34:47 2015

@author: Alex
"""

def VCNspcyclegen2(freq):
    import numpy as np;
    
    #freq = np.array(freq);
    spsec = np.ones(len(freq))*128
    spsec[0] = 96
    spsec[1] = 96
    spsec[2] = 96
    spsec[3] = 128
    spsec[4] = 128
    spsec[5] = 192
    spsec[6] = 224
    spsec[7] = 224
    #spsec = np.array(spsec);
    #spsec = spsec[0]
    spcycle = spsec/freq
    
    return spcycle, spsec
    
