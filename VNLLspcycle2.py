# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:02:58 2015

@author: Alex
"""

def VNLLspcycle2(modfreq):  
    import numpy as np;


    modfreq = np.array(modfreq);
    a =       40.07;
    b =     -0.7726;
    c =    -0.07389;

    VNLLspcycle = a*modfreq**b+c;
    
    return VNLLspcycle
    
