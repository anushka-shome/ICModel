"""
Created on Mon June 14 3:14 P.m. 2015

Author: Brandon S Coventry Lauren Marussich
Purpose: Multicomp Python model
Revision History: Aug 18: Continued work. For future updates, see GIT
"""
def SustainedFiringmulti_PSO(numE,numI,OUnoise,networkcheck,rndseed,drvinputsE,drvIinputs,appdtau,gppdtau,gtau,gscale,nmdavdep,mempot,biascur,Neurotransvec,ampatau1,ampatau2,nmdatau1,nmdatau2,gabatau1,gabatau2):
    #Start by calling necessary packages
    from neuron import *
    from nrn import *
    import numpy as np
    import pdb
    from InputPSTHs import *
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
    #print('I made it here')
    #Insert point process mechanisms
    hold = h.IClamp(soma(0.5))
    hold.delay = 0
    hold.amp = 0.065                     #Change this to required vinit
    hold.dur = 1000
    
    stim = h.IClamp(soma(0.5))           #This is here to test model
    stim.delay = 0
    stim.amp = 0
    stim.dur = 0
    
    f1 = h.Gfluct2(0.5)
    f1.g_e0 = OUnoise[0]
    f1.g_i0 = OUnoise[1]
    f1.std_e = OUnoise[2]
    f1.std_i = OUnoise[3]
    f1.tau_e = OUnoise[4]
    f1.tau_i = OUnoise[5]
    f1.new_seed(rndseed)
    
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
    
    #Hook up synaptic conductances    
    #Begin with excitatory
    rpE = []
    rpI = []
    aD = []
    bD = []
    cD = []
    dD = []
    h('objref nil')
    h('objref nclistA')
    h('objref nclistB')
    h('objref nclistC')
    h('objref nclistD')
    h('nclistA = new List()')
    h('nclistB = new List()')
    h('nclistC = new List()')
    h('nclistD = new List()')
    if drvinputsE.any():
        h('objref rpE[drvinputsE]')
    else:
        h('objref rpE')
    if drvIinputs.any():
        h('objref rpI[drvIinputs]')
    else:
        h('objref rpI')
    h('objref nclistA')
    h('objref nclistB')
    h('objref nclistC')
    h('objref nclistD')
    h('nclistA = new List()')
    h('nclistB = new List()')
    h('nclistC = new List()')
    h('nclistD = new List()')
    h('aD[drvinputsE]')
    h('bD[drvinputsE]')
    h('cD[drvIinputs]')
    h('dD[drvIinputs]')
    ampaconduct = Neurotransvec[0]
    nmdaconduct = Neurotransvec[1]
    gabaaconduct = Neurotransvec[2]
    gababconduct = Neurotransvec[3]
    #pdb.set_trace()
    for iii in range(numE):
        #if drvinputsE.any():
        rpE.append(h.Vector())
        rpE[iii].from_python(drvinputsE)
        numspiking = rpE[iii].size()
        aD.append(h.AMPA_LL_IC(0.5))
        aD[iii].tau1 = ampatau1
        aD[iii].tau = ampatau2
        nctempA = h.NetCon(h.nil,aD[iii],0,1,(ampaconduct))
        h.nclistA.append(nctempA)
        bD.append(h.NMDA_LL_IC_2(0.5))
        bD[iii].vdepscale = nmdavdep
        bD[iii].tau1 = nmdatau1
        bD[iii].tau = nmdatau2
        nctempB = h.NetCon(h.nil,bD[iii],0,1,(nmdaconduct))
        h.nclistB.append(nctempB)
    for iiii in range(numI):
        #if drvIinputs.any():
        rpI.append(h.Vector())
        rpI[iiii].from_python(drvIinputs)
        numspikingI = rpI[iiii].size()
        cD.append(h.ICGABAa(0.5))
        cD[iiii].tau1 = gabatau1
        cD[iiii].tau = gabatau2
        cD[iiii].scale = gscale
        nctempC = h.NetCon(h.nil,cD[iiii],0,1,(gabaaconduct))
        h.nclistC.append(nctempC)
        dD.append(h.ICGABAb3(0.5))
        nctempD = h.NetCon(h.nil,dD[iiii],0,1,(gababconduct))
        h.nclistD.append(nctempD)
    #pdb.set_trace()   
    fih2 = h.FInitializeHandler((loadspikes, (numE,numI,rpE,rpI,h.nclistA,h.nclistB,h.nclistC,h.nclistD)))
#    for jj in range(numE):
#        if len(rpE)>0:
#            print('Made it here')
#            numss = len(rpE[jj])
#            for ii in range(numss):
#                h('nclistA.o(jj).event((rpE[jj].x[ii]+200))')
#                h('nclistB.o(jj).event((rpE[jj].x[ii]+200))')   
    rec_t = h.Vector()
    rec_t.record(h._ref_t)
    rec_v = h.Vector()
    rec_v.record(axon(0.5)._ref_v)
    h.finitialize()
    run(tstop)
    
    g = h.Graph()
    g.size(0, 5, -80, 20)
    rec_v.line(g, rec_t)
    import matplotlib.pyplot as plt

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