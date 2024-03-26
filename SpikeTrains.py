#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:24:29 2024

@author: anushkashome
"""

import numpy as np

def spike_trains(dur, freq, num_spikes, jitter, xx):
    time_int = 1000/freq
    #spike_times = np.arange(dur, 750, time_int)
    spike_times = []
    i = 0
    prev_time = 0
    while i < num_spikes:
        spike_times.append(prev_time)
        prev_time += time_int
        if prev_time > 750:
            prev_time = 0     
        i = i+1
    if jitter:
        for i in range(num_spikes):
            spike_times[i] += xx*np.random.randn()
            
    #print (spike_times)
    list.sort(spike_times)
    return spike_times
        