# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:40:21 2015

@author: Alex
"""

def inputProb(driven,prob):
    import numpy as np
    from numpy import random    
    
    
    n = len(driven);
    okind = np.random.uniform(0,1,(1,n));
    okind = okind[0];
    
    newdriven = [];
    for i in range(0,n):
        if okind[i]<=prob:
            newdriven.append(driven[i]);
            
#    newdriven = driven[okind <= prob];
    
    return newdriven
    

