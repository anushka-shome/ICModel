#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:26:44 2024

@author: anushkashome
"""

from neuron import h
import numpy as np
from neuron.units import ms, mV
import neuron
hl = neuron.hoc.HocObject()
import pdb
h.load_file("stdrun.hoc")
import pandas as pd
import matplotlib.pyplot as plt
h.nrn_load_dll("/Users/anushkashome/Practice/arm64/special/Isodium.o")
class IC_AdaptedFiring(object):
    """
    Init class sets up the model and sets variables. Inputs are in description above. 
    """
    def __init__(self, numE=1,numI=1,OUNoise=[0,0,0,0,0,0],drvinputsE = [],drvIinputs=[],gscale=1,nmdavdep = 0,biascur=0.065,Neurotransvec=[100,100,100,0],ampatau1=0,ampatau2=0,nmdatau1=0,nmdatau2=0,gabatau1=0,gabatau2=0,rndseed=0.7254):
        super(IC_AdaptedFiring, self).__init__()
        #Super will become important when using networks of IC cells with this class.
        #Set variables so that any class function can access them.
        self.numE = numE
        self.numI = numI
        self.OUNoise = OUNoise
        self.drvinputsE = drvinputsE
        self.drvIinputs = drvIinputs
        self.gscale = gscale
        self.nmdavdep = nmdavdep
        self.biascur = biascur
        self.Neurotransvec = Neurotransvec
        self.ampatau1 = ampatau1
        self.ampatau2 = ampatau2
        self.nmdatau1 = nmdatau1
        self.nmdatau2 = nmdatau2
        self.gabatau1 = gabatau1
        self.gabatau2 = gabatau2
        self.rndseed = rndseed
        #Build the model!
        #Begin with initialization of soma
        self.soma = h.Section()
        self.soma.nseg = 1
        self.soma.Ra = 150
        self.soma.L = 34.5 #or 10.9099
        self.soma.diam = 34.5 
        self.soma.cm = 1
        
        #Passive flux channels
        self.soma.insert('pas')
        self.soma.g_pas = .0000149 #conductance
        self.soma.e_pas = -70
        
        #Na channel
        self.soma.insert('Isodium')
        self.soma.ena = 50 # reversal potential
        self.soma.vtraub_Isodium = -52 
        self.soma.gnabar_Isodium = 0.2 # max. conductance
        
        '''
        #Low threshold K channel
        self.soma.insert('kLT_VCN2003')
        self.soma.gkbar_kLT_VCN2003 = 0
        #soma.ek_kLT_VCN2003 = -90        #Change in mod code
        '''
        '''
        #High threshold K channel
        self.soma.insert('kHT_VCN2003')
        self.soma.gkbar_kHT_VCN2003 = 0
        #soma.ek_kHT_VCN2003 = -90        #Change in mod code
        '''
        
        #Delayed-rectifier k channel
        self.soma.insert('kdr')
        self.soma.gbar_kdr = 0.1
        #soma.ek_kdr = -90                #Changed in mod code
        
        '''
        #TEA-sensitive K channel
        self.soma.insert('kdrtea')
        #soma.ek_kdrtea=-90               #Changed in mod code
        '''
        
        self.soma.insert('ik2')
        #soma.ek_ik2=-90                  #Changed in mod code
        self.soma.gbar_ik2 = 0
        
        self.soma.insert('hsus')
        self.soma.eh_hsus = -40
        self.soma.gh_hsus = 0
        self.soma.ek = -90
        
        self.soma.insert('CaLT')
        
        self.soma.insert('CaHT')
        
        self.soma.insert('HCN')
        
        self.soma.insert('KCa')
        
        #Insert point process mechanisms
        #Set resting mem potential
        self.hold = h.IClamp(self.soma(0.5))
        self.hold.delay = 0
        self.hold.amp = self.biascur
        self.hold.dur = 1000
        #h.tstop = 2000
        #h.run()
        
        self.stim = h.IClamp(self.soma(0.5))           #This is here to test model
        self.stim.delay = 0
        self.stim.amp = 0.5
        self.stim.dur = 100
        
        #Insert OUNoise process
        self.f1 = h.Gfluct2(0.5)
        self.f1.g_e0 = self.OUNoise[0]
        self.f1.g_i0 = self.OUNoise[1]
        self.f1.std_e = self.OUNoise[2]
        self.f1.std_i = self.OUNoise[3]
        self.f1.tau_e = self.OUNoise[4]
        self.f1.tau_i = self.OUNoise[5]
        self.f1.new_seed(self.rndseed)
        
        #Run parameters
        self.trans = 0
        h.dt = 0.02
        self.Dt = 0.02
        self.npoints=50000
        self.tstart = self.trans
        self.tstop = self.trans + self.Dt*self.npoints
        self.v_init = -60
        h.celsius = 34
        self.steps_per_ms = 1/self.Dt
        
        '''
        #Graphing iClamp
        v = h.Vector().record(self.soma(0.5)._ref_v) #MP
        t = h.Vector().record(h._ref_t) #Time
        h.finitialize(-65*mV)
        h.continuerun(150 * ms)
        v_np = np.array(list(v))
        t_np = np.array(list(t))
        print(v_np)
        print(t_np)
        plt.figure()
        plt.plot(t_np, v_np)
        plt.xlabel("Time(ms)")
        plt.ylabel("Membrane Potential(mV)")
        plt.show()   
        '''

    def loadInputs(self,drvinputsE,drvIinputs):
        """
        Just a helper function that loads spike time vectors
        """
        self.drvIinputs = drvIinputs
        self.drvinputsE = drvinputsE

    def loadspikes(self,numE,numI,rpE,rpI,nclistA,nclistB,nclistC,nclistD):
        """
        This is a helper function to load synaptics
        """
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

    def setSynaptics(self,drvinputsE,drvIinputs):
        """
        This sets up the synaptics, taking in input spike timing vectors. This will need to be reset each run as synaptics vary, hence this helper function. 
        """
        self.drvinputsE = drvinputsE
        self.drvIinputs = drvIinputs
        #Hook up synaptic conductances    
        #Begin with excitatory
        rpE = []
        rpI = []
        aD = []
        bD = []
        cD = []
        dD = []
        #We use the h('') to easily set vectors in NEURON
        
        hl('objref nil')
        hl('objref nclistA')
        hl('objref nclistB')
        hl('objref nclistC')
        hl('objref nclistD')
        hl('nclistA = new List()')
        hl('nclistB = new List()')
        hl('nclistC = new List()')
        hl('nclistD = new List()')
        pdb.set_trace()
        if len(self.drvinputsE) > 0:
            hl('objref rpE[self.numE]')
        else:
            hl('objref rpE')
        if len(self.drvIinputs) > 0:
            hl('objref rpI[self.numI]')
        else:
            hl('objref rpI')
        hl('objref nclistA')
        hl('objref nclistB')
        hl('objref nclistC')
        hl('objref nclistD')
        hl('nclistA = new List()')
        hl('nclistB = new List()')
        hl('nclistC = new List()')
        hl('nclistD = new List()')
        hl('double aD[self.numE]')
        hl('double bD[self.numE]')
        hl('double cD[self.numI]')
        hl('double dD[self.numI]')
        ampaconduct = self.Neurotransvec[0]
        nmdaconduct = self.Neurotransvec[1]
        gabaaconduct = self.Neurotransvec[2]
        gababconduct = self.Neurotransvec[3]
        #pdb.set_trace()
        for iii in range(self.numE):
            #if drvinputsE.any():
            rpE.append(h.Vector())
            rpE[iii].from_python(self.drvinputsE)
            numspiking = rpE[iii].size()
            aD.append(h.AMPA_LL_IC(0.5))
            aD[iii].tau1 = self.ampatau1
            aD[iii].tau = self.ampatau2
            nctempA = h.NetCon(h.nil,aD[iii],0,1,(ampaconduct))
            h.nclistA.append(nctempA)
            bD.append(h.NMDA_LL_IC_2(0.5))
            bD[iii].vdepscale = self.nmdavdep
            bD[iii].tau1 = self.nmdatau1
            bD[iii].tau = self.nmdatau2
            nctempB = h.NetCon(h.nil,bD[iii],0,1,(nmdaconduct))
            h.nclistB.append(nctempB)
        for iiii in range(self.numI):
            #if drvIinputs.any():
            rpI.append(h.Vector())
            rpI[iiii].from_python(self.drvIinputs)
            numspikingI = rpI[iiii].size()
            cD.append(h.ICGABAa(0.5))
            cD[iiii].tau1 = self.gabatau1
            cD[iiii].tau = self.gabatau2
            cD[iiii].scale = self.gscale
            nctempC = h.NetCon(h.nil,cD[iiii],0,1,(gabaaconduct))
            h.nclistC.append(nctempC)
            dD.append(h.ICGABAb3(0.5))
            nctempD = h.NetCon(h.nil,dD[iiii],0,1,(gababconduct))
            h.nclistD.append(nctempD)
        #pdb.set_trace()   
        fih2 = h.FInitializeHandler((self.loadspikes, (self.numE,self.numI,rpE,rpI,h.nclistA,h.nclistB,h.nclistC,h.nclistD)))
    
    def run(self):
        """
        This helper class initiates a run of the model and outputs resultant times and voltages. Automatically stores into lists. 
        Note: Should only run after setSynaptics has been set atleast once.
        """
        #Initiate run
        rec_t = h.Vector()
        rec_t.record(h._ref_t)
        rec_v = h.Vector()
        rec_v.record(self.soma(0.5)._ref_v)
        h.finitialize()
        h.continuerun(self.tstop)
        times = [] # Use list to add another trace later.
        voltages = []
        times.append(list(rec_t)) # alternativ to `list(rec_t)`: `numpy.array(rec_t)`
        voltages.append(list(rec_v))
        return [times,voltages]
    
    def setRNDSeed(self,rndseed):
        """
        Helper function that sets the rand seed
        """
        self.rndseed = rndseed
    
    def loadSpikeTimes(self,drvinputsE,drvIinputs):
        ampaconduct = self.Neurotransvec[0]
        nmdaconduct = self.Neurotransvec[1]
        gabaaconduct = self.Neurotransvec[2]
        gababconduct = self.Neurotransvec[3]
        rpE = h.Vector(drvinputsE)
        rpI = h.Vector(drvIinputs)
        aD = []
        bD = []
        cD = []
        dD = []
        aD = h.AMPA_LL_IC(self.soma(0.5))
        aD.tau1 = self.ampatau1
        aD.tau = self.ampatau2
        bD = h.NMDA_LL_IC_2(self.soma(0.5))
        bD.vdepscale = self.nmdavdep
        bD.tau1 = self.nmdatau1
        bD.tau = self.nmdatau2
        cD = h.ICGABAa(self.soma(0.5))
        cD.tau1 = self.gabatau1
        cD.tau = self.gabatau2
        cD.scale = self.gscale
        try:
            vsEx = h.VecStim()
            vsIn = h.VecStim()
        except AttributeError:
        # note: the current version of vecevent.mod is always available from:
        # https://raw.githubusercontent.com/neuronsimulator/nrn/master/share/examples/nrniv/netcon/vecevent.mod
            raise Exception(
                "h.VecStim is not defined; did you forget to include and compile vecevent.mod?"
            )
        vsEx.play(rpE)
        vsIn.play(rpI)
        ncAMPA = h.NetCon(vsEx, aD,0,1,(ampaconduct))
        ncNMDA = h.NetCon(vsEx, bD,0,1,(nmdaconduct))
        ncGABAA = h.NetCon(vsIn, cD,0,1,(gabaaconduct))
        rec_t = h.Vector()
        rec_t.record(h._ref_t)
        rec_v = h.Vector()
        rec_v.record(self.soma(0.5)._ref_v)
        h.finitialize(-65*mV)
        h.continuerun(self.tstop)
        times = [] # Use list to add another trace later.
        voltages = []
        times.append(list(rec_t)) # alternativ to `list(rec_t)`: `numpy.array(rec_t)`
        voltages.append(list(rec_v))
        return [times,voltages]