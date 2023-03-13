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

st10_r1=pd.read_csv('data/H8_Z_depth_st10WT_r1.xvg', delim_whitespace=True)
st10_r1.columns=['time', 'X','Y','Z']
st10_r2=pd.read_csv('data/H8_Z_depth_st10WT_r2.xvg', delim_whitespace=True)
st10_r2.columns=['time', 'X','Y','Z']
st10_wt=(pd.concat([st10_r1[['Z']], st10_r2[['Z']]], axis=1)).mean(axis=1)[:395000]*10
st10_wt_err=(pd.concat([st10_r1[['Z']], st10_r2[['Z']]], axis=1)).std(axis=1)[:395000]*10

####
pepc_r1=pd.read_csv('data/H8_Z_depth_pepcWT_r1.xvg', delim_whitespace=True)
pepc_r1.columns=['time', 'X','Y','Z']
pepc_r2=pd.read_csv('data/H8_Z_depth_pepcWT_r2.xvg', delim_whitespace=True)
pepc_r2.columns=['time', 'X','Y','Z']

pepc_wt=(pd.concat([pepc_r1[['Z']], pepc_r2[['Z']]], axis=1)).mean(axis=1)[:395000]*10
pepc_wt_err=(pd.concat([pepc_r1[['Z']], pepc_r2[['Z']]], axis=1)).std(axis=1)[:395000]*10
####
sopc_r1=pd.read_csv('data/H8_Z_depth_sopcWT_r1.xvg', delim_whitespace=True)
sopc_r1.columns=['time', 'X','Y','Z']
sopc_r2=pd.read_csv('data/H8_Z_depth_sopcWT_r2.xvg', delim_whitespace=True)
sopc_r2.columns=['time', 'X','Y','Z'] 
sopc_wt=(pd.concat([sopc_r1[['Z']], sopc_r2[['Z']]], axis=1)).mean(axis=1)[:395000]*10
sopc_wt_err=(pd.concat([sopc_r1[['Z']], sopc_r2[['Z']]], axis=1)).std(axis=1)[:395000]*10

###
popc_r1=pd.read_csv('data/H8_Z_depth_popcWT_r1.xvg', delim_whitespace=True)
popc_r1.columns=['time', 'X','Y','Z']
popc_r2=pd.read_csv('data/H8_Z_depth_popcWT_r2.xvg', delim_whitespace=True)
popc_r2.columns=['time', 'X','Y','Z'] 

popc_wt=(pd.concat([popc_r1[['Z']], popc_r2[['Z']]], axis=1)).mean(axis=1)[:395000]*10
popc_wt_err=(pd.concat([popc_r1[['Z']], popc_r2[['Z']]], axis=1)).std(axis=1)[:395000]*10


popcmut_r1=pd.read_csv('data/H8_Z_depth_popcMUT_r1.xvg', delim_whitespace=True)
popcmut_r1.columns=['time', 'X','Y','Z']

popcmut_r2=pd.read_csv('data/H8_Z_depth_popcMUT_r2.xvg', delim_whitespace=True)
popcmut_r2.columns=['time', 'X','Y','Z']
 
popc_mut=(pd.concat([popcmut_r1[['Z']], popcmut_r2[['Z']]], axis=1)).mean(axis=1)[:395000]*10
popc_mut_err=(pd.concat([popcmut_r1[['Z']], popcmut_r2[['Z']]], axis=1)).std(axis=1)[:395000]*10

sopcmut_r1=pd.read_csv('data/H8_Z_depth_sopcMUT_r1.xvg', delim_whitespace=True)
sopcmut_r1.columns=['time', 'X','Y','Z']

sopcmut_r2=pd.read_csv('data/H8_Z_depth_sopcMUT_r2.xvg', delim_whitespace=True)
sopcmut_r2.columns=['time', 'X','Y','Z']
 
sopc_mut=(pd.concat([sopcmut_r1[['Z']], sopcmut_r2[['Z']]], axis=1)).mean(axis=1)[:395000]*10
sopc_mut_err=(pd.concat([sopcmut_r1[['Z']], sopcmut_r2[['Z']]], axis=1)).std(axis=1)[:395000]*10


st10mut_r1=pd.read_csv('data/H8_Z_depth_st10MUT_r1.xvg', delim_whitespace=True)
st10mut_r1.columns=['time', 'X','Y','Z']

st10mut_r2=pd.read_csv('data/H8_Z_depth_st10MUT_r2.xvg', delim_whitespace=True)
st10mut_r2.columns=['time', 'X','Y','Z']
 
st10_mut=(pd.concat([st10mut_r1[['Z']], st10mut_r2[['Z']]], axis=1)).mean(axis=1)[:395000]*10
st10_mut_err=(pd.concat([st10mut_r1[['Z']], st10mut_r2[['Z']]], axis=1)).std(axis=1)[:395000]*10


pepcmut_r1=pd.read_csv('data/H8_Z_depth_pepcMUT_r2.xvg', delim_whitespace=True)
pepcmut_r1.columns=['time', 'X','Y','Z']

pepcmut_r2=pd.read_csv('data/H8_Z_depth_pepcMUT_r2.xvg', delim_whitespace=True)
pepcmut_r2.columns=['time', 'X','Y','Z']
 
