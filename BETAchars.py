# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:48:36 2015

@author: B.S.Coventry
Vars: freq - sgi
      A1, B1: Beta dist. parameters for rate
      A2, B2: Beta dist. parameters for VS
"""

def BETAchars(freq,A1,B1,A2,B2,ratevar,vsvar):
    from scipy.stats import beta
    import numpy as np
    from VStoGaussAdj import VStoGaussAdj    
    import pdb
    sgi = np.array([8.,16.,32.,64.,128.,256.,512.,1024.,2048])
    sginorm = sgi/np.max(sgi)
    rates1 = beta.pdf(sginorm,A1,B1)
    rates1 = rates1/np.max(rates1)
    rates = rates1*ratevar
    vs1 = beta.pdf(sginorm,A2,B2)
    vs2 = vs1/np.max(vs1)
    #pdb.set_trace()
    vs = vsvar*vs2
    spcycle = rates/sgi;
    for value in spcycle:
        if value <= 0:
            value = 0.0001;
    spcycle = np.array(spcycle);
    gaussvs = VStoGaussAdj(vs);
    CV = 0.5;
    cyclesd = CV*spcycle;
    return vs, rates, spcycle, gaussvs, cyclesd