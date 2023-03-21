from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator,MultipleLocator
from matplotlib.ticker import AutoMinorLocator
#from pandas import rolling_mean
import pandas as pd
import numpy as np
import matplotlib

params = {'legend.fontsize': 20,
          'legend.handlelength': 5}

matplotlib.rc('xtick', labelsize=13)
matplotlib.rc('ytick', labelsize=13)
#use('Agg')
font = {'family' : 'sans serif', 'size' : '10'}
rc('font', **font)
mathfont = {'fontset' : 'stix' ,'default' : 'it', 'it' : 'serif:italic'}
rc('mathtext', **mathfont)
rc('lines', linewidth=0.9)

simplify = {'simplify_threshold' : '0.5'}
rc('path', **simplify)

sopc_apo=pd.read_csv('data/sopc_apo', delim_whitespace=True)
sopc_apo.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2', 'TM6-H8', 'n', 'n']

popc_apo=pd.read_csv('data/popc_apo', delim_whitespace=True)


popc_apo.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2', 'TM6-H8', 'n', 'n']



sopc_apo_anton=pd.read_csv('data/sopc_apo_anton', delim_whitespace=True)
sopc_apo_anton.columns=['time', 'TM1-TM6', 'TM1-ICL2','TM5-ICL2', 'TM6-H8', 'TM3-TM6', 'TM3-TM6-ASP241','n', 'n']
time=np.linspace(0,1000, len(sopc_apo_anton))



ax=plt.subplot(2,1,1)
time_popc=np.linspace(0,1000, len(popc_apo))
time_sopc=np.linspace(0,1000, len(sopc_apo))
plt.plot(time_sopc, sopc_apo[['TM1-TM6']].rolling(20).mean()*10, color='tab:blue', label='Apo AT1R in SOPC (replica 1)')
plt.plot(time, sopc_apo_anton[['TM1-TM6']].rolling(10).mean()*10, color='tab:red', label='Apo AT1R in SOPC (replica 2)' )
plt.plot(time_popc, popc_apo[['TM1-TM6']].rolling(20).mean()*10,color='tab:green', label='Apo AT1R in POPC')
plt.text(-110, 37,'a', weight='bold', fontsize=15)
plt.xlim(0,1000)
plt.ylim(16, 36)
plt.axhline(y=19.70, linestyle='--', color='grey', lw=2)
plt.axhline(y=33, linestyle='--', color='tab:orange', lw=2)
plt.legend(frameon=False)
plt.ylabel('TM1-TM6 $   (\AA$)', fontsize=15)
plt.xlabel('Time (ns)', fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(2))


sopc_ang=pd.read_csv('data/sopc_ang', delim_whitespace=True)
sopc_ang.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2', 'TM6-H8', 'n', 'n']


sopc_st15=pd.read_csv('data/sopc_st15', delim_whitespace=True)
sopc_st15.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2', 'TM6-H8', 'n', 'n']
time_angii=np.linspace(0,1000, len(sopc_ang))
time_st15=np.linspace(0,1000, len(sopc_st15))

ax=plt.subplot(2,1,2)
plt.plot(time_angii, sopc_ang[['TM1-TM6']].rolling(10).mean()*10, color='tab:blue', label='AT1R + AngII in SOPC')
plt.plot(time_st15, sopc_st15[['TM1-TM6']].rolling(100).mean()*10,color='tab:green', label='Apo AT1R in SOPC + 15 mN/m')
plt.xlim(0,1000)
plt.ylim(16, 36)
plt.axhline(y=19.70, linestyle='--', color='grey', lw=2)
plt.axhline(y=33, linestyle='--', color='tab:orange', lw=2)
plt.legend(frameon=False)
plt.ylabel('TM1-TM6 $   (\AA$)', fontsize=15)
plt.xlabel('Time (ns)', fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.text(-110, 37,'b', weight='bold', fontsize=15)
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(2))

fig = plt.gcf()
plt.subplots_adjust(top=0.92, bottom=0.1, left=0.12, right=0.95, hspace=0.3, wspace=0.0)
plt.Figure.set_size_inches(fig,(5, 7.5))
plt.savefig('Figure_S1.png', dpi=900)

