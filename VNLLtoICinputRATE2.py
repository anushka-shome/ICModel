# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:13:04 2015

@author: Alex
"""

def VNLLtoICinputRATE2(modfreq):     
    import numpy as np;

    modfreq= np.array(modfreq);
    a =       201.6;
    b =   -0.001057;
    c =      -153.3;
    d =   -0.009158;
       
    VNLLsprate = a*np.exp(b*modfreq) + c*np.exp(d*modfreq);

    return VNLLsprate 

