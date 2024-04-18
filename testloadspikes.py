# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:24:32 2015

@author: labadmin
"""

def loadspikes():
    from neuron import *
    from nrn import *
    import numpy as np
    import pdb
    numE = 1
    numI = 1
    for jj in range(numE):
        if len(rpE)>0:
            numss = len(rpE[jj])
            for ii in range(numss):
                h.nclistA.o(jj).event((rpE[jj].x[ii]+200))
                h.nclistB.o(jj).event((rpE[jj].x[ii]+200))
    for nn in range(numI):
        if len(rpI)>0:
            numsI = len(rpI[jj])
            for mm in range(numsI):
                h.nclistC.o(nn).event((rpI[nn].x[mm]+200))
                h.nclistD.o(nn).event((rpI[nn].x[mm]+200))
