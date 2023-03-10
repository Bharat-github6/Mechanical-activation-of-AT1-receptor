#!/usr/bin/env python

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

#def V_phi(phi):
#    return 1.062736*(1+cos(2*radians(phi)-radians(60)))

sideview = plt.imread('Active_vs_inactive_side_view_chimera_w_labels_orange.png')
bottomview = plt.imread('Active_vs_inactive_bottom_view_chimera_w_labels_orange.png')

popc_r1= pd.read_csv('data/POPC/replica_1/Deer_analysis2us', delim_whitespace=True)
popc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
popc_r1=popc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

popc_r2= pd.read_csv('data/POPC/replica_2/Deer_analysis2us', delim_whitespace=True)
popc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
popc_r2=popc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

popc=pd.concat([popc_r1,popc_r2], axis=1)



dmpc_r1= pd.read_csv('data/DMPC/replica_1/Deer_analysis_2us', delim_whitespace=True)
dmpc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
dmpc_r1=dmpc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]


dmpc_r2= pd.read_csv('data/DMPC/replica_2/Deer_analysis2us', delim_whitespace=True)
dmpc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
dmpc_r2=dmpc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

dmpc=pd.concat([dmpc_r1, dmpc_r2], axis=1)


sopc_r1= pd.read_csv('data/SOPC/replica_1/Deer_analysis_2us', delim_whitespace=True)
sopc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
sopc_r1=sopc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]


sopc_r2= pd.read_csv('data/SOPC/replica_2/Deer_analysis2us', delim_whitespace=True)
sopc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
sopc_r2=sopc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
sopc=pd.concat([sopc_r1, sopc_r2], axis=1)


