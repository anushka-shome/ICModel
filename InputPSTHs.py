# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 14:37:39 2015

@author: Brandon S Coventry       Purdue CAP Lab
Purpose: Model input PSTH files
Revision History: None
"""
def DNLLpsth(latency,rate,maxrate):
    import numpy as np
    import random as rnd
    import matplotlib.pyplot as plt
    bindivision = 1.          #Bin size in ms
    n = 30.       #Number of stimulus repitions
    histdiv = n*bindivision    #Division factor
    tlength = 200.              #Time in ms
    tvec = np.arange(0,tlength,bindivision)
    scaleratio = rate/maxrate                    #Need to scale psthbin counts
    spkcounts = np.zeros(len(tvec))          #Create initial spike count vector
    latentcells = round(latency/bindivision)     #Create latency in bins
    if latentcells > 0:
        spkcounts[range(1,int(latentcells))] = 0
        begincell = latentcells + 1
    a = 0*histdiv
    b = 5*histdiv                                #Make sure to divide by binsize for accurate binning
    spkcounts[begincell] = rnd.uniform(a,b)        #Random initial onset
    begincell = begincell + 1
    a = 37*histdiv                                #Random huge onset (Kelly et al, 1998)
    b = 55*histdiv
    spkcounts[begincell] = rnd.uniform(a,b)
    begincell=begincell+1
    expdecaylen = 5                             #Length of exp. decay section following onset
    a = 10*histdiv
    b = 23*histdiv
    expdecayvec = np.arange(begincell,begincell+expdecaylen)
    for ii in range(len(expdecayvec)):
        spkcounts[expdecayvec[ii]] = rnd.uniform(a,b)
    begincell=begincell+expdecaylen+1
    susresptime = np.arange(begincell,len(tvec))    #Sustained response area
    a = 1*histdiv
    b = 12*histdiv
    for jj in range(len(susresptime)):
        spkcounts[susresptime[jj]] = rnd.uniform(a,b)
    
    spkcounts = spkcounts*scaleratio
    spks = spkcounts*scaleratio
    psth = spks
    return psth,tvec
    
#def Gauss8(x,a1,a2,a3,a4,a5,a6,a7,a8,b1,b2,b3,b4,b5,b6,b7,b8,c1,c2,c3,c4,c5,c6,c7,c8):
    #import numpy as np
    #return a1*np.exp(-np.square((x-b1)/c1))+a2*np.exp(-np.square((x-b2)/c2))+a3*np.exp(-np.square((x-b3)/c3))+a4*np.exp(-np.square((x-b4)/c4))+a5*np.exp(-np.square((x-b5)/c5))+a6*np.exp(-np.square((x-b6)/c6))+a7*np.exp(-np.square((x-b7)/c7))+a8*np.exp(-np.square((x-b8)/c8))
#from pymodelfit import FunctionModel1DAuto
def Gauss(x,a1,b1,c1):
    #def f(self,x,a1,b1,c1): 
    import numpy as np        
    return float(a1)*np.exp(-np.square((x-float(b1))/float(c1)))
        
def PSTHgen(latency,rate,maxrate,a1,b1,a2,b2,a3,b3,a4,b4):
    import numpy as np
    import random as rnd
    import matplotlib.pyplot as plt
    bindivision = 1.          #Bin size in ms
    n = 30.       #Number of stimulus repitions
    histdiv = n*bindivision    #Division factor
    tlength = 200.              #Time in ms
    tvec = np.arange(0,tlength,bindivision)
    scaleratio = rate/maxrate                    #Need to scale psthbin counts
    spkcounts = np.zeros(len(tvec))          #Create initial spike count vector
    latentcells = round(latency/bindivision)     #Create latency in bins
    if latentcells > 0:
        spkcounts[range(1,int(latentcells))] = 0
        begincell = latentcells + 1
    #a1a = 0*histdiv
    a1a = a1*histdiv
    #b1a = 5*histdiv                                #Make sure to divide by binsize for accurate binning
    b1a = b1*histdiv    
    spkcounts[begincell] = rnd.uniform(a1a,b1a)        #Random initial onset
    begincell = begincell + 1
    a2a = a2*histdiv          #37*histdiv          #Random huge onset (Kelly et al, 1998)
    b2a = b2*histdiv          #55*histdiv
    spkcounts[begincell] = rnd.uniform(a2a,b2a)
    begincell=begincell+1
    expdecaylen = 5                             #Length of exp. decay section following onset
    a3a = a3*histdiv                            #10*histdiv
    b3a = b3*histdiv                            #23*histdiv
    expdecayvec = np.arange(begincell,begincell+expdecaylen)
    for ii in range(len(expdecayvec)):
        spkcounts[expdecayvec[ii]] = rnd.uniform(a3a,b3a)
    begincell=begincell+expdecaylen+1
    susresptime = np.arange(begincell,len(tvec))    #Sustained response area
    a4a = a4*histdiv                            #1*histdiv
    b4a = b4*histdiv                            #12*histdiv
    for jj in range(len(susresptime)):
        spkcounts[susresptime[jj]] = rnd.uniform(a4a,b4a)
    spkcounts = spkcounts*scaleratio
    spks = spkcounts*scaleratio
    psth = spks
    return psth,tvec    
def FTCcharsfreq(freq,cf,freqrange,Q10,maxrate):
    import numpy as np
    bandwidth = float(cf)/float(Q10)
    ftc = maxrate*np.exp(-(np.square(freqrange-float(cf)))/(2*np.square(bandwidth)))    #Tuning curves will approximately have this form
    #sgival = np.where(freqrange==freq)
    #rate = ftc[sgival]
    #Now, generate psth function to find rate at a particular freq
    import fit
    (xf,yf), params, err, chi = fit.fit(fit.gaus,freqrange,ftc)   #Matlab fitting toolbox
    from InputPSTHs import Gauss
    rate = Gauss(freq,params[0],params[1],params[2])
    return rate,ftc
def makeCDF(psth):
    import numpy as np          
    cdf = np.cumsum(psth)      #Hist approximates PDF Sum to find CDF
    cdf = cdf/np.max(cdf)      #Normalize
    return cdf
def InvTransform(frequency,cdf,spkrate):
    #Implement Inverse Transformation to draw spikes from unknown distribution
    #See http://en.wikipedia.org/wiki/Inverse_transform_sampling
    import numpy as np
    import random as rnd
    import scipy.signal as sps
    import pdb
    duration = 200.            #Durination of sound stimulus
    numcycles = float(frequency)*duration        #Basic periodicity equation
    numspikes = round(float(spkrate)*(duration/1000))    #Generate Spikes according to spkrate
    if numspikes < 0:
        numspikes = 0
    randseed = np.zeros(3000)                        #Generate spike time vector
    for ii in range(3000):
        randseed[ii] = rnd.uniform(0,1)
    timeseed = np.zeros(numspikes)
    for mm in range(int(numspikes)):
        timeseed[mm] = randseed[mm]
    spktimes = np.zeros(numspikes)
    cdfresample = sps.resample(cdf,20000)       #Some aliasing will occur but should be ok
    timevec = np.arange(0,1,float(1./len(cdfresample)))
    timevec = timevec*duration
    for jj in range(int(len(timeseed))):
        tempspk = randseed[jj]
        location = np.where(cdfresample == tempspk)
        if not location[0]:
            err = np.zeros(len(cdfresample))
            for kk in range(int(len(cdfresample))):
                tempcdf = cdfresample[kk]
                err[kk] = np.abs(tempcdf-tempspk)
            
            location = np.where(err==np.min(err))
        #pdb.set_trace()
        if np.size(location) <= 1:
            spktimes[jj] = timevec[location[0]]
        elif np.size(location) > 1:
            location = location[0]                #If matching spots, just take first one
            spktimes[jj] = timevec[location[0]]
    if numspikes == 0:
        spktimes = np.array([1,])
        spktimes[0] = 0
    spktimes = np.sort(spktimes)
    sp2 = spktimes
    return sp2
#def loadspikes(numE,numI,rpE,rpI,nclistA,nclistB,nclistC,nclistD):
#    from neuron import *
#    from nrn import *
#    import numpy as np
#    import pdb
#    #pdb.set_trace()
#    numE = 1
#    numI = 1
#    for jj in range(numE):
#        if len(rpE)>0:
#            numss = len(rpE[jj])
#            for ii in range(numss):
#                h.nclistA.o(jj).event((rpE[jj].x[ii]+200))
#                h.nclistB.o(jj).event((rpE[jj].x[ii]+200))
#    for nn in range(numI):
#        if h.rpI.size()>0:
#            numsI = h.rpI[jj].size()
#            for mm in range(numsI):
#                h.nclistC.o(nn).event((rpI[nn].x[mm]+200))
#                h.nclistD.o(nn).event((rpI[nn].x[mm]+200))
#        
def loadspikes(numE,numI,rpE,rpI,nclistA,nclistB,nclistC,nclistD):
    from neuron import h
    import numpy as np
    import pdb
    #pdb.set_trace()
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
def SpDetect(fdata):
    #Spike detection algorithm for Batch IC Analysis
    import numpy as np
    import pdb
    thresh = -15.0
    dlen = len(fdata)
    dt = 0.02
    shift = 1/dt
    #pdb.set_trace()
    t = np.linspace(0,int(((dlen-1)/shift)),num=dlen)
    derivDATA = np.diff(fdata)/np.diff(t)
    v = 1.0
    derivDATA = np.append(derivDATA,1.)
    d2DATA = np.diff(derivDATA)/np.diff(t)
    d2DATA = np.append(d2DATA,1.0)
    Spike2 = np.array([],dtype='float')
    for ii in range(len(fdata)):
        if np.transpose(fdata[ii])>=thresh:
            if np.transpose(derivDATA[ii]) > 0:
                Spike2 = np.append(Spike2,ii)
    #Spike2 = np.argwhere(fdata>=thresh and derivDATA > 0)
    spiktim = np.array([],dtype = 'float')
    #pdb.set_trace()
    if Spike2.size != 0:
        spiktim = np.append(spiktim,Spike2[0])
        o = 1
        for i in range(o,len(Spike2)):
            difs = Spike2[i]-Spike2[i-1]
            if difs >= 10:
                spiktim = np.append(spiktim,Spike2[i])
                o = o + 1
        Spike = spiktim
    else:
        Spike = np.array([])
    #pdb.set_trace()
    if not np.all(Spike == 0):
        spiketime = Spike/shift
        numspikes = Spike.size
    else:
        spiketime = -1.0
        numspikes = 0
    return [spiketime, numspikes]
        