# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:41:06 2015

@author: Alex
"""

def VNLLchars(freq):
    import numpy as np   
    from VNLLtoICinputVS import VNLLtoICinputVS;
    from VNLLinputRATES import VNLLinputRATES;
    from VNLLtoICinputRATE2 import VNLLtoICinputRATE2;
    from VNLLspcycle2 import VNLLspcycle2;
    from VStoGaussAdj import VStoGaussAdj;
     
    #global shape2;
    global INpeak;
    shape2=0
    freq = np.array(freq);
    vs = VNLLtoICinputVS(freq);

    if shape2 == 1:
        rates = VNLLinputRATES(INpeak,freq);
        rates = np.array(rates);
        spcycle = rates/freq;
    else:
        rates  = VNLLtoICinputRATE2(freq);
        spcycle = VNLLspcycle2(freq);
    
    for value in spcycle:
        if value <=0:
            value = 0.0001;
            
    gaussvs = VStoGaussAdj(vs);

    spcycle = np.array(spcycle);
    
    CV = .5;
    cyclesd = CV*spcycle;

    return vs, rates, spcycle, gaussvs, cyclesd




