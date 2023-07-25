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

sopc_ang= pd.read_csv('data_Figure_8/angii_20us', delim_whitespace=True)
sopc_ang.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6','Npxxy','n','n']
time_ang=np.linspace(0,20, len(sopc_ang))


sopc_10= pd.read_csv('data_Figure_8/st10_20us', delim_whitespace=True)
sopc_10.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6','Npxxy','n','n']
time_10=np.linspace(0,20, len(sopc_10))


sopc_apo= pd.read_csv('data_Figure_8/apo_20us', delim_whitespace=True)
sopc_apo.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6','Npxxy','n','n']
time_apo=np.linspace(0,20, len(sopc_apo))


window=30

ax=plt.subplot(2,3,1)
ax.plot(time_apo, sopc_apo[['TM1-TM6']].rolling(window).mean()*10, color='tab:blue', label="SOPC")
ax.plot(time_10, sopc_10[['TM1-TM6']].rolling(window).mean()*10, color='tab:green', label="SOPC + 10 mN/m")
ax.plot(time_ang, sopc_ang[['TM1-TM6']].rolling(window).mean()*10, color='tab:red', label='SOPC + AngII')
ax.axhline(y=32.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
ax.set_ylabel('TM1-TM6 Dist. ($\AA$)', fontsize=12)
ax.set_xlim(0,20)
ax.set_ylim(17,37)
#ax.set_legend()
ax.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax.yaxis.set_major_locator(MaxNLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
leg=ax.legend(ncol=3, frameon=False, borderpad=None, loc='upper center', bbox_to_anchor=(1.8,1.31), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)
#leg=plt.legend(ncol=3,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(25,36), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

for i in leg.legendHandles:
    i.set_linewidth(2)



ax1=plt.subplot(2,3,2)
ax1.plot(time_apo, sopc_apo[['TM1-ICL2']].rolling(window).mean()*10, color='tab:blue', label="Apo")
ax1.plot(time_10, sopc_10[['TM1-ICL2']].rolling(window).mean()*10, color='tab:green', label="ST=15 mN/m")
ax1.plot(time_ang, sopc_ang[['TM1-ICL2']].rolling(window).mean()*10, color='tab:red', label='Angii')
ax1.axhline(y=25.57, linestyle='dashed', color='tab:orange', lw=1.5)
ax1.axhline(y=19.50, linestyle='dashed', color='0.5',lw=1.5)
ax1.set_ylabel('TM1-ICL2 Dist. ($\AA$)', fontsize=12)
ax1.set_xlim(0,20)
ax1.set_ylim(16,30)
ax1.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax1.yaxis.set_major_locator(MaxNLocator(4))
ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))


ax2=plt.subplot(2,3,3)
ax2.plot(time_apo, sopc_apo[['TM5-ICL2']].rolling(window).mean()*10, color='tab:blue', label="Apo")
ax2.plot(time_10, sopc_10[['TM5-ICL2']].rolling(window).mean()*10, color='tab:green', label="ST=15 mN/m")
ax2.plot(time_ang, sopc_ang[['TM5-ICL2']].rolling(window).mean()*10, color='tab:red', label='Angii')
ax2.axhline(y=23.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax2.axhline(y=29.77, linestyle='dashed', color='0.5',lw=1.5)
ax2.set_ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=12)
ax2.set_xlim(-0,20)
ax2.set_ylim(19,32)
ax2.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax2.yaxis.set_major_locator(MaxNLocator(4))
ax2.yaxis.set_minor_locator(AutoMinorLocator(3))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))



ax3=plt.subplot(2,3,4)
ax3.plot(time_apo, sopc_apo[['TM6-H8']].rolling(window).mean()*10, color='tab:blue', label="ST=10 mN/m")
ax3.plot(time_10, sopc_10[['TM6-H8']].rolling(window).mean()*10, color='tab:green', label="ST=15 mN/m")
ax3.plot(time_ang, sopc_ang[['TM6-H8']].rolling(window).mean()*10, color='tab:red', label='Angii')
ax3.axhline(y=22.56, linestyle='dashed', color='tab:orange', lw=1.5)
ax3.axhline(y=17.30, linestyle='dashed', color='0.5',lw=1.5)
ax3.set_ylabel('TM6-H8 Dist. ($\AA$)', fontsize=12)
ax3.set_xlim(0,20)
ax3.set_ylim(10,30)
ax3.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax3.yaxis.set_major_locator(MaxNLocator(4))
ax3.yaxis.set_minor_locator(AutoMinorLocator(4))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))



