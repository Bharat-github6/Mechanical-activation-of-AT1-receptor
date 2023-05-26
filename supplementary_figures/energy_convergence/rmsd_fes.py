from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import AutoMinorLocator
#from pandas import rolling_mean
import pandas as pd
import numpy as np
import matplotlib

params = {'legend.fontsize': 20,
          'legend.handlelength': 5}

matplotlib.rc('xtick', labelsize=15)
matplotlib.rc('ytick', labelsize=15)
#use('Agg')
font = {'family' : 'sans serif', 'size' : '10'}
rc('font', **font)
mathfont = {'fontset' : 'stix' ,'default' : 'it', 'it' : 'serif:italic'}
rc('mathtext', **mathfont)
rc('lines', linewidth=1.2)
#rc('text', usetex=True)
simplify = {'simplify_threshold' : '0.5'}
rc('path', **simplify)

plt.figure(figsize=(10,5))
popc=np.loadtxt('data/rmsd_data/popc.dat')
st10=np.loadtxt('data/rmsd_data/st10.dat')
angii=np.loadtxt('data/rmsd_data/angii.dat')
apo=np.loadtxt('data/rmsd_data/sopc_apo.dat')
partial_ag=np.loadtxt('data/rmsd_data/s1i8.dat')
pe=np.loadtxt('data/rmsd_data/sopc_sope.dat')
plt.plot(popc[:,0]*0.008,popc[:,1]/4.2, label='AT1R (POPC)')
plt.plot(partial_ag[:,0]*0.008,partial_ag[:,1]/4.2, label='AT1R + S1I8 (SOPC)')
plt.plot(angii[:,0]*0.008,angii[:,1]/4.2, label='AT1R + AngII (SOPC)')
plt.plot(st10[:,0]*0.008,st10[:,1]/4.2, label='AT1R + 10 mN/m (SOPC)')
plt.plot(apo[:,0]*0.008,apo[:,1]/4.2, label='AT1R (SOPC)')
plt.plot(pe[:,0]*0.008,pe[:,1]/4.2, label='AT1R (SOPC+SOPE)')
plt.legend(fontsize=15,frameon=False)
plt.ylabel('$F$ RMSD (kcal/mol)', fontsize=18)
plt.xlabel('Time (ns)', fontsize=18)
plt.yticks([0,1,2,3,4], fontsize=15)
plt.xticks(fontsize=15)
plt.savefig('Figure_S12.png', bbox_inches='tight', dpi=300)
