# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:24:54 2015

@author: Alex
"""

def DNLLchars(freq,quota):
    import numpy as np

    from DNLLtoICinputVS import DNLLtoICinputVS
    from DNLLtoICinputRATE import DNLLtoICinputRATE
    from DNLLtoICspcycles import DNLLtoICspcycles
    from VStoGaussAdj import VStoGaussAdj

    #global quota
    
    freq = np.array(freq);
    vs = DNLLtoICinputVS(freq);
    rates = DNLLtoICinputRATE(freq); # delete
    #rates = np.array(rates);
    #vs = np.array([0.8, 0.8, 0.8, 0.8, 0.8, 0.5, 0.2, 0]) #why is this overwriting vs?
    rates = rates[0]; # if this is intended to extract the scalar value, it's not working
    # Delete last line, looks like we need an array for spcycle anyways
   
    if quota == 1: #Linear Modeling
        spcycle = rates/freq;
    elif quota ==2: #Exponential Modeling
        spcycle = DNLLtoICspcycles(freq);
    else: 
        spcycle = rates/freq;   
    
    
    counter = 0;
    for value in spcycle:
        if value <=0:
            spcycle[counter] = 0.0001;
        counter +=1;
        
    gaussvs = VStoGaussAdj(vs);
    CV = 0.5;
    cyclesd = CV*spcycle;
        
    return vs, rates, spcycle, gaussvs, cyclesd
 
