# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 07:41:01 2015

@author: Alex
"""

def OnsetRatioMeasure(numtrials,k):
    import scipy.io as sio
    import numpy as np
    import matplotlib.pyplot as plt
    
    placeholder = sio.loadmat('TrialSPK2.mat')
    PerTrialSpk = placeholder['PerTrialSpk'] 
    freq = np.array([8,16,32,64,128,256,512,1024]);   
    k = np.array([k]);
    if len(k) == 0:
        k = [8];
    k = k[0]
    z = 0;
    MeanOnsetRatio = []; 
    rateOns = [];
    rateSus = [];
    OnsetRatio = []; OnsetRatioStDev = []; OnsetRatioStErr = [];
    for i in range(0, len(freq)): 
        for g in range(0, numtrials): 
            dummy1 = []; dummy2 = []; onset = []; sustained = [];
            onset = PerTrialSpk[i,z,k-1]['test'][0][g]['data'][0][PerTrialSpk[i,z,k-1]['test'][0][g]['data'][0] <= 350];
            dummy1 = len(onset);
            rateOns.append(dummy1/0.150);
            sustained = PerTrialSpk[i,z,k-1]['test'][0][g]['data'][0][PerTrialSpk[i,z,k-1]['test'][0][g]['data'][0] > 350];
            dummy2 = len(sustained);
            rateSus.append(dummy2/0.600);
            OnsetRatio.append((rateOns[g]-rateSus[g])/(rateOns[g] + rateSus[g])); ## may need to add np.array  to these
            if np.isnan(OnsetRatio[g]):
                OnsetRatio[g] = [];
        MeanOnsetRatio.append(np.mean(OnsetRatio));
        OnsetRatioStDev.append(np.std(OnsetRatio)); 
        OnsetRatioStErr.append(OnsetRatioStDev[i]/np.sqrt(numtrials));
       
    plt.figure;
    plt.errorbar(freq,MeanOnsetRatio,OnsetRatioStErr)
    plt.errorbar(freq,MeanOnsetRatio,OnsetRatioStErr)
    plt.xlabel('Modulation Freq')
    plt.xlim([0, 1024])
    plt.ylim([-1, 1])
    plt.ylabel('Vector Strength')
    plt.savefig('ICOnsRat.png');
 
    return [MeanOnsetRatio, OnsetRatioStErr]
    
