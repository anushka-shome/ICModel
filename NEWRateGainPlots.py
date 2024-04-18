# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:09:09 2015

@author: Alex
"""

def NEWRateGainPlots(EXins, INins, numtrials, mempot):
    import numpy as np    
    import scipy.io as sio    
    
    freq = np.array([8,16,32,64,128,256,512,1024]);
    
    del PerTrialSpk
    del PerVS2
    del PerRAY2
    del RayStat
    del VSstat
    
#    load TrialSPK2
    
    z=1;
    k = mempot;
    
    for i in range(0,len(freq)):
        for g in range(0,numtrials):
#            numE = np.size(((EXins[i,g,z])['no'][oh])['list']);
            for oh in range(0,numI):
#                dummy2 = len(INins[i,g,z]['no'][oh]['list']);
                set2[oh] = dummy2/0.750;
            idRAWe[g] = np.mean(set2);
            numI = np.size(INins(i,g,z)['no'],2);
            for oh in range(0,numI):
#                dummy3 = len(INins(i,g,z).no(oh).list);
                set3[oh] = dummy3/0.750;
            idRAWi[g] = np.mean(set3);
        ratesE[i] = np.mean(idRAWe);
        ratesI[i] = np.mean(idRAWi);
        
    for i in range(0,len(freq)):
        for g in range(0,numtrials):
            dummy = len(PerTrialSpk(i,z,k).test(g).data);
            flash[g] = dummy/0.75;
            permean[i] = np.mean(flash);
            rategainE[i] = permean[i]/ratesE[i];
            rategainI[i] = permean[i]/ratesI[i];
            
    nfig = plt.figure();
    plt.semilogx(freq,rategainE, color = b, linestyle = '-')
    plt.semilogx(freq, rategainI, color = r,linestyle = '-',marker = '+')
    plt.xlim(1,1100);
    plt.ylim(0,3);
    plt.xlabel('Rate Gain');
    plt.ylim('Period (ms)');
    plt.savefig("ICRateGains.fig",nfig)
    
    return
#NumE = 1
#NumI = 1
#delays = 0
#numtrials = 10
#freq = [8,16,32,64,128,256,512,1024];
#k = 1   
NEWRateGainPlots(EXins, INins, numtrials, mempot)           
        
                