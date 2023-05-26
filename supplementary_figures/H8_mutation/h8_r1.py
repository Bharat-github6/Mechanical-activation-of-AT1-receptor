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
from matplotlib.patches import Rectangle
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

popc_r1= pd.read_csv('data/popc_r1', delim_whitespace=True)
popc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
popc_r1=popc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH']]


popc_r2= pd.read_csv('data/popc_r2', delim_whitespace=True)
popc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
popc_r2=popc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH']]


popc=pd.concat([popc_r1, popc_r2], axis=1)
popc=popc[:200000]
time_popc=np.linspace(0,2000,len(popc))

sopc_r1= pd.read_csv('data/sopc_r1', delim_whitespace=True)
sopc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
sopc_r1=sopc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH']]


sopc_r2= pd.read_csv('data/sopc_r2', delim_whitespace=True)
sopc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
sopc_r2=sopc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH']]


sopc=pd.concat([sopc_r1, sopc_r2], axis=1)
sopc=sopc[:200000]
time_sopc=np.linspace(0,2000,len(sopc))

pepc_r1= pd.read_csv('data/pepc_r1', delim_whitespace=True)
pepc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
pepc_r1=pepc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH']]


pepc_r2= pd.read_csv('data/pepc_r2', delim_whitespace=True)
pepc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
pepc_r2=pepc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH']]


pepc=pd.concat([pepc_r1, pepc_r2], axis=1)
pepc=pepc[:200000]
time_pepc=np.linspace(0,2000,len(pepc))


st10_r1= pd.read_csv('data/st10_r1', delim_whitespace=True)
st10_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
st10_r1=st10_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH']]


st10_r2= pd.read_csv('data/st10_r2', delim_whitespace=True)
st10_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
st10_r2=st10_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH']]


st10=pd.concat([st10_r1, st10_r2], axis=1)
st10=st10[:200000]

time_st10=np.linspace(0,2000,len(st10))



##ICL2
popc_ssr1=pd.read_csv('data/popc_ICL2_r1.xvg', delim_whitespace=True, comment='#')
popc_ssr1.columns=['time', 'structure', 'coil','Bend', 'Turn', 'A_Helix','Th_Helix']
popc_ssr1=popc_ssr1[:400000]

popc_ssr2=pd.read_csv('data/popc_ICL2_r2.xvg', delim_whitespace=True, comment='#')
popc_ssr2.columns=['time', 'structure', 'coil','Bend', 'Turn', 'A_Helix','Th_Helix']
popc_ssr2=popc_ssr2[:400000]

popc_ssr1=popc_ssr1[['A_Helix','Th_Helix']].sum(axis=1)/11
popc_ssr2=popc_ssr2[['A_Helix','Th_Helix']].sum(axis=1)/11

popc_ss=pd.concat([popc_ssr1, popc_ssr2], axis=1)
popc_ss_err=pd.concat([popc_ssr1, popc_ssr2], axis=1).std(axis=1)

sopc_ssr1=pd.read_csv('data/sopc_ICL2_r1.xvg', delim_whitespace=True, comment='#')
sopc_ssr1.columns=['time', 'structure', 'coil','Bend', 'B_bride','Turn', 'A_Helix','fiv_Helix','Th_Helix']
sopc_ssr1=sopc_ssr1[:400000]

sopc_ssr2=pd.read_csv('data/sopc_ICL2_r2.xvg', delim_whitespace=True, comment='#')
sopc_ssr2.columns=['time', 'structure', 'coil','Bend', 'Turn', 'A_Helix','fiv_helix','Th_Helix']
sopc_ssr2=sopc_ssr2[:400000]

sopc_ssr1=sopc_ssr1[['A_Helix','fiv_Helix','Th_Helix' ]].sum(axis=1)/11
sopc_ssr2=sopc_ssr2[['A_Helix','fiv_helix','Th_Helix' ]].sum(axis=1)/11
sopc_ss=pd.concat([sopc_ssr1, sopc_ssr2], axis=1)
sopc_ss_err=pd.concat([sopc_ssr1, sopc_ssr2], axis=1).std(axis=1)


pepc_ssr1_1=pd.read_csv('data/pepc_ICL2_r1.xvg', delim_whitespace=True, comment='#')
pepc_ssr1_1.columns=['time', 'structure', 'coil','Bend','Turn', 'A_Helix','fiv_Helix','Th_Helix']
#pepc_ssr1=pepc_ssr1[:400000]

