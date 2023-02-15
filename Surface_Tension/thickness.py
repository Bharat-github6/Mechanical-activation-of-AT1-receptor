#!/usr/bin/env python

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

#illustr = plt.imread('SOPC-SOPE.png')



x_label=['0','5','10','15','20']
x=[0,5,10,15,20]
st_thickness=[41.05,40.35,38.45,37.25,35.5]
thickness_err=[0.77,0.35,0.35,0.63,0.98]
y=[0,5,10]
popc=[38.2,37.5,36.5]
popc_thickness=38.2
dmpc_thickness=35.6
pe_pc_thickness=42.85
ax6=plt.subplot(1,1,1)
ax6.plot(x,st_thickness,marker='s',markersize=4,color='tab:blue', label='SOPC')
#ax6.plot(0,popc_thickness,marker='>',markersize=4, color='tab:green', label='POPC')
#ax6.plot(y,popc,marker='>',markersize=4, color='tab:green', label='POPC')
ax6.plot(0, popc[0], marker='v', markersize=4, color='tab:green', label='POPC')
ax6.plot(0,dmpc_thickness,marker='D', markersize=4,color='tab:red', label='DMPC')
ax6.plot(0,pe_pc_thickness,marker='o',markersize=4, color='grey', label='SOPC:SOPE')

plt.errorbar(x,st_thickness, yerr=thickness_err ,color='tab:blue')#
plt.errorbar(0,38.2, yerr=0.14, color='tab:green')
plt.errorbar(0,35.6, yerr=0.14,color='tab:red')
plt.errorbar(0,42.85, yerr=0.21,color='grey')
#plt.xticks(y,y_label)
plt.xticks(x,x_label)
plt.ylabel('Bilayer Thicknes', fontsize=10)
ax6.text(1.0,35.6, 'DMPC', color='tab:red', fontsize=11, fontweight='medium')
ax6.text(1.0,38.2, 'POPC', color='tab:green', fontsize=11, fontweight='medium')
ax6.text(12.5,40, 'SOPC', color='tab:blue', fontsize=11, fontweight='medium')
ax6.text(1.0,42.5, 'SOPC:SOPE', color='grey', fontsize=11, fontweight='medium')
ax6.set_ylim(33,44)
ax6.set_ylabel('Bilayer thickness ($\AA$)', fontsize=11)
ax6.xaxis.set_major_locator(MultipleLocator(5))
##ax4.yaxis.set_minor_locator(AutoMinorLocator(5))
ax6.yaxis.set_major_locator(MultipleLocator(2))
ax6.yaxis.set_minor_locator(AutoMinorLocator(2))
ax6.set_xlabel('Tension (mN/m)', fontsize=11)



#leg=ax1.legend(ncol=1,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(1.9,1.1), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

#for i in leg.legendHandles:
#    i.set_linewidth(2)




fig = plt.gcf()
#plt.subplots_adjust(top=0.92, bottom=0.115, left=0.1, right=0.975, hspace=0.43, wspace=0.5)

plt.subplots_adjust(top=0.96, bottom=0.2, left=0.17, right=0.96, hspace=0.4, wspace=0.2)
plt.Figure.set_size_inches(fig,(3, 2.5))

plt.savefig('thickness_sopc.png', dpi=300)
#plt.savefig('time_evolution.svg', dpi=900, bbox_inches='tight')
plt.close()
