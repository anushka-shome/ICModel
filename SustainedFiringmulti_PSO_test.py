"""
Created on Mon June 14 3:14 P.m. 2015

Author: Brandon S Coventry Lauren Marussich
Purpose: Multicomp Python model
Revision History: Aug 18: Continued work. For future updates, see GIT
"""

from neuron import *
from nrn import *
import numpy as np
import pdb
from InputPSTHs import *
import matplotlib.pyplot as plt

def SustainedFiringmulti_PSO():#(numE,numI,OUnoise,networkcheck,rndseed,drvinputsE,drvIinputs,appdtau,gppdtau,gtau,gscale,nmdavdep,mempot,biascur,Neurotransvec,ampatau1,ampatau2,nmdatau1,nmdatau2,gabatau1,gabatau2):
    #Start by calling necessary packages
#    from neuron import *
#    from nrn import *
#    import numpy as np
#    import pdb
#    from InputPSTHs import *
    #Next declare sections and appropriate biophysics
    #Soma
    soma = h.Section()
    soma.nseg = 1
    soma.Ra = 150
    soma.L = 34.5468
    soma.diam = 14.0754
    soma.cm = 1
    #soma.insert('pas')
    #soma.g_pas=0.0019
    #soma.e_pas=-70
    soma.insert('Isodium')
    soma.ena = 50
    soma.vtraub_Isodium = -52
    soma.gnabar_Isodium = 0.1
    
    soma.insert('kLT_VCN2003')
    soma.gkbar_kLT_VCN2003 = 0
    #soma.ek_kLT_VCN2003 = -90        #Change in mod code
    
    soma.insert('kHT_VCN2003')
    soma.gkbar_kHT_VCN2003 = 0.005
    #soma.ek_kHT_VCN2003 = -90        #Change in mod code
    
    soma.insert('kdr')
    soma.gbar_kdr = 0.1
    #soma.ek_kdr = -90                #Changed in mod code
    
    soma.insert('kdrtea')
    #soma.ek_kdrtea=-90               #Changed in mod code
    
    soma.insert('ik2')
    #soma.ek_ik2=-90                  #Changed in mod code
    soma.gbar_ik2 = 0
    
    soma.insert('hsus')
    soma.eh_hsus = -40
    soma.gh_hsus = 0
    soma.ek = -90
    
    #Axon generation
    axon = h.Section()
    axon.nseg = 1
    axon.Ra = 150
    axon.cm = 1
    axon.L = 100
    axon.diam = 2
    axon.insert('pas')
    axon.g_pas=0.00019
    axon.e_pas=-70
    
    axon.insert('Isodium')
    axon.ena=50
    axon.vtraub_Isodium = -52
    axon.gnabar_Isodium=0.2
    
    axon.insert('kdr')
    axon.gbar_kdr=0.1
    
    #Axon Hillock Generation
    hillock = h.Section()
    hillock.Ra = 150
    hillock.cm = 1
    hillock.L = 100
    hillock.diam = 3
    hillock.insert('Isodium')
    hillock.ena = 50
    hillock.vtraub_Isodium = -52
    hillock.gnabar_Isodium = 0.2
    
    hillock.insert('kLT_VCN2003')
    hillock.gkbar_kLT_VCN2003 = 0 
    
    hillock.insert('kHT_VCN2003')
    hillock.gkbar_kHT_VCN2003 = 0.005
    
    hillock.insert('kdr')
    hillock.gbar_kdr = 0.1
    
    hillock.insert('kdrtea')
    #hillock.ek_kdrtea=-90
    
    hillock.insert('ik2')
    hillock.gbar_ik2=0
    
    hillock.insert('hsus')
    hillock.gh_hsus=0
    hillock.eh_hsus=-40
    hillock.ek=-90
    
    #Now proximal dendrite
    proxdend = h.Section()
    proxdend.Ra = 150
    proxdend.cm = 1
    proxdend.L = 150
    proxdend.diam = 1.4
    proxdend.insert('pas')
    proxdend.g_pas=0.00019
    proxdend.e_pas=-70
    
    proxdend.insert('Isodium')
    proxdend.ena = 50
    proxdend.vtraub_Isodium = -52
    proxdend.gnabar_Isodium = 0.2
    
    proxdend.insert('kLT_VCN2003')
    proxdend.gkbar_kLT_VCN2003 = 0 
    
    proxdend.insert('kHT_VCN2003')
    proxdend.gkbar_kHT_VCN2003 = 0.005
    
    proxdend.insert('kdr')
    proxdend.gbar_kdr = 0.1*1.1
    
    proxdend.insert('kdrtea')
    #hillock.ek_kdrtea=-90
    
    proxdend.insert('ik2')
    proxdend.gbar_ik2=0
    
    
    #Finally distal dendrite
    distdend = h.Section()
    distdend.Ra = 150
    distdend.cm = 1
    distdend.L = 250
    distdend.diam = 0.882
    
    distdend.insert('pas')
    distdend.g_pas = 0.00019
    distdend.e_pas = -70
    
    #Connect Sections together
    hillock.connect(soma,1,0)
    axon.connect(hillock,1,0)
    proxdend.connect(soma,0,0)
    distdend.connect(proxdend,1,0)
    #print "I made it here!"
    