pepc_ssr1_2=pd.read_csv('data/pepc_ICL2_2us_2nd.xvg', delim_whitespace=True, comment='#')
pepc_ssr1_2.columns=['time', 'structure', 'coil','Bend','Turn', 'A_Helix','Th_Helix']
pepc_ssr1_2=pepc_ssr1_2[['A_Helix', 'Th_Helix']].sum(axis=1)/11

pepc_ssr2=pd.read_csv('data/pepc_ICL2_r2.xvg', delim_whitespace=True, comment='#')
pepc_ssr2.columns=['time', 'structure', 'coil','Bend', 'Turn', 'A_Helix','fiv_helix','Th_Helix']
pepc_ssr2=pepc_ssr2[:4000000]

pepc_ssr1_1=pepc_ssr1_1[['A_Helix','fiv_Helix','Th_Helix' ]].sum(axis=1)/11
pepc_ssr1=pd.concat([pepc_ssr1_1, pepc_ssr1_2], axis=0)
pepc_ssr1=pepc_ssr1.reset_index(drop=True) 

time_pepc_ss=np.linspace(0,2000,len(pepc_ssr1))
pepc_ssr2=pepc_ssr2[['A_Helix','fiv_helix','Th_Helix' ]].sum(axis=1)/11
pepc_ss=pd.concat([pepc_ssr1, pepc_ssr2], axis=1)
pepc_ss_err=pd.concat([pepc_ssr1, pepc_ssr2], axis=1).std(axis=1)



st10_ssr1=pd.read_csv('data/st10_ICL2_r1.xvg', delim_whitespace=True, comment='#')
st10_ssr1.columns=['time', 'structure', 'coil','Bend','Turn', 'A_Helix','fiv_Helix','Th_Helix']
st10_ssr1=st10_ssr1[:400000]
time=st10_ssr1[['time']]*0.001


st10_ssr2=pd.read_csv('data/st10_ICL2_r2.xvg', delim_whitespace=True, comment='#')
st10_ssr2.columns=['time', 'structure', 'coil','B_bridge','Bend', 'Turn','Th_Helix']
st10_ssr2=st10_ssr2[:400000]

st10_ssr1=st10_ssr1[['A_Helix','fiv_Helix','Th_Helix' ]].sum(axis=1)/11
st10_ssr2=st10_ssr2[['Th_Helix' ]].sum(axis=1)/11
st10_ss=pd.concat([st10_ssr1, st10_ssr2], axis=1)
st10_ss_err=pd.concat([st10_ssr1, st10_ssr2], axis=1).std(axis=1)


#exp=[33.48,25.57,23.65,22.56] 6DO1
exp=[32.656,25.796,23.422,22.235] #6OS0

#time_popc_ss=np.linspace(0,2000,len(popc_ss))
#time_sopc_ss=np.linspace(0,2000,len(sopc_ss))
#time_pepc_ss=np.linspace(0,2000,len(pepc_ss))
#time_st10_ss=np.linspace(0,2000,len(st10_ss))

#time=sopc_ssr1[['time']]*0.001
#time_sopc_ss=np.linspace(0,2000,len(sopc_ss))
#time_pepc_ss=np.linspace(0,2000,len(pepc_ss))
#time_st10_ss=np.linspace(0,2000,len(st10_ss))

window = 500
width=70
start=2100
sp = 100


