#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:24:29 2024

@author: anushkashome
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

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
    #period = 1000/freq
    period = (float) ((1./freq) * 1000)
    w = 2 * np.pi/period
    #print(period)
    
    num_spikes = round(rate * 0.75)#check if rate is given in ms or s
    
    #spike_times = np.sort(np.random.uniform(0, 750, num_spikes))
    spike_times = []
    #spike_times.append(abs(rnd.uniform(0, 750)))
    spike_times.append(0)
    #print(len(spike_times))
    tolerance = 0.01
    #tolerance = 0.05 #?
    max_attempts = 1000000
    num_attempts = 0
    for i in range(1, num_spikes):
        num_attempts = 0
        #t = abs(rnd.uniform(spike_times[i-1], 750))
        #phase = rnd.uniform(0, 2*np.pi)
        #t = (phase/w) % 750
        t = abs(rnd.uniform(0, 750))
        while num_attempts < max_attempts:
            temp_times = spike_times + [t]
            curr_vs = vector_strength(temp_times, w)
            #print(curr_vs)
            if abs(curr_vs - vs) <= tolerance:
                spike_times.append(abs(t))
                num_attempts = 0
                break
            else:
                jitter = abs(curr_vs - vs)
                sf = 0
                if jitter > 0.2:
                    sf = 1000000
                    #sf = 10000000
                #elif jitter > 0.2:
                 #   sf = 1000
                elif jitter > 0.1:
                    sf = 1000
                    #sf = 1000
                else:
                    sf = 100
                jitter = jitter * sf
                t += rnd.uniform(-jitter, jitter)
                t = max(0, min(t, 750))
                #phase += rnd.uniform(-0.05, 0.05)
                #t = (phase/w) % 750
                num_attempts += 1
        if num_attempts == max_attempts:
            print("Failed to generate spike")
            spike_times.append(abs(t))
    #phases = 2 * np.pi * freq * 750
    print("--------------------")
    print(vector_strength(spike_times, w))
    list.sort(spike_times)
    spike_times = [round(time, 1) for time in spike_times]
    spike_times = spike_time_gap(spike_times)
    print(spike_times)
    final_vs = vector_strength(spike_times, w)
    return spike_times, final_vs

def spike_trains_VS_05(freq, rate, vs, synch, depth):
    
    period = (float) ((1./freq) * 1000)
    w = 2 * np.pi/period
    num_spikes = round(rate * 0.75)#check if rate is given in ms or s
    spike_times = []
    spike_times.append(abs(rnd.uniform(0, 750)))
    tolerance = 0.05
    max_attempts = 100
    num_attempts = 0
    for i in range(1, num_spikes):
        num_attempts = 0
        t = abs(rnd.uniform(0, 750))
        while num_attempts < max_attempts:
            temp_times = spike_times + [t]
            curr_vs = vector_strength(temp_times, w)
            if abs(curr_vs - vs) <= tolerance or len(spike_times) < 30:
                spike_times.append(abs(t))
                num_attempts = 0
                break
            else:
                t = abs(rnd.uniform(0, 750))
                num_attempts += 1
        if num_attempts == max_attempts:
            print("Failed to generate spike")
            spike_times.append(abs(t))
    print("--------------------")
    print(vector_strength(spike_times, w))
    list.sort(spike_times)
    spike_times = [round(time, 1) for time in spike_times]
    spike_times = spike_time_gap(spike_times)
    print(spike_times)
    final_vs = vector_strength(spike_times, w)
    return spike_times, final_vs
    
    '''
    #freq is modulation frequency
    #period = 1000/freq
    period = (float) ((1./freq) * 1000)
    w = 2 * np.pi/period
    #print(period)
    
    num_spikes = round(rate * 0.75)#check if rate is given in ms or s
    
    #spike_times = np.sort(np.random.uniform(0, 750, num_spikes))
    spike_times = []
    spike_times.append(abs(rnd.uniform(0, 750)))
    #spike_times.append(0)
    #print(len(spike_times))
    #tolerance = 0.01
    tolerance = 0.06 #?
    max_attempts = 100000000
    num_attempts = 0
    for i in range(1, num_spikes):
        num_attempts = 0
        #t = abs(rnd.uniform(spike_times[i-1], 750))
        #phase = rnd.uniform(0, 2*np.pi)
        #t = (phase/w) % 750
        t = abs(rnd.uniform(0, 750))
        while num_attempts < max_attempts:
            temp_times = spike_times + [t]
            curr_vs = vector_strength(temp_times, w)
            print(curr_vs)
            if abs(curr_vs - vs) <= tolerance or len(spike_times) < 30:
                spike_times.append(abs(t))
                num_attempts = 0
                break
            else:
                jitter = abs(curr_vs - vs)
                sf = 0
                if jitter > 0.1:
                    #sf = 1000000
                    sf = 10000000
                #elif jitter > 0.2:
                 #   sf = 1000
                elif jitter > 0.05:
                    sf = 1000
                 #   sf = 10000
                else:
                    sf = 100
                jitter = jitter * sf
                t += rnd.uniform(-jitter, jitter)
                t = max(0, min(t, 750))
                #phase += rnd.uniform(-0.05, 0.05)
                #t = (phase/w) % 750
                num_attempts += 1
        if num_attempts == max_attempts:
            print("Failed to generate spike")
            spike_times.append(abs(t))
    #phases = 2 * np.pi * freq * 750
    print("--------------------")
    print(vector_strength(spike_times, w))
    list.sort(spike_times)
    spike_times = [round(time, 1) for time in spike_times]
    spike_times = spike_time_gap(spike_times)
    print(spike_times)
    print(vector_strength(spike_times, w))
    return spike_times
'''

def vector_strength(spike_times, w):
    p_w = 0
    times = spike_times
    i = 1j
    for time in times:
        p_w += np.exp(i*w*time)
    p_w = p_w/len(times)
    #print(abs(p_w))
    return abs(p_w)

def spike_time_gap(spike_times):
    for i in range(1, len(spike_times)):
        if spike_times[i] - spike_times[i-1] <= 0.1:
            spike_times[i] = spike_times[i-1] + 0.2
        
    return spike_times

def main():
    #spike_trains_VS(32, 100, 1, True, 0)
    vs = [0.05, 0.2, 0.4, 0.6, 0.8]
    all_spikes = []
    for v in vs:
        if v == 0.05:
            spikes,_ = spike_trains_VS_05(8, 100, 0.05, True, 0)
        else:
            spikes,_ = spike_trains_VS(8, 100, v, True, 0)
        all_spikes.append(spikes)
    # Create the raster plot
    plt.figure(figsize=(8, 6))
    # Create a custom colormap by removing the middle white region
    colors_list = ["#8B0000", "#00008B"]  # Dark red → Dark blue (Hex codes)
    custom_cmap = LinearSegmentedColormap.from_list("dark_red_blue", colors_list, N=256)
    colors = custom_cmap(np.linspace(0, 1, len(vs))) 
    plt.eventplot(all_spikes, orientation='horizontal', lineoffsets=range(len(vs)), linelengths=0.8, colors=colors)

    # Adjust y-axis to show frequencies as categorical labels
    plt.yticks(range(len(vs)), [str(v) for v in vs])  # Treat frequencies as categories
    plt.xlabel("Time (s)")
    plt.ylabel("Vector Strength")
    plt.title("Spike Train Raster Plot")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

    

if __name__ == "__main__":
    main()
