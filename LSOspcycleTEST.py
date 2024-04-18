# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:57:01 2015

@author: Alex
"""

def LSOspcycleTEST(freq, mins, peak, mins2):
    import numpy as np;
    freq = np.array(freq);
    mins = np.array(mins);
    peak = np.array(peak);
    mins2 = np.array(mins2);
    
    spcycle = np.zeros((1,len(freq)));
    spcycle = spcycle[0];
    counter = 0;
    for value in freq:
        if value == peak:
            spcycle[counter]=1;
        counter +=1;
    spcycle[0] = mins;
    spcycle[5:8] = mins2;
    
    testc = np.where(freq == peak);
    testc = testc[0]
    testc = testc[0]
    if testc == 1:
        for i in range(testc+1,5):
            spcycle[i] = mins2 + (5.0-i)*(1.0 - mins2)/(5.0 - testc);
    if testc == 2:
        for i in range(1,(testc)):
            spcycle[i] = mins + (i*1.0)*(1.0-mins)/(testc*1.0);
        for i in range (testc,5):
            spcycle[i] = mins2 +(5.0 - i)*(1.0-mins2)/(5.0-testc);
    if testc ==3:
        for i in range(1,testc):
            spcycle[i] = mins + (i*1.0)*(1.0-mins)/(testc*1.0);
        spcycle[4] = np.mean([1,mins2]);
    scale = spcycle;
    scale = np.array(spcycle);
    mrates = scale * 64;
    spcycle2 = mrates / freq;

    
    return spcycle2

spcycle2 = LSOspcycleTEST([8,16,32,64,128,256,512,1024], 0, 32, 0);
#print spcycle2