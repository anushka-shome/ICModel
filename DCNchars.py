# -*- coding: utf-8 -*-
"""
Created on Tue May 26 11:17:52 2015

@author: Alex
"""

def DCNchars(freq,quota,ap,bp,cp):
    import numpy as np
    import random as rnd
    import matplotlib.pyplot as plt
    
    from DCNtoICinputVS import DCNtoICinputVS
    from DCNtoICinputRATE import DCNtoICinputRATE
    from VStoGaussAdj import VStoGaussAdj    

    freq = np.array(freq);
    vs = DCNtoICinputVS(freq);
    rates=DCNtoICinputRATE(freq,ap,bp,cp);
    rates = np.array(rates);
    spcycle = rates/freq;
    for value in spcycle:
        if value <= 0:
            value = 0.0001;
    spcycle = np.array(spcycle);
    gaussvs = VStoGaussAdj(vs);
    CV = 0.5;
    cyclesd = CV*spcycle;
    return vs, rates, spcycle, gaussvs, cyclesd
    
#[vs,rates,spcycle, gaussvs,cyclesd] = DCNchars([8,16,32,64,128,256,512,1024],quota);
#print vs
#print rates
#print spcycle
#print gaussvs
#print cyclesd