ax4=plt.subplot(2,3,5)
ax4.plot(time_apo, sopc_apo[['TM3-TM6']].rolling(window).mean()*10, color='tab:blue', label="Apo")
ax4.plot(time_10, sopc_10[['TM3-TM6']].rolling(window).mean()*10, color='tab:green', label="ST=15 mN/m")
ax4.plot(time_ang, sopc_ang[['TM3-TM6']].rolling(window).mean()*10, color='tab:red', label='Angii')
ax4.axhline(y=17.67, linestyle='dashed', color='tab:orange', lw=1.5)
ax4.axhline(y=9.12, linestyle='dashed', color='0.5',lw=1.5)
ax4.set_ylabel('TM3-TM6 Dist. ($\AA$)', fontsize=12)
ax4.set_xlim(-0,20)
ax4.set_ylim(8,23)
ax4.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax4.yaxis.set_major_locator(MaxNLocator(4))
ax4.yaxis.set_minor_locator(AutoMinorLocator(5))
ax4.xaxis.set_minor_locator(AutoMinorLocator(5))



ax5=plt.subplot(2,3,6)
ax5.plot(time_apo, sopc_apo[['Npxxy']].rolling(window).mean()*10, color='tab:blue', label="Apo")
ax5.plot(time_10, sopc_10[['Npxxy']].rolling(window).mean()*10, color='tab:green', label="ST=15 mN/m")
ax5.plot(time_ang, sopc_ang[['Npxxy']].rolling(window).mean()*10, color='tab:red', label='Angii')
ax5.axhline(y=4.43, linestyle='dashed', color='tab:orange', lw=1.5)
ax5.axhline(y=11.71,  linestyle='dashed', color='0.5',lw=1.5)
#plt.ylabel(r'ICL2 $\alpha$-helicity, $f_{\alpha}$', fontsize=15)
ax5.set_ylabel('Y302$^{7.53}$-Y215$^{5.58}$ ($\AA$)', fontsize=12)
ax5.set_xlim(0,20)
#plt.ylim(-0.05,1)
ax5.set_xlabel('Time ($\mathrm{\mu}$s)', fontsize=12)
ax5.yaxis.set_major_locator(MaxNLocator(4))
ax5.yaxis.set_minor_locator(AutoMinorLocator(5))
ax5.xaxis.set_minor_locator(AutoMinorLocator(5))



ax.text(-0.14, 1., 'a', transform=ax.transAxes, ha='center', fontsize=15, fontweight='bold')
ax1.text(-0.14, 1., 'b', transform=ax1.transAxes, ha='center', fontsize=15, fontweight='bold')
ax2.text(-0.14, 1., 'c', transform=ax2.transAxes, ha='center', fontsize=15, fontweight='bold')
ax3.text(-0.14, 1, 'd', transform=ax3.transAxes, ha='center', fontsize=15, fontweight='bold')
ax4.text(-0.14, 1, 'e', transform=ax4.transAxes, ha='center', fontsize=15, fontweight='bold')
ax5.text(-0.14, 1, 'f', transform=ax5.transAxes, ha='center', fontsize=15, fontweight='bold')


fig = plt.gcf()

plt.subplots_adjust(top=0.915, bottom=0.11, left=0.07, right=0.975, hspace=0.35, wspace=0.35)
plt.Figure.set_size_inches(fig,(11, 5))
plt.savefig('Figure_8.png', dpi=600)
plt.savefig('Figure_8.svg', dpi=600)
plt.close()
#plt.savefig('ST_apo_ang.png', bbox_inches='tight', dpi=600)