pepc_mut=(pd.concat([pepcmut_r1[['Z']], pepcmut_r2[['Z']]], axis=1)).mean(axis=1)[:395000]*10
pepc_mut_err=(pd.concat([pepcmut_r1[['Z']], pepcmut_r2[['Z']]], axis=1)).std(axis=1)[:395000]*10

time_sopc=np.linspace(0,2000,len(sopc_wt))
time_popc=np.linspace(0,2000,len(popc_wt))
time_st10=np.linspace(0,2000,len(st10_wt))
time_pepc=np.linspace(0,2000,len(pepc_wt))


window=500
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.plot(time_sopc, sopc_wt.rolling(window).mean(), color='green', label='SOPC + WT' )
plt.fill_between(time_sopc, sopc_wt+sopc_wt_err, sopc_wt-sopc_wt_err, color='tab:green', alpha=0.1)
plt.plot(time_sopc, sopc_mut.rolling(window).mean(), color='blue', label='SOPC + F309P/F313P')
plt.fill_between(time_sopc, sopc_mut+sopc_mut_err, sopc_mut-sopc_mut_err, color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.axhline(y=0, color='orange',linestyle='--' ,lw='2')
#plt.ylim(-3.5,-0.5)
plt.xticks([0,500,1000,1500,2000],fontsize=15)
plt.yticks(fontsize=15)
plt.legend(frameon=False)
plt.xlabel('Time (ns)', fontsize=15)
plt.ylabel('Insertion depth ($\AA$)', fontsize=15)
plt.text (1200, -2, 'Glycerol P', fontsize=12)
plt.text (-150, 17, 'a', fontsize=20, weight='bold')
plt.ylim(-20,15)

plt.subplot(2,2,3)
plt.plot(time_popc, popc_wt.rolling(window).mean(), color='green', label='POPC + WT')
plt.fill_between(time_popc, popc_wt+popc_wt_err, popc_wt-popc_wt_err, color='tab:green', alpha=0.1)
plt.plot(time_popc, popc_mut.rolling(window).mean(), color='blue', label='POPC + F309P/F313P')
plt.fill_between(time_popc, popc_mut+popc_mut_err, popc_mut-popc_mut_err, color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.xticks([0,500,1000,1500,2000],fontsize=15)
plt.yticks(fontsize=15)
plt.axhline(y=0, color='orange',linestyle='--' ,lw='2')
#plt.ylim(-3.5,-0.5)
plt.xlabel('Time (ns)', fontsize=15)
plt.ylabel('Insertion depth ($\AA$)', fontsize=15)
plt.text (1200, 2, 'Glycerol P', fontsize=12)
plt.text (-150, 17, 'c', fontsize=20, weight='bold')
plt.legend(frameon=False)
plt.ylim(-20,15)

plt.subplot(2,2,2)
plt.plot(time_st10, st10_wt.rolling(window).mean(), color='green', label='SOPC + WT + 10 mN/m')
plt.fill_between(time_st10, st10_wt+st10_wt_err, st10_wt-st10_wt_err, color='tab:green', alpha=0.1)
plt.plot(time_st10, st10_mut.rolling(window).mean(), color='blue', label='SOPC + F309P/F313P +10 mN/m')
plt.fill_between(time_st10, st10_mut+st10_mut_err, st10_mut-st10_mut_err, color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.xticks([0,500,1000,1500,2000],fontsize=15)
plt.yticks(fontsize=15)
plt.axhline(y=0, color='orange',linestyle='--' ,lw='2')
#plt.ylim(-3.5,-0.5)
plt.xlabel('Time (ns)', fontsize=15)
plt.ylabel('Insertion depth ($\AA$)', fontsize=15)
plt.text (1200, -3, 'Glycerol P', fontsize=12)
plt.text (-150, 17, 'b', fontsize=20, weight='bold')
plt.ylim(-20,15)
plt.legend(frameon=False)

plt.subplot(2,2,4)
plt.plot(time_pepc, pepc_wt.rolling(window).mean(), color='green', label='SOPC:SOPE + WT ')
plt.fill_between(time_pepc, pepc_wt+pepc_wt_err, pepc_wt-pepc_wt_err, color='tab:green', alpha=0.1)
plt.plot(time_pepc, pepc_mut.rolling(window).mean(), color='blue', label='SOPC:SOPE + F309P/F313P')
plt.fill_between(time_pepc, pepc_mut+pepc_mut_err, pepc_mut-pepc_mut_err, color='tab:blue', alpha=0.1)
plt.legend()
plt.xlim(0,2000)
#plt.ylim(-3.5,-0.5)
plt.xticks([0,500,1000,1500,2000],fontsize=15)
plt.yticks(fontsize=15)
plt.axhline(y=0, color='orange',linestyle='--' ,lw='2')
plt.xlabel('Time (ns)', fontsize=15)
plt.ylabel('Insertion depth ($\AA$)', fontsize=15)
plt.text (1200, -2, 'Glycerol P', fontsize=12)
plt.text (-150, 17, 'd', fontsize=20, weight='bold')
plt.ylim(-20,15)
plt.legend(frameon=False)

plt.subplots_adjust(top=0.90, bottom=0.115, left=0.1, right=0.975, hspace=0.3, wspace=0.3)
plt.savefig('Figure_S5.png', dpi=300)
