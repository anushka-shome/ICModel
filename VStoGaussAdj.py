# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:31:42 2015

@author: Alex
"""
import numpy as np

def VStoGaussAdj(VS):
    a1 =        2418;  
    b1 =       2.112;  
    c1 =      0.4489; 
    a2 =      0.7923;  
    b2 =        1.03;
    c2 =       0.589;
    VS = np.array(VS);
    gaussVSadj = a1*np.exp(-((VS-b1)/c1)**2) + a2*np.exp(-((VS-b2)/c2)**2); 
    return gaussVSadj
   