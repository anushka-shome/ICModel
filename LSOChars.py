# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:07:57 2015

@author: Alex
"""

def LSOChars(freq):
    import numpy as np;
    
    from LSO_ICinputVS import LSO_ICinputVS;
    from LSO_ICinputRATE import LSO_ICinputRATE;
    from LSOspcycleTEST import LSOspcycleTEST;
    from LSOspcycle import LSOspcycle;
    from VStoGaussAdj import VStoGaussAdj;

    '''
    global LSOmin; 
    global LSOpeak;
    global LSOmax;
    global shape;
    '''
    
    LSOmin = 1
    LSOpeak = 2
    LSOmax = 2
    shape = 2
    
    freq = np.array(freq);    
    vs = LSO_ICinputVS(freq);
    
    counter = 0;
    for value in vs:
        if value < 0:
            vs[counter] = 0;
        counter +=1;
    
    rates = LSO_ICinputRATE(freq);
    rates = rates[0];
    
    if shape ==1:
        spcycle = LSOspcycleTEST(freq, LSOmin, LSOpeak, LSOmax);
    else:
        spcycle = LSOspcycle(freq);
    counter = 0;
    for value in spcycle:
        if value <= 0:
            spcycle[counter] = 0.0001;
        counter += 1;
    gaussvs = VStoGaussAdj(vs);
    CV = 0.5;
    cyclesd = CV*spcycle;
    
    return vs, rates, spcycle, gaussvs, cyclesd