ax=plt.subplot(2,3,1)
ax.plot(time_popc,(popc_r1[['TM1-TM6']][:200000].rolling(window).mean()*10),color='tab:green',label='POPC')
ax.plot(time_sopc,(sopc_r1[['TM1-TM6']][:200000].rolling(window).mean()*10), color='tab:blue', label='SOPC')
ax.plot(time_pepc,(pepc_r1[['TM1-TM6']][:200000].rolling(window).mean()*10),color='tab:red', label='SOPE:SOPC') 
ax.plot(time_st10,(st10_r1[['TM1-TM6']][:200000].rolling(window).mean()*10), color='grey', label='SOPC + 10 mN/m')
ax.axhline(y=32.85, linestyle='dashed', color='tab:orange', lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
#ax.legend(loc='best', fontsize=5)
ax.set_ylim(17,41)
ax.set_xlim(0,2000)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
ax.yaxis.set_major_locator(MaxNLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('TM1-TM6 Dist. ($\AA$)', fontsize=11)
#ax.set_xlabel('Time (ns)', fontsize=11)
ax.set_xlabel('Time (ns)', fontsize=11)
#for i in leg.legendHandles:
#    i.set_linewidth(2)

box_parts = ax.boxplot((popc[['TM1-TM6']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

box_parts = ax.boxplot((sopc[['TM1-TM6']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax.boxplot((pepc[['TM1-TM6']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax.boxplot((st10[['TM1-TM6']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)

rect = Rectangle((2040,17), 432, 24, clip_on=False, ec='k', fill=False)
ax.add_patch(rect)



ax1=plt.subplot(2,3,2)
ax1.plot(time_popc,(popc_r1[['TM1-ICL2']][:200000].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax1.plot(time_pepc,(pepc_r1[['TM1-ICL2']][:200000].rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (SOPE_SOPC)')
ax1.plot(time_sopc,(sopc_r1[['TM1-ICL2']][:200000].rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
ax1.plot(time_st10,(st10_r1[['TM1-ICL2']][:200000].rolling(window).mean()*10), color='grey', label='AT1R/-/- (ST10)')
ax1.axhline(y=25.57, linestyle='dashed', color='tab:orange', lw=1.5)
ax1.axhline(y=19.50, linestyle='dashed', color='0.5',lw=1.5)
#ax.legend(loc='best', fontsize=5)
ax1.set_ylim(17,32)
ax1.set_xlim(0,2000)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
ax1.yaxis.set_major_locator(MaxNLocator(4))
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.set_ylabel('TM1-ICL2 Dist. ($\AA$)', fontsize=11)
#ax.set_xlabel('Time (ns)', fontsize=11)
ax1.set_xlabel('Time (ns)', fontsize=11)
rect = Rectangle((2040,17), 432, 15, clip_on=False, ec='k', fill=False)
ax1.add_patch(rect)
box_parts = ax1.boxplot((popc[['TM1-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

box_parts = ax1.boxplot((sopc[['TM1-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax1.boxplot((pepc[['TM1-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax1.boxplot((st10[['TM1-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)






ax2=plt.subplot(2,3,3)
ax2.plot(time_popc,(popc_r1[['TM5-ICL2']][:200000].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax2.plot(time_pepc,(pepc_r1[['TM5-ICL2']][:200000].rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (SOPE_SOPC)')
ax2.plot(time_sopc,(sopc_r1[['TM5-ICL2']][:200000].rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
ax2.plot(time_st10,(st10_r1[['TM5-ICL2']][:200000].rolling(window).mean()*10), color='grey', label='AT1R/-/- (ST10)')
ax2.axhline(y=23.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax2.axhline(y=29.77, linestyle='dashed', color='0.5',lw=1.5)
#ax.legend(loc='best', fontsize=5)
ax2.set_ylim(15,32)
ax2.set_xlim(0,2000)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
ax2.yaxis.set_major_locator(MaxNLocator(4))
ax2.yaxis.set_minor_locator(AutoMinorLocator(5))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
ax2.set_ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=11)
#ax.set_xlabel('Time (ns)', fontsize=11)
ax2.set_xlabel('Time (ns)', fontsize=11)
rect = Rectangle((2040,15), 432, 17, clip_on=False, ec='k', fill=False)
ax2.add_patch(rect)
box_parts = ax2.boxplot((popc[['TM5-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

box_parts = ax2.boxplot((sopc[['TM5-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax2.boxplot((pepc[['TM5-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax2.boxplot((st10[['TM5-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)



ax3=plt.subplot(2,3,4)
ax3.plot(time_popc,(popc_r1[['TM6-H8']][:200000].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax3.plot(time_pepc,(pepc_r1[['TM6-H8']][:200000].rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (SOPE_SOPC)')
ax3.plot(time_sopc,(sopc_r1[['TM6-H8']][:200000].rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
ax3.plot(time_st10,(st10_r1[['TM6-H8']][:200000].rolling(window).mean()*10), color='grey', label='AT1R/-/- (ST10)')
ax3.axhline(y=22.56, linestyle='dashed', color='tab:orange', lw=1.5)
ax3.axhline(y=17.30, linestyle='dashed', color='0.5',lw=1.5)
#ax.legend(loc='best', fontsize=5)
ax3.set_ylim(10,31)
ax3.set_xlim(0,2000)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
ax3.yaxis.set_major_locator(MaxNLocator(4))
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))
ax3.set_ylabel('TM6-H8 Dist. ($\AA$)', fontsize=11)
#ax.set_xlabel('Time (ns)', fontsize=11)
ax3.set_xlabel('Time (ns)', fontsize=11)
rect = Rectangle((2040,10), 432, 21, clip_on=False, ec='k', fill=False)
ax3.add_patch(rect)
box_parts = ax3.boxplot((popc[['TM6-H8']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

box_parts = ax3.boxplot((sopc[['TM6-H8']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax3.boxplot((pepc[['TM6-H8']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax3.boxplot((st10[['TM6-H8']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)


ax4=plt.subplot(2,3,5)
ax4.plot(time_popc,(popc_r1[['TM3-TM6-ASP241']][:200000].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
ax4.plot(time_pepc,(pepc_r1[['TM3-TM6-ASP241']][:200000].rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (SOPE_SOPC)')
ax4.plot(time_sopc,(sopc_r1[['TM3-TM6-ASP241']][:200000].rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
ax4.plot(time_st10,(st10_r1[['TM3-TM6-ASP241']][:200000].rolling(window).mean()*10), color='grey', label='AT1R/-/- (ST10)')
ax4.axhline(y=17.67, linestyle='dashed', color='tab:orange', lw=1.5)
ax4.axhline(y=9.12, linestyle='dashed', color='0.5',lw=1.5)
ax.legend(loc='best', fontsize=5)
ax4.set_ylim(6,23)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
ax4.yaxis.set_major_locator(MaxNLocator(4))
ax4.yaxis.set_minor_locator(AutoMinorLocator(5))
ax4.xaxis.set_minor_locator(AutoMinorLocator(5))
ax4.set_ylabel('TM3-TM6 Dist. ($\AA$)', fontsize=11)
ax4.set_xlim(0,2000)
ax4.set_xlabel('Time (ns)', fontsize=11)
#ax4.set_xlabel('Time (ns)', fontsize=11)
rect = Rectangle((2040,6), 432, 17, clip_on=False, ec='k', fill=False)
ax4.add_patch(rect)
box_parts = ax4.boxplot((popc[['TM3-TM6-ASP241']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

box_parts = ax4.boxplot((sopc[['TM3-TM6-ASP241']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax4.boxplot((pepc[['TM3-TM6-ASP241']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)
5
box_parts = ax4.boxplot((st10[['TM3-TM6-ASP241']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)





#ax5=plt.subplot(2,3,6)
#ax5.plot(time_popc,(popc_r1[['OH']][:200000].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (POPC)')
#ax5.plot(time_pepc,(pepc_r1[['OH']][:200000].mean(axis=1).rolling(window).mean()*10),color='tab:red', label='AT1R/-/- (SOPE_SOPC)')
#ax5.plot(time_sopc,(sopc_r1[['OH']][:200000].mean(axis=1).rolling(window).mean()*10), color='tab:blue', label='AT1R/-/- (SOPC)')
#ax5.plot(time_st10,(st10_r1[['OH']][:200000].mean(axis=1).rolling(window).mean()*10), color='grey', label='AT1R/-/- (ST10)')
#plt.fill_between(time_pepc, (pepc[['OH']][:200000].mean(axis=1).rolling(window).mean()*10)-(pepc[['OH']][:200000].std(axis=1).rolling(window).mean()*10), (pepc[['OH']][:200000].mean(axis=1).rolling(window).mean()*10)+(pepc[['OH']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:red', alpha=0.1)
#plt.fill_between(time_popc, (popc[['OH']][:200000].mean(axis=1).rolling(window).mean()*10)-(popc[['OH']][:200000].std(axis=1).rolling(window).mean()*10), (popc[['OH']][:200000].mean(axis=1).rolling(window).mean()*10)+(popc[['OH']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:green', alpha=0.1)
#plt.fill_between(time_sopc, (sopc[['OH']][:200000].mean(axis=1).rolling(window).mean()*10)-(sopc[['OH']][:200000].std(axis=1).rolling(window).mean()*10), (sopc[['OH']][:200000].mean(axis=1).rolling(window).mean()*10)+(sopc[['OH']][:200000].std(axis=1).rolling(window).mean()*10),color='tab:blue', alpha=0.1)
#plt.fill_between(time_st10, (st10[['OH']][:200000].mean(axis=1).rolling(window).mean()*10)-(st10[['OH']][:200000].std(axis=1).rolling(window).mean()*10), (st10[['OH']][:200000].mean(axis=1).rolling(window).mean()*10)+(st10[['OH']][:200000].std(axis=1).rolling(window).mean()*10),color='grey', alpha=0.1)
#ax5.axhline(y=4.43, linestyle='dashed', color='tab:orange', lw=1.5)
#ax5.axhline(y=11.23, linestyle='dashed', color='0.5',lw=1.5)
#ax.legend(loc='best', fontsize=5)
#ax5.set_ylim(2,16)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
#ax5.yaxis.set_major_locator(MaxNLocator(4))
#ax5.yaxis.set_minor_locator(AutoMinorLocator(5))
#ax5.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax5.set_ylabel('TYR215OH-TYR302OH Dist. ($\AA$)', fontsize=11)
#ax5.set_xlim(0,2000)
#ax5.set_xlabel('Time (ns)', fontsize=11)


ax6=plt.subplot(2,3,6)
ax6.plot(time,popc_ssr1.rolling(window).mean(),color='tab:green',label='AT1R/-/- (POPC)')
ax6.plot(time_pepc_ss,pepc_ssr1.rolling(window).mean(),color='tab:red', label='AT1R/-/- (SOPE_SOPC)')
ax6.plot(time,sopc_ssr1.rolling(window).mean(), color='tab:blue', label='AT1R/-/- (SOPC)')
ax6.plot(time,st10_ssr1.rolling(window).mean(), color='grey', label='AT1R/-/- (ST10)')
ax6.axhline(y=0.66, linestyle='dashed', color='tab:orange', lw=1.5)
ax6.axhline(y=0, linestyle='dashed', color='0.5',lw=1.5)
#ax.legend(loc='best', fontsize=5)
ax6.set_ylim(-0.05,0.8)
ax6.set_xlim(0,2000)
rect = Rectangle((2040,-0.05), 432, 0.85, clip_on=False, ec='k', fill=False)
ax6.add_patch(rect)

box_parts = ax6.boxplot((popc_ss[300000:400000].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False, whis=(10,90))
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

box_parts = ax6.boxplot((sopc_ss[300000:400000].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax6.boxplot((pepc_ss[300000:400000].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax6.boxplot((st10_ss[300000:400000].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)

leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(1.8,1.38), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)

ax6.yaxis.set_major_locator(MultipleLocator(0.2))
ax6.yaxis.set_minor_locator(AutoMinorLocator(2))
ax6.xaxis.set_minor_locator(AutoMinorLocator(5))
ax6.set_ylabel(r'ICL2 $\alpha$-helicity, $f_{\alpha}$', fontsize=11)
ax6.set_xlim(0,2000)
#ax.set_xlabel('Time (ns)', fontsize=11)
ax6.set_xlabel('Time (ns)', fontsize=11)






#ax5.bar(0,sopc_ss,width,yerr=sopc_ss_err,color='lightblue',edgecolor='black', label='0mN/m')
#ax5.bar(5,st5_ss,width,yerr=st5_ss_err,color='lightblue', edgecolor='black', label='5mN/m')
#ax5.bar(10,st10_ss,width,yerr=st10_ss_err,color='lightblue',edgecolor='black', label='10mN/m')
#ax5.bar(15,st15_ss,width,yerr=st15_ss_err,color='lightblue',edgecolor='black', label='15mN/m')
#ax5.bar(20,st20_ss,width,yerr=st20_ss_err,color='lightblue',edgecolor='black', label='20mN/m')
#ax5.axhline(y=0.65, linestyle='--', lw=1.5, color='tab:orange')
#ax5.set_ylim(0,0.7)
#ax5.set_xticks([0,5,10,15,20])
#ax5.set_xlabel('Tension (mN/m)', fontsize=11)
#ax5.set_ylabel(r'ICL2 $\alpha$-helicity, $f_{\alpha}$', fontsize=11)
#ax5.yaxis.set_major_locator(MaxNLocator(4))
#ax5.yaxis.set_minor_locator(AutoMinorLocator(3))



for i in leg.legendHandles:
    i.set_linewidth(2)


ax.text(-0.21, 1.05, 'a', transform=ax.transAxes, ha='center', fontsize=14, fontweight='bold')
ax1.text(-0.22, 1.05, 'b', transform=ax1.transAxes, ha='center', fontsize=14, fontweight='bold')
ax2.text(-0.22, 1.05, 'c', transform=ax2.transAxes, ha='center', fontsize=14, fontweight='bold')
ax3.text(-0.21, 1.05, 'd', transform=ax3.transAxes, ha='center', fontsize=14, fontweight='bold')
ax4.text(-0.22, 1.05, 'e', transform=ax4.transAxes, ha='center', fontsize=14, fontweight='bold')
ax6.text(-0.22, 1.05, 'f', transform=ax6.transAxes, ha='center', fontsize=14, fontweight='bold')


fig = plt.gcf()
plt.subplots_adjust(top=0.9, bottom=0.115, left=0.07, right=0.94, hspace=0.43, wspace=0.6)

plt.Figure.set_size_inches(fig,(8.5, 4))
plt.savefig('Figure_S7.png', dpi=300)
#plt.savefig('time_evolution.svg', dpi=900, bbox_inches='tight')
plt.close()
