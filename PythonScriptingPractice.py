#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 23:16:39 2023

@author: anushkashome
"""

from neuron import h
from neuron.units import mV, ms, um
import matplotlib.pyplot as plt
import math
import plotly.io as pio
import plotly.express as px
import matplotlib.pyplot as plt
pio.renderers.default='browser'
h.load_file("stdrun.hoc")

import cProfile

cProfile.run("IC_SAM_Control.py")



'''
Etype = input("EnterNum ")
Etype = int(Etype)
#Etype = 1
if Etype == 1:
    print("1")
else:
    print("No")
    '''

'''
for seg in soma :
    print(seg, seg.area())
    
#Different properties in each segment
soma(0.5).diam = 20 * um

papic = h.Section(name="proxApical")
apic1 = h.Section(name="apic1")
apic2 = h.Section(name="apic2")
pb = h.Section(name="proxBasal")

papic.connect(soma)
pb.connect(soma(0))
apic1.connect(papic)
apic2.connect(papic)

h.topology()

class Pyramidal:
    def __init__(self):
        self.soma = h.Section(name="soma")
        self.soma.L = self.soma.diam = 10

pyrs = [Pyramidal() for i in range(1000)]

class Cell:
    def __init__(self):
        main = h.Section(name="main")
        dend1 = h.Section(name="dend1")
        dend2 = h.Section(name="dend2")
        main.diam = 10
        dend1.diam = dend2.diam = 2
        dend1.connect(main)
        dend2.connect(main)
        
        #store sections
        self.main = main; self.dend1 = dend1; self.dend2 = dend2
        self.all = main.wholetree()
        
my_cell = Cell()
my_cell.main.v = 50
my_cell.dend1.v = 0
my_cell.dend2.v = -65

ps = h.PlotShape(False)
ps.variable("v")
ps.scale(-80, 80)
ps.plot()
#ps = h.PlotShape(False)
#ps.plot(plotly).show()
#ps.printfile("practicecellgraph.eps")
'''

'''
import IC_SustainedFiring
from IC_SustainedFiring import IC_SustainedFiring

ICCell = IC_SustainedFiring()
'''