#    stim = h.IClamp(distdend(0.5))           #This is here to test model
#    stim.delay = 200
#    stim.amp = .15
#    stim.dur = 200

# Test Start
    # Test using values in FreqTuningPSO_WTA.py
    
    # Def null variable (?)
    h('objref nil')
    
    # excitatory: AMPA,NMDA at
    p=h.AMPA_LL_IC(0.5)
    p.tau1=.5464
    p.tau=6
    p2=h.NMDA_LL_IC_2(0.5)
    p2.vdepscale=35.7
    p2.tau1=32
    p2.tau=50
    # use h.NetCon for POINT_PROCESS with NET_RECEIVE block for event driven firing
    tmp_c=h.NetCon(h.nil,p,0,1,(5))
    tmp_c_2=h.NetCon(h.nil,p2,0,1,(3))
    
    # NetCon queue of events
    c_list=[tmp_c,tmp_c_2,tmp_c,tmp_c_2,tmp_c,tmp_c_2]
    # Corresponding timings
    timings=[200,200,210,210,300,300]
    #tmp_c.event(300)
    
    #fih2 = h.FInitializeHandler((tmp_c.event, (500)))
    
    # set up presynaptic events
    fih2 = h.FInitializeHandler((my_event_handler, (c_list,timings)))
    
    #Run parameters
    trans = 0
    h.dt = 0.02
    Dt = 0.02
    npoints=50000
    tstart = trans
    tstop = trans + Dt*npoints
    v_init = -60
    h.celsius = 34
    steps_per_ms = 1/Dt
    
    rec_t = h.Vector()
    rec_t.record(h._ref_t)
    rec_v = h.Vector()
    rec_v.record(axon(0.5)._ref_v)
    h.finitialize()
    #run(tstop)
    target_t=25000
    cnt=0
    while h.t<tstop:
        cnt+=1
#        if cnt==target_t:
#            stim = h.alphasyn(proxdend(0.5))
#            stim.e=10000
#            stim.i=100
        h.fadvance()
    
    g = h.Graph()
    g.size(0, 5, -80, 20)
    rec_v.line(g, rec_t)
    #import matplotlib.pyplot as plt

    # get values from NEURON-vector format into Python format
    times = [] # Use list to add another trace later.
    voltages = []
    times.append(list(rec_t)) # alternativ to `list(rec_t)`: `numpy.array(rec_t)`
    voltages.append(list(rec_v))
    # check types by:
        # >>> type(rec_t)
        # >>> type(time[0])
    fig = plt.figure()
    plt.plot(times[0], voltages[0])
    plt.title("Hello World")
    plt.xlabel("Time [ms]")
    plt.ylabel("Voltage [mV]")
    plt.axis(ymin=-90, ymax=50)
    plt.show()
    #plt.savefig('demo.png')

# Test End

def my_event_handler(p_process_list,timings):
	for i in range(len(p_process_list)):
		p_process_list[i].event(timings[i])


SustainedFiringmulti_PSO()