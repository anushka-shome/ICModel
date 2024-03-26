# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def psth_to_vsAV(freqinput,spcycle,cyclesd,gausswid,strial):
    #gausswid is the relative width of the Gaussian
    #period is the modulation period in ms
    #spcycle is the average spikes per modulation cycle
    #cyclesd is the standard deviation of the spikes per cycle

    import numpy as np
    from numpy import random
    import pdb
    duration = 750.; # in ms
    period = (1./float(freqinput))*1000
    if period <= duration:
        numcycles = int(round(duration / period));
    else:
        numcycles = 1;
    #pdb.set_trace()
    prevspike = 1;   
    
    sptrial = strial * 0.75;
    
    #So now we do this:
    spkspertrial = sptrial /spcycle;
    genrandseed = (spcycle + np.random.standard_normal((1,))*cyclesd);
    
    ## Creation of raw spike probabilities
    
    if genrandseed < 0:
        genrandseed = np.abs((spcycle + np.absolute(np.random.standard_normal((1,1)))*cyclesd));
    if not np.isnan(spkspertrial):
        spnum = np.random.exponential(genrandseed,(1,numcycles));
        spnum = spnum[0];
        spnum = sorted(spnum,reverse=True);
    else:
        spnum = np.array([0.0])
    if len(spnum) < numcycles:
        temp = np.zeros(numcycles);
        for i in range (0,len(spnum)):
            temp[i] = spnum[i];
        spnum = np.array(temp);
        
    for i in range(0,len(spnum)):
        if spnum[i]>1:
            spnum[i] = round(spnum[i]);
    spnum = np.array(spnum);
    if len(np.where(spnum < 1)[0]) != 0:
        first = np.where(spnum <1)[0];

        test = np.mean(spnum[first[0]:len(spnum)]);

        sust = len(spnum[first[0]:len(spnum)]);

        spnum[first[0]:len(spnum)] = np.random.binomial(1,test,(1,sust))[0];

    
    spnum[np.where(spnum<0)] = 0; #no negative spike numbers
    nspikes = 10000; #number of spikes
    sphase = np.random.rand(1,nspikes)[0]; #generates random vector with number of spikes
   


    numbins = 360;

    psthbins = np.arange(2*np.pi/numbins,2*np.pi + 2*np.pi/numbins, 2*np.pi/numbins);
#    #NOTE THAT THE PSTHPROB IS THE PROBABILITY DISTRIBUTION OF THE PSTH
#    #IT CAN BE ANY FUNCTION SUCH AS GAUSSIAN, SINUSOIDAL, UNIFORM, ETC.

    psthprob = np.exp(-(gausswid*(psthbins-np.pi)**2));
    gsum = np.cumsum(psthprob); #divide this by gsum[len(gsum) - 1]
    
    #gsum = gsum/gsum[len(gsum)-1]

    
    spbin = [];
    spstart = [];
    phase = [];
    

    for i in range(0,len(sphase)):
        spbintemp = [];
        gdiff = [];
        sprop = []; 
        testsize = np.where(sphase[i]<gsum)
        if np.size(testsize)>1:
            spbintemp = np.amin(np.where(sphase[i]<gsum));
        else:
            spbintemp = []
        if not spbintemp:
            spbin.append(0);
            spstart.append(0);
            gdiff = gsum[1];
            sprop = sphase[i]/gdiff;

        elif spbintemp >0:
            spbin.append(spbintemp);
            spstart.append(spbintemp -1);
            gdiff = gsum[spbintemp] - gsum[spbintemp - 1];
            sprop = (sphase[i] - gsum[spbintemp - 1])/gdiff;
            phase.append(psthbins[spbintemp - 1] + 2*np.pi*sprop/numbins);
       
        elif spbintemp == 0:
            spbin.append(spbintemp);
            spstart.append(spbintemp - 1);
            gdiff = gsum[spbintemp]; # don't need to subtract from anything because it is the first bin
            sprop = (sphase[i])/gdiff;
            phase.append(2*np.pi*sprop/numbins);
    perhist = np.histogram(spbin, bins = np.arange(1,len(psthbins)+2,1))[0]; 
    vscos = sum(np.cos(psthbins[spbin]));
    vssin = sum(np.sin(psthbins[spbin]));
    vs = (1.0/nspikes)*(vscos**2+vssin**2)**0.5;
       
    spikevec = [];
    scount1 = 0;
    scount2 = 0;
    
    for i in range(0,int(numcycles)):
        cysptemp = [];
        svtemp = [];
        svtemp2 = [];
        pdtemp = [];
        cyspike = [];
        cysptemp = spnum[i];
        cyspike.append(cysptemp);
        scount1 = int(scount1 +cysptemp);
        pdtemp = period*np.array(phase[scount2:scount1])/(2*np.pi); #spike time diffs in ms
        pdtemp = sorted(pdtemp);
        pdiff = np.absolute(np.diff(pdtemp));
        if len(pdiff) != 0:
            pdref = [];
            pdref = np.where(pdiff <= 2)[0];
            if len(pdref) != 0:
                for j in range(0,len(pdref)):
                    
                    pdtemp[pdref[j]+1]= np.ndarray.tolist(np.squeeze(pdtemp[pdref[j]] + 1.5 + (period/5.0) * np.random.rand(1,1)))
                    #added absolute (1.5) and relative refractory period
        #print len(svtemp2)
        svtemp2 = period*(i)+np.array(pdtemp);
        svtemp2 = np.ndarray.tolist(svtemp2)
        
        spikevec.extend(svtemp2);
        scount2 = scount1+1;
    
    #spikevec = spikevec[0];
    
    spikevec = sorted(spikevec);
    sptic = np.ones([1,len(spikevec)]);
    cysum = sum(cyspike);
    spikevec = np.array(spikevec)
    sp2 = spikevec[:, None];

    return sp2

