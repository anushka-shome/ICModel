# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 14:16:25 2015

@author: Brandon S Coventry       Purdue CAP Lab
Purpose: IC Model for Python
Revision History: None
"""
#def loadspikes():
#def loadspikes(numE,numI,rpE,rpI,nclistA,nclistB,nclistC,nclistD):
#    from neuron import *
#    from nrn import *
#    import numpy as np
#    import pdb
#    pdb.set_trace()
#    numE = 1
#    numI = 1
#    for jj in range(numE):
#        if rpE[jj].size()>0:
#            numss = rpE[jj].size()
#            for ii in range(numss):
#                h.nclistA.o(jj).event((rpE[jj].x[ii]+200))
#                h.nclistB.o(jj).event((rpE[jj].x[ii]+200))
#    for nn in range(numI):
#        if rpI[nn].size()>0:
#            numsI = rpI[jj].size()
#            for mm in range(numsI):
#                h.nclistC.o(nn).event((rpI[nn].x[mm]+200))
#                h.nclistD.o(nn).event((rpI[nn].x[mm]+200))
                
def SustainedFiring(numE,numI,OUnoise,networkcheck,rndseed,drvinputsE,drvIinputs,appdtau,gppdtau,gtau,gscale,nmdavdep,mempot,biascur,Neurotransvec,ampatau1,ampatau2,nmdatau1,nmdatau2,gabatau1,gabatau2):
    from neuron import *
    from nrn import *
    import numpy as np
    import pdb
    from InputPSTHs import *
    #h.nrn_load_dll('C:\\Python27\\neuronhome\\nrnmech.dll')
    #Begin with initialization of soma
    soma = h.Section()
    soma.nseg = 1
    soma.Ra = 150
    soma.L = 32.65
    soma.diam = 32.65
    soma.cm = 1
    
    soma.insert('pas')
    soma.g_pas = .00019
    soma.e_pas = -70
    
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
    #Initiate run
    rec_t = h.Vector()
    rec_t.record(h._ref_t)
    rec_v = h.Vector()
    rec_v.record(soma(0.5)._ref_v)
    h.finitialize()
    run(tstop)
#    rpE = []
#    rpI = []
#    aD = []
#    bD = []
#    cD = []
#    dD = []
#    #pdb.set_trace()
#    h('objref nil')
#    #if drvinputsE.any():
#    #h("objref rpE[1]")          #Will need to fix this for non lumped inputs
#    #h("objref rpI[1]") 
#    h('objref nclistA')
#    h('objref nclistB')
#    h('objref nclistC')
#    h('objref nclistD')
#    h('nclistA = new List()')
#    h('nclistB = new List()')
#    h('nclistC = new List()')
#    h('nclistD = new List()')
#    #h("objref aD[1]")
#    #h("objref bD[1]")
#    #h("objref cD[1]")
#    #h("objref dD[1]")
#    ampaconduct = Neurotransvec[0]
#    nmdaconduct = Neurotransvec[1]
#    gabaaconduct = Neurotransvec[2]
#    gababconduct = Neurotransvec[3]
#    #pdb.set_trace()
#    #drvinputsE = np.array([22.54, 23.09, 84.72, 109.02, 130.21, 165.97])
#    #drvIinputs = np.array([26.61, 43.27, 191.95])
#    for iii in range(numE):
#        rpE.append(h.Vector())
#        rpE[iii].from_python(drvinputsE)
#        #if drvinputsE.any():
#        #pdb.set_trace()
#        #h("rpE[0] = h.Vector()")
#        #h("rpE[0].from_python(drvinputsE)")
#        #numspiking = h.rpE[iii].size()
#        #aD[iii] = h.AMPA_LL_IC(0.5)
#        #aD[iii].tau1 = ampatau1
#        #aD[iii].tau = ampatau2
#        aD.append(h.AMPA_LL_IC(0.5))
#        aD[iii].tau1 = ampatau1
#        aD[iii].tau = ampatau2
#        nctempA = h.NetCon(h.nil,aD[iii],0,1,(ampaconduct))
#        h.nclistA.append(nctempA)
#        #bD[iii] = h.NMDA_LL_IC_2(0.5)
#        #bD[iii].vdepscale = nmdavdep
#        #bD[iii].tau1 = nmdatau1
#        #bD[iii].tau = nmdatau2
#        bD.append(h.NMDA_LL_IC_2(0.5))
#        bD[iii].vdepscale = nmdavdep
#        bD[iii].tau1 = nmdatau1
#        bD[iii].tau = nmdatau2
#        nctempB = h.NetCon(h.nil,bD[iii],0,1,(nmdaconduct))
#        h.nclistB.append(nctempB)
#    for iiii in range(numI):
#        rpI.append(h.Vector())
#        rpI[iiii].from_python(drvIinputs)
#        #if drvIinputs.any():
#        #h("rpI[0] = h.Vector()")
#        #rpI.append(h.Vector())
#        #h("rpI[iiii].from_python(drvIinputs)")
#        #numspikingI = h.rpI[iiii].size()
#        #cD[iiii] = h.ICGABAa(0.5)
#        #cD[iiii].tau1 = gabatau1
#        #cD[iiii].tau = gabatau2
#        #cD[iiii].scale = gscale
#        cD.append(h.ICGABAa(0.5))
#        cD[iiii].tau1 = gabatau1
#        cD[iiii].tau = gabatau2
#        cD[iiii].scale = gscale
#        nctempC = h.NetCon(h.nil,cD[iiii],0,1,(gabaaconduct))
#        h.nclistC.append(nctempC)
#        #h.dD[iiii] = h.ICGABAb3(0.5)
#        dD.append(h.ICGABAb3(0.5))
#        nctempD = h.NetCon(h.nil,dD[iiii],0,1,(gababconduct))
#        h.nclistD.append(nctempD)
#    #pdb.set_trace()
#    fih2 = h.FInitializeHandler((loadspikes, (numE,numI,rpE,rpI,h.nclistA,h.nclistB,h.nclistC,h.nclistD)))
##    for jj in range(numE):
##        if len(rpE)>0:
##            print('Made it here')
##            numss = len(rpE[jj])
##            for ii in range(numss):
##                h('nclistA.o(jj).event((rpE[jj].x[ii]+200))')
##                h('nclistB.o(jj).event((rpE[jj].x[ii]+200))')
#    #Initiate run
#    rec_t = h.Vector()
#    rec_t.record(h._ref_t)
#    rec_v = h.Vector()
#    rec_v.record(soma(0.5)._ref_v)
#    #pdb.set_trace()
#    h.finitialize()
#    run(tstop)
    
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
    #fig = plt.figure()
    #plt.plot(times[0], voltages[0])
    #plt.title("Hello World")
    #plt.xlabel("Time [ms]")
    #plt.ylabel("Voltage [mV]")
    #plt.axis(ymin=-90, ymax=50)
    #plt.show()
    return [times, voltages]
#def loadspikes(numE,numI,rpE,rpI,nclistA,nclistB,nclistC,nclistD):
