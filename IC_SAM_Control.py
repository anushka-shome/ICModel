#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Author: Brandon S Coventry               Purdue University CAP lab, Wisconsin Institute for Translational Neuroengineering
# Date: 03/05/2022
# Revision History: None
# Purpose: Control program for IC Model SAM runs. Use this program to perform model runs (without swarm optimization)
# Notes: Modified from Coventry et al J Comput Neuro 2017 and Rabang et al Front Neural Circuits 2012. See these papers for more details
# I/O Variables: N/A, stand alone and set variables here.
# Python Version notes: Runs on Python 3. Tested on 3.6.8, cannot guarentee performance on 3.8+
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import required packages
import numpy as np
import matplotlib.pyplot as plt
import neuron
import nrn
import scipy.io
from numpy.matlib import randn
import pdb
import random as rnd
import math
# Import helper files
# Note, loading via the * is not recommended generally, but we use here since we developed helper functions
from IC_SustainedFiring import IC_SustainedFiring     #This is the sustained model     
from IC_AdaptedFiring import IC_AdaptedFiring 
from InputPSTHs import SpDetect
from MSOchars import MSOchars
from DCNchars import DCNchars
from LSOChars import LSOChars
from VCNchars import VCNchars
from DCNchars import DCNchars
from DNLLchars import DNLLchars
from VNLLchars import VNLLchars
from VNLLchars import VNLLchars
from psth_to_vsAV import psth_to_vsAV
from inputProb import inputProb
from BETAchars import BETAchars
from ICModelAnalysis import ICstats,fitfuncm
from SpikeTrains import spike_trains


# Setup model input parameters
networkcheck = 0              #For extension to networks eventually.
rndseed = 0.7254
sgi = np.array([8,16,32,64,128,256,512,1024])         #These are the AM Modulation frequencies. Log spaced between 8 and 1024.
periods = (1.0/sgi)*1000          #Set in milliseconds
numE = 1                #Number of excitatory and inhibitory inputs. For this model, we lump conductances together. Distributed conductances not implemented just yet. 
numI = 1                # Yell at Brandon to do so at some point.
cfe = input('Input Excitatory Best Modulation Frequency: ')        #Input Excitatory Best modulation frequency
cfe = float(cfe)
cfi = input('Input Inhibitory Best Modulation Frequency: ') #Input Inhibitory Best Modulation Frequency
cfi = float(cfi)
latency = 5                           #Input PSTH latency
numtrials = 10                   #Sets the total number of repititions to build tMTFs
yoo = input('Young(0) or Aged(1) model: ')    #Young or aged model
yoo = int(yoo) 
AMPAConduct = float(input('Input AMPA Conductance (In %, 200 -> 2 inputs, etc '))
NMDAConduct = float(input('Input NMDA Conductance (In %, 200 -> 2 inputs, etc '))
GABAAConduct = float(input('Input GABA A Conductance (In %, 200 -> 2 inputs, etc '))

# OUnoise vector: [EX conductance, In Conductance, EX sd, In sd, Ex tau, In tau]
if yoo == 0:
    OUnoise = [0.000935,0.0005,0.0008891,0.0005,2,10]
else:
    OUnoise = [0.000935,0.0001,0.0008891,0.0005,2,10] #0.00047
Etype = input('Excitatory Inputs - 1) MSO, 2) DCN (Default = 2) 3) LSO: 4) VCN Chopper: ')   # Input Excitatory Nuclei 1 MSO, 2 DCN, 3 LSO 4 VCN
Etype = int(Etype)
Itype = input('Inhibitory Inputs - 1)DNLL, 2)VNLL (Default = DNLL): ')                       # Input Inhibitory Nuclei 1 DNLL 2 VNLL 
Itype = int(Itype)
quota = input('All Pass? 1.)')     #Different filtering characteristics for DCN not implemented yet. Yet again, yell at Brandon
# Set the synaptic parameters
multiplierA = 100           #NMDA conductance reduction
multiG = 100                #GABAa conductance
gTau = 15                   #GABAa ISPC decay Tau (ms)
vdepscale = 35.7            #NMDA voltage dependence
EXprob = 1                  #EX release prob
APPDTau = 25.42             #Apparent Postsynaptic Decay Tau
PPDRatio= .6629             #Paired-Pulse Depression Ratio
gTau1 = 3
tprime = ((gTau*gTau1)/(gTau-gTau1))*np.log(gTau/gTau1) #np.log() is base e
gscale = 1/(np.exp(-tprime/15.0) - np.exp(-tprime/3.0))
GPPDTau = APPDTau * PPDRatio

