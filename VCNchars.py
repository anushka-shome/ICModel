# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:11:45 2015

@author: Alex
"""

def VCNchars(freq):
    import numpy as np; 
    from VCNtoVSgen2 import VCNtoVSgen2;
    from VCNspcyclegen2 import VCNspcyclegen2;
    from VStoGaussAdj import VStoGaussAdj;
    
    vs = VCNtoVSgen2(freq);    
    [spcycle,rates] = VCNspcyclegen2(freq);
    gaussvs = VStoGaussAdj(vs);
    CV = .5;
    cyclesd = spcycle*CV;

    return vs, rates, spcycle, gaussvs, cyclesd 
    
