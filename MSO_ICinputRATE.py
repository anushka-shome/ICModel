# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:11:01 2015

@author: Alex
"""

def MSO_ICinputRATE(modfreq,ap,bp,cp,dp):
    import numpy as np;
    
    modfreq = np.array(modfreq);

    #a = 119.6;
    #b = -0.006725;
    #c = -120.5;
    #d = -0.01828;
    a = ap
    b = bp
    c = cp
    d = dp
    modRATE = a*np.exp(b*modfreq) + c*np.exp(d*modfreq) + 6;
    
    return(modRATE)
    