AMPAtau1 = .5464
AMPAtau2 = 6
NMDAtau1 = 32
NMDAtau2 = 50
GABAtau1 = 3
GABAtau2 = 15
duration = .75
# Setup inputs
#Notes: a,b,c are curve fit parameters for static input tuning characteristics. See Rabang et al for details.
if Etype == 1:
    a = 119.6
    b = -0.006725
    c = -120.5
    d = -0.01828
    [EXvs, EXrates, EXspcycle, EXgaussvs, EXcyclesd] = MSOchars(sgi,a,b,c,d)
    AMPA = 5
    NMDA = 3
elif Etype == 2:
    a =  -308.9      #a,b,c are curve fit parameters for static input tuning characteristics. See Rabang et al for details.
    b =  -0.01862 
    c =   359.8
    [EXvs, EXrates, EXspcycle, EXgaussvs, EXcyclesd] = DCNchars(sgi,quota,a,b,c)
    AMPA = 6
    NMDA = 1.5
elif Etype  == 3:
    [EXvs, EXrates, EXspcycle, EXgaussvs, EXcyclesd] = LSOChars(sgi)
    AMPA = 5
    NMDA = 1.5  
elif Etype  == 4:
    [EXvs, EXrates, EXspcycle, EXgaussvs, EXcyclesd] = VCNchars(sgi)
    AMPA = 5
    NMDA = 1.5
elif Etype == 5:
    # This is for generating aribtrary input tMTFs based off a beta distribution. Set params based on needs.
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    [EXvs, EXrates, EXspcycle, EXgaussvs, EXcyclesd] = BETAchars(sgi,a,b,c,d,e,f)
    AMPA = 5
    NMDA = 1.5
else:
    #Default to DCN
    a =  -308.9      
    b =  -0.01862 
    c =   359.8
    [EXvs, EXrates, EXspcycle, EXgaussvs, EXcyclesd] = DCNchars(sgi,quota,a,b,c)
    AMPA = 6
    NMDA = 1.5

#Inhibitory characteristics
if Itype == 1:
    [INvs, INrates, INspcycle, INgaussvs, INcyclesd] = DNLLchars(sgi,quota)
    GABA = 3
elif Itype == 2:
    [INvs, INrates, INspcycle, INgaussvs, INcyclesd] = VNLLchars(sgi)
    GABA = 4
elif Itype == 3: #not implemented
    # This is for generating aribtrary input tMTFs based off a beta distribution. Set params based on needs.
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    [INvs, INrates, INspcycle, INgaussvs, INcyclesd] = BETAchars(sgi,a,b,c,d,e,f)
else:
    [INvs, INrates, INspcycle, INgaussvs, INcyclesd] = DNLLchars(sgi,quota)
    GABA = 3
#Setup Receptor conductances
perAMPA = AMPAConduct           #Grab current AMPA conductance
perNMDA = NMDAConduct           #Grab current NMDA conductance
perGABA = GABAAConduct           #Grab current GABA conductance
AMPA1 = AMPA*(perAMPA/100.)     # Different from input line
NMDA1 = NMDA*(perNMDA/100.)
GABA1 = GABA*(perGABA/100.)
GABAB = 0                        #No GABAB for now. Another time to yell at Brandon
E = [AMPA1,NMDA1,GABA1,GABAB]
#Biascur = .091   #Generate Bias current, should set resting potential at -60mV
Biascur = 0.091
# Set run params:
PerTrialSpk = np.zeros([numtrials,len(sgi)])          #Spike storage
onset = 200.           #Wait 200 ms before turning on stimulation
stimduration = 750.    #Stimulation time. Total run time set in NEURON is 1000 ms. Offset is then 50 ms
spikevec = [0 for i in range(len(sgi))]
delays = 0                                 #Add in extra delay on inputs if wanted.
#EXgaussvs = np.array([1.1519, 1.1519, 1.1519, 1.1519, 1.1519, 0.3586, 0.1088, 0.0372])
#INgaussvs = np.array([1.1519, 1.1519, 1.1519, 1.1519, 1.1519, 0.3586, 0.1088, 0.0372])
EXvariance = 0          #Add in randomness to drivin inputs. 
INvariance = 0
drvinputsE=[]
drvIinputs=[]
VecStrength = np.zeros(len(sgi), dtype=float)
total_spikes = np.zeros(len(sgi))

# Create a Model cell
#ICCell = IC_AdaptedFiring(numE,numI,OUnoise,drvinputsE,drvIinputs,gscale,vdepscale,Biascur,E,AMPAtau1,AMPAtau2,NMDAtau1,NMDAtau2,GABAtau1,GABAtau2,rndseed)
ICCell = IC_SustainedFiring(numE,numI,OUnoise,drvinputsE,drvIinputs,gscale,vdepscale,Biascur,E,AMPAtau1,AMPAtau2,NMDAtau1,NMDAtau2,GABAtau1,GABAtau2,rndseed)

