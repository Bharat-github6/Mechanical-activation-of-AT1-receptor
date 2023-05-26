#!/usr/bin/env python

from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator,MultipleLocator
from matplotlib.ticker import AutoMinorLocator
from matplotlib.patches import Rectangle
#from pandas import rolling_mean
import pandas as pd 
import numpy as np
import matplotlib

params = {'legend.fontsize': 20,
          'legend.handlelength': 5}

matplotlib.rc('xtick', labelsize=11)
matplotlib.rc('ytick', labelsize=11)
#use('Agg')
font = {'family' : 'sans serif', 'size' : '10'}
rc('font', **font)
mathfont = {'fontset' : 'stix' ,'default' : 'it', 'it' : 'serif:italic'}
rc('mathtext', **mathfont)
rc('lines', linewidth=0.9)

simplify = {'simplify_threshold' : '0.5'}
rc('path', **simplify)


apo_ss=pd.read_csv('ICL2_apo.xvg', delim_whitespace=True, comment='#')
apo_ss.columns=['time', 'structure', 'coil','B-bridge', 'Bend', 'Turn', 'A_Helix','Th_Helix']
th=apo_ss[['Th_Helix']]
a=apo_ss[['A_Helix']]
apo=pd.concat([a,th]).mean(axis=1)/11


angii_ss=pd.read_csv('ICL2_angii.xvg', delim_whitespace=True, comment='#')
angii_ss.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']
th1=angii_ss[['Th_Helix']]
a1=angii_ss[['A_Helix']]
angii=pd.concat([a1,th1]).mean(axis=1)/11


st10_ss=pd.read_csv('ICL2_st10.xvg', delim_whitespace=True, comment='#')
st10_ss.columns=['time', 'structure', 'coil','B-bridge', 'Bend', 'Turn', 'A_Helix','Th_Helix']
th2=st10_ss[['Th_Helix']]
a2=st10_ss[['A_Helix']]
st10=pd.concat([a2,th2]).mean(axis=1)/11

time=np.linspace(0,20, len(apo))
#print(st10)

plt.figure(figsize=(10,7))
window=15
plt.plot(time, apo.rolling(window).mean(), color='tab:blue', label='SOPC')
plt.plot(time, st10.rolling(window).mean(), color='tab:green', label='SOPC + 10 mN/m')
plt.plot(time, angii.rolling(window).mean(), color='tab:red', label='SOPC + AngII')
plt.axhline(y=0.66, linestyle='--', lw=1.5, color='tab:orange')
plt.axhline(y=0.0, linestyle='--', lw=1.5, color='0.5')
plt.xlabel('Time  ($\mu$s)', fontsize=12)
plt.ylabel(r'ICL2 $\alpha$-helicity, $f_{\alpha}$', fontsize=12)
plt.legend(loc='best')
#plt.close()
plt.savefig('Figure_9_supp.png', dpi=600)
plt.close()
