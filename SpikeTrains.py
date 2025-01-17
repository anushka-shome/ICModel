#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:24:29 2024

@author: anushkashome
"""

import numpy as np
import random as rnd

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
            spike_times[i] += xx*rnd.uniform(0,1)
            if spike_times[i] < 0:
                spike_times[i] = 0
    #print (spike_times)
    list.sort(spike_times)
    #print(spike_times)
    return spike_times
        
def spike_trains_VS(freq, rate, vs, synch, depth):
    #freq is modulation frequency
    period = 1000/freq
    w = 2 * np.pi/period
    #print(period)
    
    num_spikes = round(rate * 0.75)#check if rate is given in ms or s
    
    #spike_times = np.sort(np.random.uniform(0, 750, num_spikes))
    spike_times = [0]
    print(len(spike_times))
    tolerance = 0.01
    max_attempts = 100
    num_attempts = 0
    for i in range(1, num_spikes):
        t = rnd.uniform(spike_times[i-1], 750)
        while num_attempts < max_attempts:
            temp_times = spike_times + [t]
            curr_vs = vector_strength(spike_times, w)
            if abs(curr_vs - vs) <= tolerance:
                spike_times.append(t)
                num_attempts = 0
                break
            else:
                t += rnd.uniform(-0.005, 0.005)
                t = max(0, min(t, 750))
                num_attempts += 1
        if num_attempts == max_attempts:
            print("Failed to generate spike")
    #phases = 2 * np.pi * freq * 750
    return spike_times

def vector_strength(spike_times, w):
    p_w = 0
    times = spike_times
    i = 1j
    for time in times:
        p_w += np.exp(i*w*time)
    p_w = p_w/len(times)
    return abs(p_w)