# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:53:36 2015

@author: Alex
"""

def DNLLtoICspcycles(modfreq):
    import numpy as np;
    modfreq = np.array(modfreq);
    
    a = 5.372; 
    b = -0.01034; 
    c = 1.38; 
    d = -0.001488;
    
    spcycleDNLL = a*np.exp(b*modfreq) + c*np.exp(d*modfreq);
    
    return spcycleDNLL
    

