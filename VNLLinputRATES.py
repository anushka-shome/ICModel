# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:11:24 2015

@author: Alex
"""
def VNLLinputRATES(peak,freq):
    import numpy as np;
    freq = np.array(freq);
    ratelist = np.absolute(np.log2(float(peak)/freq));
    ratelist = np.array(ratelist);    
    rats = 2**ratelist;
    rats = np.array(rats);
    rates = 1/rats;
    scale = 100
    rates = scale*rates
#    try:
#        scale = float(scale);
#    except ValueError:
#        scale = 100;
#        rates = scale*rates;
#    else:
#        rates = scale*rates;
    return rates
        