for nn in range(len(sgi)):
    spcycleE = EXspcycle[nn]
    cyclesdE = EXcyclesd[nn]
    gaussvsE = EXgaussvs[nn]
    ratesE = EXrates[nn]
    spcycleI = INspcycle[nn]
    cyclesdI = INcyclesd[nn]
    gaussvsI = INgaussvs[nn]
    ratesI = INrates[nn]
    trialvec = [0 for j in range(numtrials)]
    spike_phases = []
    #angfreq = 2*np.pi*sgi[nn]
    #total_spikes = 0;
    period = (float) ((1./sgi[nn]) * 1000)
    numcycle = round(750./period)
    if(numcycle == 0):
        numcycle = 1
    spcycle = (float)(750./numcycle)
    for mm in range(numtrials):
        for zz in range(1):
            drvinputs = psth_to_vsAV(sgi[nn],spcycleE,cyclesdE,gaussvsE,ratesE)
            #print(drvinputs)
            #print(len(drvinputs))
            drvinputs = inputProb(drvinputs,EXprob)
            drvIinputs = psth_to_vsAV(sgi[nn],spcycleI,cyclesdI,gaussvsI,ratesI)
            
            #For spike trains:
            #drvinputs = spike_trains(100, 10, len(drvinputs), False, 0)
            #drvIinputs = np.zeros(len(drvIinputs))
            
            #if sgi[nn] == 6498:
                #pdb.set_trace()
                
            #/*Remove for spike trains
            jittershift = delays
            B = drvinputs + EXvariance*np.asarray(randn(1))[0][0]
            C = drvIinputs + jittershift + INvariance*np.asarray(randn(1))[0][0]
             #*/
             
            randseed = rnd.uniform(0,1)
            randseed = round(randseed*100)
            
            #/*Remove for spike trains
            if np.size(drvinputs)> 0:
                drvinputs = np.concatenate(drvinputs)
            else:
                drvinputs = np.asarray(drvinputs)
            if np.size(drvIinputs)>0:
                drvIinputs = np.concatenate(drvIinputs)
            else:
                drvIinputs = np.asarray(drvIinputs)
            #ICCell.loadInputs(drvinputsE,drvIinputs)
            #*/
            
            ICCell.setRNDSeed(randseed)
            #[spikes, nums] = spike_trains(100, 10, False, 0)
            #spike_trains = np.asarray(spike_trains)
            #[spkts, voltages] = ICCell.loadSpikeTimes(spikes,spikes)
            [spkts, voltages] = ICCell.loadSpikeTimes(drvinputs,drvIinputs)
            #[spkts, voltages] = SustainedFiring_PSO(numE,numI,OUnoise,networkcheck,randseed,drvinputs,drvIinputs,APPDTau,GPPDTau,gTau,gscale,vdepscale,agent[3,0],Biascur,E,AMPAtau1,AMPAtau2,NMDAtau1,NMDAtau2,GABAtau1,GABAtau2)
            [spike_timesRAW, num_spikes] = SpDetect(voltages[0]) #Count and detect spikes
            #print(spike_timesRAW)
            #[spike_timesRAW, num_spikes] = spike_trains(100, 10, True, 1)
            #spike_timesRAW = spike_trains(100, 10, num_spikes, False, 0)
            #total_spikes += num_spikes
            spike_timesRa = np.array([],dtype = 'float')
            offset = np.array([],dtype = 'float')
            for uu in range(num_spikes):
                if (spike_timesRAW[uu] > onset + stimduration):
                    offset = np.append(offset,spike_timesRAW[uu])
            offset = offset - stimduration
            spike_timesRa = np.array([],dtype = 'float')
            for yy in range(num_spikes):
                #pdb.set_trace()
                if spike_timesRAW[yy] > 0: 
                    if spike_timesRAW[yy] <= stimduration+onset:
                        spike_timesRa = np.append(spike_timesRa,spike_timesRAW[yy])
            if len(spike_timesRa) > 0:
                spike_times = spike_timesRa - onset
            else:
                spike_times = []
            #[trialvec[mm], num_spikes] = spike_trains(100, 10)
            trialvec[mm] = spike_timesRAW
            tempphase = []
            j = 0
            
            #/*Remove for spike trains
            offset_index = 0
            if (len(offset) == 0):
                offset_index = len(spike_timesRa) + 1 
            else:
                offset_index = len(spike_timesRa) - len(offset)
            offset_ind = 0
            #*/
            
            while(j < len(trialvec[mm])):
                new_time = trialvec[mm][j]
                
                #/*Remove for spike trains
                if (j == offset_index):
                    #new_time -= offset[offset_ind]
                    offset_ind += 1 
                    offset_index += 1
                #*/
                
                while (new_time > (spcycle)):
                    new_time -= spcycle
                tempphase.append(new_time/spcycle)
                j += 1
            #curr_len = len(spike_phases)
            for k in tempphase:
                spike_phases.append(k)
    spikevec[nn] = trialvec
    #spike_phases = spike_phases*2*np.pi
    spike_phases = np.array(spike_phases)
    for i in range(len(spike_phases)):
        spike_phases[i] = spike_phases[i]*2*np.pi
    vscos = sum(np.cos(spike_phases))
    vssin = sum(np.sin(spike_phases))
    #if (nn == len(sgi)-1):
     #   print(spike_phases)
      #  print(vscos)
       # print(vssin)
    VecStrength[nn] = np.sqrt(vscos**2 + vssin**2)
    if (len(spike_phases) != 0):
        VecStrength[nn] /= (len(spike_phases))
    total_spikes[nn] = len(spike_phases)
    
        #print(sgi[nn])
    #else:
        #VecStrength[nn] = 0
    #pdb.set_trace()
