# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 14:56:16 2015

@author: Brandon S. Coventry         CAP Lab Purdue University
Purpose: Analysis and Plotting functions for the IC model
"""
def ICstats(spikevec,numtrials,sgi):
    import numpy as np
    import pdb
    meanvec = np.zeros([len(sgi)])
    sdvec = np.zeros([len(sgi)])
    #pdb.set_trace()
    for ii in range(len(sgi)):
        #pdb.set_trace()
        curdat = spikevec[ii]
        spklen = np.zeros([numtrials])
        for jj in range(numtrials):
            spklen[jj] = np.asarray(float(len(curdat[jj])))
        meanvec[ii] = np.mean(spklen)
        sdvec[ii] = np.std(spklen)
    return [meanvec,sdvec]

def FTCgen(meanspikes,sdspikes,sgi):
    import numpy as np
    import matplotlib.pyplot as plt
    fig = plt.show()
    ax = plt.gca()    
    ax.errorbar(sgi,meanspikes,yerr=sdspikes)
    ax.set_xscale('log')
    plt.show()
    
def fitfunc(meanspikes,sdspikes,sgi,expmean,expsd):
    import numpy as np
    RMSEterm = np.sqrt(np.mean(np.power((expmean-meanspikes),2)))
    rr = np.corrcoef(expmean,meanspikes)
    newerrterm = np.power((1.0 + rr[0,1]),-3)
    ee = RMSEterm*newerrterm
    MSE = 1-np.power((1+ee),-1)
    return MSE
def fitfuncm(meanspikes,sdspikes,sgi,expmean,expsd):
    import numpy as np
    lenterm = float(np.size(expmean))
    err = meanspikes-expmean
    sqerr = np.power(err,2)
    sumsqerr = np.sum(sqerr)
    MSErr = float(sumsqerr)/float(lenterm)
    return MSErr
    