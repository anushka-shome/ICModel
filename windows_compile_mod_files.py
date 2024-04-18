# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 13:53:29 2015

@author: Uri Cohen (Adapted by BSC)
"""
import os
def windows_compile_mod_files(model_dir):
        #s1=os.environ['NEURONHOME']
        #s2=os.environ['NEURONHOME']
        s1="C:\\Python27\\neuronhome"
        s2="C:\\Python27\\neuronhome"
        s1u=s1.replace('\\', '/')
        s2u=s2.replace('\\', '/')
        model_diru=model_dir.replace('\\', '/')
        cmd=s1+"\\bin\\bash.exe"
        arg="cd "+model_diru+";"+s1u+"/bin/sh -c '" + s2u + "/lib/mknrndll.sh " + s2u + "'"
        import subprocess
        subprocess.Popen([cmd, '-c', arg], stdin=subprocess.PIPE).communicate(input="\r\n")
model_dir = "C:\\Users\\Alex\\repos\\temporal-swarm-model\\"    
#model_dir = "C:\\neuron_mechanism"
windows_compile_mod_files(model_dir)
