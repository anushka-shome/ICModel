# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:18:31 2015

@author: Alex
"""

def MSOchars(freq,ap,bp,cp,dp):
    import numpy as np;

    from MSO_ICinputVS import MSO_ICinputVS;
    from MSO_ICinputRATE import MSO_ICinputRATE;
    from MSO_ICinputSpSec import MSO_ICinputSpSec;
    from VStoGaussAdj import VStoGaussAdj;
    
    freq = np.array(freq);
    #print freq
    vs = MSO_ICinputVS(freq);
    rates = MSO_ICinputRATE(freq,ap,bp,cp,dp);
    spcycle = MSO_ICinputSpSec(freq);
    gaussvs = VStoGaussAdj(vs);
    CV = 0.5;    
    counter = 0;
    for value in spcycle:
        counter += 1;
        if value <= 0:
            spcycle[counter - 1] = 0.0001;
    spcycle = np.array(spcycle);
    cyclesd = CV*spcycle;
    return vs, rates, spcycle, gaussvs, cyclesd
    
