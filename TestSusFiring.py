# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:15:58 2015

@author: labadmin
"""
#def #loadspikes():
def loadspikes(numE,numI,rpE,rpI,nclistA,nclistB,nclistC,nclistD):
    from neuron import *
    from nrn import *
    import numpy as np
    import pdb
    pdb.set_trace()
    numE = 1
    numI = 1
    for jj in range(numE):
        if len(rpE)>0:
            numss = len(rpE[jj])
            for ii in range(numss):
                h.nclistA.o(jj).event((rpE[jj].x[ii]+200))
                h.nclistB.o(jj).event((rpE[jj].x[ii]+200))
    for nn in range(numI):
        if len(rpI)>0:
            numsI = len(rpI[jj])
            for mm in range(numsI):
                h.nclistC.o(nn).event((rpI[nn].x[mm]+200))
                h.nclistD.o(nn).event((rpI[nn].x[mm]+200))
from neuron import *
from nrn import *
import numpy as np
import pdb
#from testloadspikes import loadspikes
    #h.nrn_load_dlusFiringl('C:\\Python27\\neuronhome\\nrnmech.dll')
    #Begin with initialization of soma
numE = 1
numI = 1
OUnoise = [0.000935, 0.0005, 0.0008891, 0.0005, 2, 10]
networkcheck = 0
rndseed = 45
drvinputsE = np.array([22.54, 23.09, 84.72, 109.02, 130.21, 165.97])
drvIinputs = np.array([26.61, 43.27, 191.95])
appdtau = 25.42
gppdtau = 16.850918000000004
gtau = 15
gscale = 1.9055616465621483
nmdavdep = 35.7
mempot = -60
biascur = 0.065
Neurotransvec = [6.650000000004, 4.08000000001, 3.62999999999, 0]
ampatau1 = 0.5464
ampatau2 = 6
nmdatau1 = 32
nmdatau2 = 50
gabatau1 = 3
gabatau2 = 15
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
################################ 20220126 ?
#fih2 = h.FInitializeHandler((loadspikes, (numE,numI,rpE,rpI,h.nclistA,h.nclistB,h.nclistC,h.nclistD)))
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
    
#def loadspikes(numE,numI,rpE,rpI,nclistA,nclistB,nclistC,nclistD):
#def loadspikes():
#    from neuron import *
#    from nrn import *
#    import numpy as np
#    import pdb
#    numE = 1
#    numI = 1
#    for jj in range(numE):
#        if len(rpE)>0:
#            numss = len(rpE[jj])
#            for ii in range(numss):
#                h.nclistA.o(jj).event((rpE[jj].x[ii]+200))
#                h.nclistB.o(jj).event((rpE[jj].x[ii]+200))
#    for nn in range(numI):
#        if len(rpI)>0:
#            numsI = len(rpI[jj])
#            for mm in range(numsI):
#                h.nclistC.o(nn).event((rpI[nn].x[mm]+200))
#                h.nclistD.o(nn).event((rpI[nn].x[mm]+200))