#print(spikevec)
#print(sgi) #modulation frequencies
#print(trialvec)
#print("Out")
#print(VecStrength)
#Rayleigh's test
R = np.zeros(len(sgi))
for i in range(len(sgi)):
    R[i] = (VecStrength[i]**2) * total_spikes[i] * 2
    #print(R[i])
R_ind = (R > 13.8)
vec_plot = VecStrength[R_ind]

#

#Main Plot
[meanvec,sdvec] = ICstats(spikevec,numtrials,sgi)
sevec = sdvec/np.sqrt(numtrials)            #Set up standard error
#Fitfun = fitfuncm(meanvec,sdvec,sgi,expdata["totmean"][0][1:9],expdatasd[1:9])
#fig, (ax1) = plt.subplots(1, 1)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
#ax1.set_xscale("log",'mask')
ax1.set_xscale("log")
ax1.errorbar(sgi,meanvec,yerr=sevec)
plt.xlim([sgi[0] - 1, sgi[len(sgi)-1] + 100])
plt.xlabel("Modulation Frequency")
plt.ylabel("Spike Rate (spike/s)")



#With Vector Strength (at synchronization only)
ax2 = ax1.twinx()
ax2.plot(sgi[R_ind], vec_plot, 'ro')
if (len(R_ind) > 1):
    for i in range(len(R_ind)-2):
        if (R_ind[i] & R_ind[i+1]):
            ax2.plot([sgi[i], sgi[i+1]], [VecStrength[i], VecStrength[i+1]], "r-")
ax2.set_ylim(0, 0.8)
#ax2.ylabel("Vector Strength")
ax2.set_ylabel("Vector Strength", rotation=-90, labelpad=20)
print(R_ind)

#With Vector Strength
ax2 = ax1.twinx()
ax2.plot(sgi, VecStrength, 'ro-')
ax2.set_ylabel("Vector Strength", rotation=-90, labelpad=20)
ax2.set_ylim(0, 0.8)


'''
#PSTH
#For now, 750 bins with 1ms duration
#8 mod. freq: spikevec[0]
curr_time = 0
spikearr = np.zeros((10, 750))
for i in range(len(spikevec[0])):
    print(len(spikevec[0][i]))
    for j in range(len(spikevec[0][i])):
        binum = math.floor(spikevec[0][i][j])
        print(binum)
        if (binum < 750):
            spikearr[i][binum] = 1

print(spikearr)

fig, ax = plt.subplots()
ax.bar(np.arange(750) * 1, np.mean(spikearr, 0), width = 5, align = 'edge')
ax.set_title('Peri-Stimulus Time Histogram (PSTH)')
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Prob. spike occurrences at this time')
plt.show()
'''

'''
#Dot Raster Plot
#Using mod. freq 8 only

plt.figure(figsize=(7, 15))
plt.eventplot([spikevec[0][0], spikevec[0][1], spikevec[0][2], spikevec[0][3], spikevec[0][4], spikevec[0][5], spikevec[0][6], spikevec[0][7], spikevec[0][8], spikevec[0][9]], linelengths=0.5)
plt.xlabel('Time (s)')
plt.ylabel('Trial')
plt.title('Raster Plot of Spike Times')
plt.grid(True)
#print(meanvec)
#plt.plot(meanvec)
#plt.set_xscale("log")
'''
plt.show()