sopc_ssr1=pd.read_csv('data/SOPC/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
sopc_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']

sopc_ssr2=pd.read_csv('data/SOPC/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
sopc_ssr2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']

sopc_ssr1=sopc_ssr1[['A_Helix','Th_Helix', 'Fiv_Helix' ]].sum(axis=1)/11
sopc_ssr2=sopc_ssr2[['A_Helix','Th_Helix']].sum(axis=1)/11
sopc_ss=pd.concat([sopc_ssr1, sopc_ssr2], axis=1).mean(axis=1)
sopc_ss_err=(pd.concat([sopc_ssr1, sopc_ssr2], axis=1)).std(axis=1)
sopc_ss=sopc_ss[:400000]
sopc_ss_err=sopc_ss_err[:400000]


popc_ssr1=pd.read_csv('data/POPC/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
popc_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']


popc_ssr2=pd.read_csv('data/POPC/replica_2/ICL2.xvg', delim_whitespace=True, comment='#')
popc_ssr2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']

popc_ssr2=popc_ssr2[['A_Helix','Th_Helix', 'Fiv_Helix' ]].sum(axis=1)/11
popc_ssr1=popc_ssr1[['A_Helix','Th_Helix']].sum(axis=1)/11


dmpc_ssr1=pd.read_csv('data/DMPC/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
popc_ss=pd.concat([popc_ssr1, popc_ssr2], axis=1).mean(axis=1)
popc_ss_err=(pd.concat([popc_ssr1, popc_ssr2], axis=1)).std(axis=1)
popc_ss=popc_ss[:400000]
popc_ss_err=popc_ss_err[:400000]

dmpc_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']

dmpc_ssr2=pd.read_csv('data/DMPC/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
dmpc_ssr2.columns=['time', 'structure', 'coil','B_bridge', 'Bend', 'Turn', 'A_Helix','Fiv_Helix', 'Th_Helix']

dmpc_ssr2=dmpc_ssr2[['A_Helix','Th_Helix', 'Fiv_Helix' ]].sum(axis=1)/11
dmpc_ssr1=dmpc_ssr1[['A_Helix','Th_Helix']].sum(axis=1)/11
dmpc_ss=pd.concat([dmpc_ssr1, dmpc_ssr2], axis=1).mean(axis=1)
dmpc_ss_err=(pd.concat([dmpc_ssr1, dmpc_ssr2], axis=1)).std(axis=1)
dmpc_ss=dmpc_ss[:400000]
dmpc_ss_err=dmpc_ss_err[:400000]

time_ss_sopc=np.linspace(0,2000,len(sopc_ss))
time_ss_popc=np.linspace(0,2000,len(popc_ss))
time_ss_dmpc=np.linspace(0,2000,len(dmpc_ss))


fyay=[19.70,19.50,29.77,17.30]


exp=[33.48,25.57,23.65,22.56]



time_sopc=np.linspace(0,2000,len(sopc[['TM1-TM6']][:200000]))
time_popc=np.linspace(0,2000,len(popc[['TM1-TM6']][:200000]))
time_dmpc=np.linspace(0,2000,len(dmpc[['TM1-TM6']][:200000]))


window = 500

ax=plt.subplot(2,4,2)
ax.plot(time_popc,(popc[['TM1-TM6']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax.plot(time_dmpc,(dmpc[['TM1-TM6']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (DMPC)')
ax.plot(time_sopc,(sopc[['TM1-TM6']][:200000].mean(axis=1).rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
plt.fill_between(time_dmpc, (dmpc[['TM1-TM6']][:200000].mean(axis=1).rolling(window).mean()*10)-(dmpc[['TM1-TM6']][:200000].std(axis=1).rolling(window).mean()*10), (dmpc[['TM1-TM6']][:200000].mean(axis=1).rolling(window).mean()*10)+(dmpc[['TM1-TM6']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:red', alpha=0.1)
plt.fill_between(time_popc, (popc[['TM1-TM6']][:200000].mean(axis=1).rolling(window).mean()*10)-(popc[['TM1-TM6']][:200000].std(axis=1).rolling(window).mean()*10), (popc[['TM1-TM6']][:200000].mean(axis=1).rolling(window).mean()*10)+(popc[['TM1-TM6']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:green', alpha=0.1)
plt.fill_between(time_sopc, (sopc[['TM1-TM6']][:200000].mean(axis=1).rolling(window).mean()*10)-(sopc[['TM1-TM6']][:200000].std(axis=1).rolling(window).mean()*10), (sopc[['TM1-TM6']][:200000].mean(axis=1).rolling(window).mean()*10)+(sopc[['TM1-TM6']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:blue', alpha=0.1)
ax.axhline(y=32.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
#ax.legend(loc='best', fontsize=5)
ax.set_ylim(17,36)
ax.set_xlim(0,2000)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
ax.yaxis.set_major_locator(MaxNLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('TM1-TM6 Dist. ($\AA$)', fontsize=11)
ax.set_xlim(0,2000)
#ax.set_xlabel('Time (ns)', fontsize=11)
ax.set_xlabel('Time (ns)', fontsize=11)


ax1=plt.subplot(2,4,3)
ax1.plot(time_popc,(popc[['TM1-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax1.plot(time_dmpc,(dmpc[['TM1-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (DMPC)')
ax1.plot(time_sopc,(sopc[['TM1-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
plt.fill_between(time_dmpc, (dmpc[['TM1-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)-(dmpc[['TM1-ICL2']][:200000].std(axis=1).rolling(window).mean()*10), (dmpc[['TM1-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)+(dmpc[['TM1-ICL2']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:red', alpha=0.1)
plt.fill_between(time_popc, (popc[['TM1-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)-(popc[['TM1-ICL2']][:200000].std(axis=1).rolling(window).mean()*10), (popc[['TM1-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)+(popc[['TM1-ICL2']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:green', alpha=0.1)
plt.fill_between(time_sopc, (sopc[['TM1-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)-(sopc[['TM1-ICL2']][:200000].std(axis=1).rolling(window).mean()*10), (sopc[['TM1-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)+(sopc[['TM1-ICL2']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:blue', alpha=0.1)


ax1.axhline(y=19.50, linestyle='--', lw=1.5, color='0.5')
ax1.axhline(y=25.57, linestyle='--', lw=1.5, color='tab:orange')
ax1.set_ylim(17,27)
ax1.set_xlim(0,2000)
ax1.set_ylabel('TM1-ICL2 Dist. ($\AA$)', fontsize=11)
ax1.set_xlabel('Time (ns)', fontsize=11)
ax1.yaxis.set_major_locator(MaxNLocator(5))
ax1.yaxis.set_minor_locator(AutoMinorLocator(2))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax1.set_yticks([ 20, 25], minor=True)
#leg=ax1.legend(ncol=3,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(2.2,1.15), markerscale=8 ,columnspacing=1, handletextpad=1, handlelength=1, fontsize=15)

#for i in leg.legendHandles:
#    i.set_linewidth(3)

ax2=plt.subplot(2,4,4)
ax2.plot(time_popc,(popc[['TM5-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax2.plot(time_dmpc,(dmpc[['TM5-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (DMPC)')
ax2.plot(time_sopc,(sopc[['TM5-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
plt.fill_between(time_dmpc, (dmpc[['TM5-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)-(dmpc[['TM5-ICL2']][:200000].std(axis=1).rolling(window).mean()*10), (dmpc[['TM5-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)+(dmpc[['TM5-ICL2']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:red', alpha=0.1)
plt.fill_between(time_popc, (popc[['TM5-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)-(popc[['TM5-ICL2']][:200000].std(axis=1).rolling(window).mean()*10), (popc[['TM5-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)+(popc[['TM5-ICL2']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:green', alpha=0.1)
plt.fill_between(time_sopc, (sopc[['TM5-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)-(sopc[['TM5-ICL2']][:200000].std(axis=1).rolling(window).mean()*10), (sopc[['TM5-ICL2']][:200000].mean(axis=1).rolling(window).mean()*10)+(sopc[['TM5-ICL2']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:blue', alpha=0.1)
ax2.set_xlim(0,2000)
ax2.set_xlabel('Time (ns)', fontsize=11)
ax2.axhline(y=23.65, linestyle='--', lw=1.5, color='tab:orange')
ax2.axhline(y=29.77, linestyle='--', lw=1.5, color='0.5')
#ax2.text(0.15, 24, 'AT1R/-/-$_{Exp}$', ha='center', fontsize=9, fontname='sans-serif')
#ax2.text(-0.15, 30, 'AT1R/-/-$_{Exp}$', ha='center', fontsize=9, fontname='sans-serif')
ax2.set_ylim(21,32)
ax2.set_xlabel('Time (ns)', fontsize=11)
ax2.set_ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=11)
ax2.yaxis.set_major_locator(MaxNLocator(6))
ax2.yaxis.set_minor_locator(AutoMinorLocator(2))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax1.set_yticks([ 20, 25], minor=True)

ax3=plt.subplot(2,4,6)
ax3.plot(time_popc,(popc[['TM6-H8']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax3.plot(time_dmpc,(dmpc[['TM6-H8']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (DMPC)')
ax3.plot(time_sopc,(sopc[['TM6-H8']][:200000].mean(axis=1).rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
plt.fill_between(time_dmpc, (dmpc[['TM6-H8']][:200000].mean(axis=1).rolling(window).mean()*10)-(dmpc[['TM6-H8']][:200000].std(axis=1).rolling(window).mean()*10), (dmpc[['TM6-H8']][:200000].mean(axis=1).rolling(window).mean()*10)+(dmpc[['TM6-H8']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:red', alpha=0.1)
plt.fill_between(time_popc, (popc[['TM6-H8']][:200000].mean(axis=1).rolling(window).mean()*10)-(popc[['TM6-H8']][:200000].std(axis=1).rolling(window).mean()*10), (popc[['TM6-H8']][:200000].mean(axis=1).rolling(window).mean()*10)+(popc[['TM6-H8']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:green', alpha=0.1)
plt.fill_between(time_sopc, (sopc[['TM6-H8']][:200000].mean(axis=1).rolling(window).mean()*10)-(sopc[['TM6-H8']][:200000].std(axis=1).rolling(window).mean()*10), (sopc[['TM6-H8']][:200000].mean(axis=1).rolling(window).mean()*10)+(sopc[['TM6-H8']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:blue', alpha=0.1)

ax3.set_ylabel( 'TM6-H8 Dist. ($\AA$)', fontsize=11)
ax3.axhline(y=17.30, linestyle='--', lw=1.5, color='0.5')
ax3.axhline(y=22.56, linestyle='--', lw=1.5, color='tab:orange')
ax3.set_ylim(10,26)
ax3.set_xlim(0,2000)
ax3.set_xlabel('Time (ns)', fontsize=11)
#ax3.yaxis.set_major_locator(MaxNLocator(6))
ax3.set_yticks([10,15,20,25])
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))


ax6=plt.subplot(2,4,7)
ax6.plot(time_popc,(popc[['TM3-TM6-ASP241']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax6.plot(time_dmpc,(dmpc[['TM3-TM6-ASP241']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (DMPC)')
ax6.plot(time_sopc,(sopc[['TM3-TM6-ASP241']][:200000].mean(axis=1).rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
plt.fill_between(time_dmpc, (dmpc[['TM3-TM6-ASP241']][:200000].mean(axis=1).rolling(window).mean()*10)-(dmpc[['TM3-TM6-ASP241']][:200000].std(axis=1).rolling(window).mean()*10), (dmpc[['TM3-TM6-ASP241']][:200000].mean(axis=1).rolling(window).mean()*10)+(dmpc[['TM3-TM6-ASP241']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:red', alpha=0.1)
plt.fill_between(time_popc, (popc[['TM3-TM6-ASP241']][:200000].mean(axis=1).rolling(window).mean()*10)-(popc[['TM3-TM6-ASP241']][:200000].std(axis=1).rolling(window).mean()*10), (popc[['TM3-TM6-ASP241']][:200000].mean(axis=1).rolling(window).mean()*10)+(popc[['TM3-TM6-ASP241']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:green', alpha=0.1)
plt.fill_between(time_sopc, (sopc[['TM3-TM6-ASP241']][:200000].mean(axis=1).rolling(window).mean()*10)-(sopc[['TM3-TM6-ASP241']][:200000].std(axis=1).rolling(window).mean()*10), (sopc[['TM3-TM6-ASP241']][:200000].mean(axis=1).rolling(window).mean()*10)+(sopc[['TM3-TM6-ASP241']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:blue', alpha=0.1)
ax6.set_ylabel( 'TM3-TM6 Dist. ($\AA$)', fontsize=11)
ax6.axhline(y=9.12, linestyle='--', lw=1.5, color='0.5')
ax6.axhline(y=17.67, linestyle='--', lw=1.5, color='tab:orange')
#ax3.axhline(y=17.30, linestyle='--', lw=1.5, color='0.5')
#ax3.axhline(y=22.56, linestyle='--', lw=1.5, color='tab:orange')
#ax6.set_ylabel( 'TM3-TM6 Dist. ($\AA$)', fontsize=11)
ax6.set_ylim(6,23)
ax6.set_xlim(0,2000)
ax6.set_xlabel('Time (ns)', fontsize=11)
#ax3.yaxis.set_major_locator(MaxNLocator(6))
ax6.set_yticks([10,15,20])
ax6.yaxis.set_minor_locator(AutoMinorLocator(5))
ax6.xaxis.set_minor_locator(AutoMinorLocator(5))


ax7=plt.subplot(2,4,8)
ax7.plot(time_ss_dmpc,dmpc_ss.rolling(window).mean(), color='tab:red', label='DMPC (di-C14:0)')
plt.fill_between(time_ss_dmpc, dmpc_ss.rolling(window).mean()+dmpc_ss_err.rolling(window).mean(), dmpc_ss.rolling(window).mean()-dmpc_ss_err.rolling(window).mean(), color='tab:red',alpha=0.1)
ax7.plot(time_ss_popc,popc_ss.rolling(window).mean(), color='tab:green', label='POPC (C16:0,C18:1)')
plt.fill_between(time_ss_popc, popc_ss.rolling(window).mean()+popc_ss_err.rolling(window).mean(), popc_ss.rolling(window).mean()-popc_ss_err.rolling(window).mean(), color='tab:green',alpha=0.1)
ax7.plot(time_ss_sopc,sopc_ss.rolling(window).mean(), color='tab:blue', label='SOPC (C18:0,C18:1)')
plt.fill_between(time_ss_sopc, sopc_ss.rolling(window).mean()+sopc_ss_err.rolling(window).mean(), sopc_ss.rolling(window).mean()-sopc_ss_err.rolling(window).mean(), color='tab:blue',alpha=0.1)
ax7.axhline(y=0.66, linestyle='--', lw=1.5, color='tab:orange', label='6OS0, Active')
ax7.axhline(y=0.0, linestyle='--', lw=1.5, color='0.5', label='4YAY, Inactive')
#ax4.set_xticklabels(d,rotation=0,zorder=100)
#ax4.set_xticks(d1)
#print('sopc=',ss_sopc,'popc=',ss_popc,'dmpc=',ss_dmpc)
ax7.set_xlim(0,2000)
ax7.set_xlabel('Time (ns)', fontsize=11)
ax7.set_ylabel(r'ICL2 $\alpha$-helicity, $f_{\alpha}$', fontsize=11)
ax7.axhline(y=0.66, linestyle='--', lw=1.5, color='tab:orange')
ax7.axhline(y=0.0, linestyle='--', lw=1.5, color='0.5')
ax7.set_ylim(-0.05,0.7)
ax7.yaxis.set_major_locator(MaxNLocator(4))
ax7.yaxis.set_minor_locator(AutoMinorLocator(2))
ax7.xaxis.set_minor_locator(AutoMinorLocator(5))

leg=ax7.legend(ncol=5,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-1.5,2.8), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

for i in leg.legendHandles:
    i.set_linewidth(2)






ax.text(-0.24, 1.05, 'a', transform=ax.transAxes, ha='center', fontsize=14, fontweight='bold')
ax1.text(-0.24, 1.05, 'b', transform=ax1.transAxes, ha='center', fontsize=14, fontweight='bold')
ax2.text(-0.24, 1.05, 'c', transform=ax2.transAxes, ha='center', fontsize=14, fontweight='bold')
ax3.text(-0.24, 1.05, 'd', transform=ax3.transAxes, ha='center', fontsize=14, fontweight='bold')
ax6.text(-0.24, 1.05, 'e', transform=ax6.transAxes, ha='center', fontsize=14, fontweight='bold')
ax7.text(-0.24, 1.05, 'f', transform=ax7.transAxes, ha='center', fontsize=14, fontweight='bold')
fig = plt.gcf()

#left_top = plt.subplot(2,4,1)
#left_bottom = plt.subplot(2,4,5)
#left_top = plt.axes([-0.03, 0.47, 0.3, 0.52])
left_top=plt.axes([-0.03,0.45,0.3,0.50])
#left_bottom = plt.axes([-0.024, 0.015, 0.3, 0.45])
left_bottom = plt.axes([-0.024, 0.015, 0.28, 0.44])
left_top.axis('off')
left_bottom.axis('off')
im1 = left_top.imshow(sideview, aspect='equal')
im2 = left_bottom.imshow(bottomview, aspect='equal')

plt.subplots_adjust(top=0.90, bottom=0.115, left=0.02, right=0.975, hspace=0.43, wspace=0.5)
plt.Figure.set_size_inches(fig,(10, 5))
plt.savefig('Figure_1.png', dpi=300)
plt.close()
