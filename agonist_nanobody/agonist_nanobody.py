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

illustr = plt.imread('Structure_v2.png')


ang_r2= pd.read_csv('data/angii/replica_2/Deer_analysis2us', delim_whitespace=True)
ang_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
ang_r2=ang_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

ang_r1= pd.read_csv('data/angii/replica_1/Deer_analysis2us', delim_whitespace=True)
ang_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
ang_r1=ang_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

ang=pd.concat([ang_r1,ang_r2], axis=1)[:200000]
time_ang=np.linspace(0,2000,len(ang))


#/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_agonist_only/ASPH74-125/production_run/descriptor
s1i8_r1= pd.read_csv('data/s1i8/replica_1/Deer_analysis2us', delim_whitespace=True)
s1i8_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
s1i8_r1=s1i8_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

s1i8_r2= pd.read_csv('data/s1i8/replica_2/Deer_analysis_2us', delim_whitespace=True)
s1i8_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
s1i8_r2=s1i8_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

s1i8=pd.concat([s1i8_r1,s1i8_r2], axis=1)[:200000]


#/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_nanobody_only/ASPH74-125/production_run/descriptor
n_r1= pd.read_csv('data/nanobody/replica_1/Deer_analysis2us', delim_whitespace=True)
n_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
n_r1=n_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

n_r2= pd.read_csv('data/nanobody/replica_2/Deer_analysis_2us', delim_whitespace=True)
n_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
n_r2=n_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

n=pd.concat([n_r1,n_r2], axis=1)[:200000]

an_r1= pd.read_csv('data/agonist_nanobody/replica_1/Deer_analysis2us', delim_whitespace=True)
an_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
an_r1=an_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

an_r2= pd.read_csv('data/agonist_nanobody/replica_2/Deer_analysis2us', delim_whitespace=True)
an_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
an_r2=an_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

an=pd.concat([an_r1,an_r2], axis=1)[:200000]







##secondary_strcture

ang_ssr1=pd.read_csv('data/angii/replica_1/ICL2.xvg', delim_whitespace=True, comment='#')
ang_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']
ang_ssr1=ang_ssr1[:400000]

ang_ssr2=pd.read_csv('data/angii/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
ang_ssr2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']
ang_ssr2=ang_ssr2[:400000]

ang_ssr2=ang_ssr2[['A_Helix','Th_Helix', 'Fiv_Helix' ]].sum(axis=1)/11
ang_ssr1=ang_ssr1[['A_Helix','Th_Helix']].sum(axis=1)/11
ang_ss=pd.concat([ang_ssr1, ang_ssr2], axis=1).mean(axis=1)
ang_ss_err=(pd.concat([ang_ssr1, ang_ssr2], axis=1)).std(axis=1)


an_ssr1= pd.read_csv('data/agonist_nanobody/replica_1/ICL2.xvg', delim_whitespace=True, comment='#')
an_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']
an_ssr1=an_ssr1[:400000]

an_ssr2= pd.read_csv('data/agonist_nanobody/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
an_ssr2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']
an_ssr2=an_ssr2[:400000]

an_ssr2=an_ssr2[['A_Helix','Th_Helix' ]].sum(axis=1)/11
an_ssr1=an_ssr1[['A_Helix','Th_Helix']].sum(axis=1)/11
an_ss=pd.concat([an_ssr1, an_ssr2], axis=1).mean(axis=1)
an_ss_err=(pd.concat([an_ssr1, an_ssr2], axis=1)).std(axis=1)


n_ssr1= pd.read_csv('data/nanobody/replica_1/ICL2.xvg', delim_whitespace=True, comment='#')
n_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']
n_ssr1=n_ssr1[:400000]

n_ssr2= pd.read_csv('data/nanobody/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
n_ssr2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']
n_ssr2=n_ssr2[:400000]

n_ssr2=n_ssr2[['A_Helix','Th_Helix' ]].sum(axis=1)/11
n_ssr1=n_ssr1[['A_Helix','Th_Helix']].sum(axis=1)/11
n_ss=pd.concat([n_ssr1, n_ssr2], axis=1).mean(axis=1)
n_ss_err=(pd.concat([n_ssr1, n_ssr2], axis=1)).std(axis=1)


s1i8_ssr1= pd.read_csv('data/s1i8/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
s1i8_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'B-Bridge','Turn', 'A_Helix', 'Fiv_Helix', 'Th_Helix']
#s1i8_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']
s1i8_ssr1=s1i8_ssr1[:400000]


s1i8_ssr2= pd.read_csv('data/s1i8/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
s1i8_ssr2.columns=['time', 'structure', 'coil','B-sheet','B_bridge', 'Bend', 'Turn', 'A_Helix','Th_Helix']
s1i8_ssr2=s1i8_ssr2[:400000]

s1i8_ssr2=s1i8_ssr2[['A_Helix','Th_Helix']].sum(axis=1)/11
s1i8_ssr1=s1i8_ssr1[['A_Helix','Fiv_Helix','Th_Helix']].sum(axis=1)/11
s1i8_ss=pd.concat([s1i8_ssr1, s1i8_ssr2], axis=1).mean(axis=1)
s1i8_ss_err=(pd.concat([s1i8_ssr1, s1i8_ssr2], axis=1)).std(axis=1)

print(s1i8_ss)
print(s1i8_ss_err)

delta_fyay=[16.509851568627454, 3.890564117647055, -15.710935098039215, 5.308243921568627]


time_ang=np.linspace(0,2000,len(ang_r1[['TM1-TM6']]))
time_s1i8=np.linspace(0,2000,len(s1i8_r1[['TM1-TM6']]))
time_n=np.linspace(0,2000,len(n_r1[['TM1-TM6']]))
time_an=np.linspace(0,2000,len(an_r1[['TM1-TM6']]))

time_ang_ss=np.linspace(0,2000,len(ang_ss))
time_a_ss=np.linspace(0,2000,len(s1i8_ss))
time_n_ss=np.linspace(0,2000,len(n_ss))
time_an_ss=np.linspace(0,2000,len(an_ss))

fyay=[19.70,19.50,29.77,17.30]

#exp=[33.48,25.57,23.65,22.56] 6DO1
exp=[32.656,25.796,23.422,22.235] #6OS0

window = 500
width=75
start=2150
sp = 120

ax=plt.subplot(2,4,2)
ax.plot(time_ang,(ang_r1[['TM1-TM6']].rolling(window).mean()*10),color='tab:blue',label='AT1R + AngII')
ax.plot(time_s1i8,(s1i8_r1[['TM1-TM6']].rolling(window).mean()*10),color='tab:red', label='AT1R + S1i8')
ax.plot(time_an,(an_r1[['TM1-TM6']].rolling(window).mean()*10), color='tab:green', label='AT1R + S1I8 + Nanobody')
ax.plot(time_n,(n_r1[['TM1-TM6']].rolling(window).mean()*10), color='tab:purple', label='AT1R + Nanobody')

ax.axhline(y=32.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
#ax.legend(loc='best', fontsize=5)
ax.set_ylim(17,36)
ax.set_xlim(0,2000)
#leg= ax.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-0.2,1.15), markerscale=7, columnspacing=1, handletextpad=0.4, handlelength=2, fontsize=10)
ax.yaxis.set_major_locator(MultipleLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('TM1-TM6 Dist. ($\AA$)', fontsize=11)
ax.set_xlim(0,2000)
#ax.set_xlabel('Time (ns)', fontsize=11)
ax.set_xlabel('Time (ns)', fontsize=11)
rect = Rectangle((2056,17), 550, 19, clip_on=False, ec='k', fill=False)
ax.add_patch(rect)

box_parts = ax.boxplot((ang[['TM1-TM6']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax.boxplot((s1i8[['TM1-TM6']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax.boxplot((n[['TM1-TM6']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:purple', clip_on=False)

box_parts = ax.boxplot((an[['TM1-TM6']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)



ax1=plt.subplot(2,4,3)
ax1.plot(time_ang,(ang_r1[['TM1-ICL2']].rolling(window).mean()*10),color='tab:blue',label='AT1R + AngII')
ax1.plot(time_s1i8,(s1i8_r1[['TM1-ICL2']].rolling(window).mean()*10),color='tab:red', label='AT1R + S1i8')
ax1.plot(time_an,(an_r1[['TM1-ICL2']].rolling(window).mean()*10), color='tab:green', label='AT1R + S1I8 + Nanobody')
ax1.plot(time_n,(n_r1[['TM1-ICL2']].rolling(window).mean()*10), color='tab:purple', label='AT1R + Nanobody')
#ax1.set_xticklabels(b,rotation=0,zorder=100)
ax1.axhline(y=19.50, linestyle='--', lw=1.5, color='0.5')
ax1.axhline(y=exp[1], linestyle='--', lw=1.5, color='tab:orange')
#ax1.text(-0.15, 20, 'AT1R/-/-$_{Exp}$', ha='center', fontsize=9, fontname='sans-serif')
#ax1.text(-0.15, 26, 'AT1R/-/-$_{Exp}$', ha='center', fontsize=9, fontname='sans-serif')
#ax1.set_xticks(b1)
ax1.set_ylim(17,30.5)
ax1.set_xlim(0,2000)
ax1.set_ylabel('TM1-ICL2 Dist. ($\AA$)', fontsize=11)
ax1.set_xlabel('Time (ns)', fontsize=11)
ax1.yaxis.set_major_locator(MultipleLocator(2))
ax1.yaxis.set_minor_locator(AutoMinorLocator(2))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax1.set_yticks([ 20, 25], minor=True)
#leg=ax1.legend(ncol=3,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(2.2,1.15), markerscale=8 ,columnspacing=1, handletextpad=1, handlelength=1, fontsize=15)
rect = Rectangle((2056,17), 550, 13.5, clip_on=False, ec='k', fill=False)
ax1.add_patch(rect)
#for i in leg.legendHandles:
#    i.set_linewidth(3)


box_parts = ax1.boxplot((ang[['TM1-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax1.boxplot((s1i8[['TM1-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax1.boxplot((n[['TM1-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:purple', clip_on=False)

box_parts = ax1.boxplot((an[['TM1-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)


ax2=plt.subplot(2,4,4)
ax2.plot(time_ang,(ang_r1[['TM5-ICL2']].rolling(window).mean()*10),color='tab:blue',label='AT1R + AngII')
ax2.plot(time_s1i8,(s1i8_r1[['TM5-ICL2']].rolling(window).mean()*10),color='tab:red', label='AT1R + S1i8')
ax2.plot(time_an,(an_r1[['TM5-ICL2']].rolling(window).mean()*10), color='tab:green', label='AT1R + S1I8 + Nanobody')
ax2.plot(time_n,(n_r1[['TM5-ICL2']].rolling(window).mean()*10), color='tab:purple', label='AT1R + Nanobody')
ax2.set_xlim(0,2000)
ax2.set_xlabel('Time (ns)', fontsize=11)
ax2.axhline(y=exp[2], linestyle='--', lw=1.5, color='tab:orange')
ax2.axhline(y=29.77, linestyle='--', lw=1.5, color='0.5')
#ax2.text(0.15, 24, 'AT1R/-/-$_{Exp}$', ha='center', fontsize=9, fontname='sans-serif')
#ax2.text(-0.15, 30, 'AT1R/-/-$_{Exp}$', ha='center', fontsize=9, fontname='sans-serif')
ax2.set_ylim(18,31)
ax2.set_xlabel('Time (ns)', fontsize=11)
ax2.set_ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=11)
ax2.yaxis.set_major_locator(MultipleLocator(2))
ax2.yaxis.set_minor_locator(AutoMinorLocator(2))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax1.set_yticks([ 20, 25], minor=True)
rect = Rectangle((2056,18), 550, 13, clip_on=False, ec='k', fill=False)
ax2.add_patch(rect)
box_parts = ax2.boxplot((ang[['TM5-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax2.boxplot((s1i8[['TM5-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax2.boxplot((n[['TM5-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:purple', clip_on=False)

box_parts = ax2.boxplot((an[['TM5-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)



ax3=plt.subplot(2,4,6)
ax3.plot(time_ang,(ang_r1[['TM6-H8']].rolling(window).mean()*10),color='tab:blue',label='AT1R + AngII')
ax3.plot(time_s1i8,(s1i8_r1[['TM6-H8']].rolling(window).mean()*10),color='tab:red', label='AT1R + S1i8')
ax3.plot(time_an,(an_r1[['TM6-H8']].rolling(window).mean()*10), color='tab:green', label='AT1R + S1I8 + Nanobody')
ax3.plot(time_n,(n_r1[['TM6-H8']].rolling(window).mean()*10), color='tab:purple', label='AT1R + Nanobody')
ax3.set_ylabel( 'TM6-H8 Dist. ($\AA$)', fontsize=11)
ax3.axhline(y=17.30, linestyle='--', lw=1.5, color='0.5')
ax3.axhline(y=exp[3], linestyle='--', lw=1.5, color='tab:orange')
ax3.set_ylim(10,26)
ax3.set_xlim(0,2000)
ax3.set_xlabel('Time (ns)', fontsize=11)
ax3.yaxis.set_major_locator(MultipleLocator(5))
#ax3.set_yticks([10,15,20,25])
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))
rect = Rectangle((2056,10), 550, 16, clip_on=False, ec='k', fill=False)
ax3.add_patch(rect)
box_parts = ax3.boxplot((ang[['TM6-H8']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax3.boxplot((s1i8[['TM6-H8']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax3.boxplot((n[['TM6-H8']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:purple', clip_on=False)

box_parts = ax3.boxplot((an[['TM6-H8']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)

ax4=plt.subplot(2,4,7)
ax4.plot(time_ang,(ang_r1[['TM3-TM6-ASP241']].rolling(window).mean()*10),color='tab:blue',label='AT1R + AngII')
ax4.plot(time_s1i8,(s1i8_r1[['TM3-TM6-ASP241']].rolling(window).mean()*10),color='tab:red', label='AT1R + S1i8')
ax4.plot(time_an,(an_r1[['TM3-TM6-ASP241']].rolling(window).mean()*10), color='tab:green', label='AT1R + S1I8 + Nanobody')
ax4.plot(time_n,(n_r1[['TM3-TM6-ASP241']].rolling(window).mean()*10), color='tab:purple', label='AT1R + Nanobody')
ax4.set_ylabel( 'TM3-TM6 Dist. ($\AA$)', fontsize=11)
ax4.axhline(y=9.12, linestyle='--', lw=1.5, color='0.5')
ax4.axhline(y=17.67, linestyle='--', lw=1.5, color='tab:orange')
ax4.set_ylim(6,23)
ax4.set_xlim(0,2000)
ax4.set_xlabel('Time (ns)', fontsize=11)
ax4.yaxis.set_major_locator(MultipleLocator(5))
#ax3.set_yticks([10,15,20,25])
ax4.yaxis.set_minor_locator(AutoMinorLocator(5))
ax4.xaxis.set_minor_locator(AutoMinorLocator(5))

rect = Rectangle((2056,6), 550, 17, clip_on=False, ec='k', fill=False)
ax4.add_patch(rect)
box_parts = ax4.boxplot((ang[['TM3-TM6-ASP241']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax4.boxplot((s1i8[['TM3-TM6-ASP241']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax4.boxplot((n[['TM3-TM6-ASP241']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:purple', clip_on=False)

box_parts = ax4.boxplot((an[['TM3-TM6-ASP241']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)



time_s1i8_ss=np.linspace(0,2000,len(s1i8_ssr1))
#time_p=np.linspace(0,2000,len(ss_p))
time_n_ss=np.linspace(0,2000,len(n_ssr1))
time_an_ss=np.linspace(0,2000,len(an_ssr1))
time_ang_ss=np.linspace(0,2000,len(ang_ssr1))
ax5=plt.subplot(2,4,8)
ax5.plot(time_ang_ss,ang_ssr1.rolling(window).mean(), color='tab:blue', label='SOPC + AngII')
#plt.fill_between(time_ang,0,ang_ss.rolling(window).mean()+ang_ss_err.rolling(window).mean(), color='tab:blue', alpha=0.1)
ax5.plot(time_s1i8_ss,s1i8_ssr1.rolling(window).mean(), color='tab:red', label='SOPC + S1I8')
ax5.plot(time_an_ss,an_ssr1.rolling(window).mean(), color='tab:purple', label='SOPC + S1I8 + Nanobody')
ax5.plot(time_n_ss,n_ssr1.rolling(window).mean(), color='tab:green', label='SOPC + Nanobody')
#ax4.set_xticklabels(d,
#rotation=0,zorder=100)
#ax4.set_xticks(d1)
#print('sopc=',ss_sopc,'popc=',ss_popc,'dmpc=',ss_dmpc)
ax5.set_xlim(0,2000)
ax5.set_xlabel('Time (ns)', fontsize=11)
ax5.set_ylabel(r'ICL2 $\alpha$-helicity, $f_{\alpha}$', fontsize=11)
ax5.axhline(y=0.66, linestyle='--', lw=1.5, color='tab:orange')#, label='6OS0, Active')
ax5.axhline(y=0.0, linestyle='--', lw=1.5, color='0.5')#, label='4YAY, Inactive')
ax5.set_ylim(-0.05,0.7)
ax5.yaxis.set_major_locator(MultipleLocator(4))
ax5.yaxis.set_minor_locator(AutoMinorLocator(2))
ax5.xaxis.set_minor_locator(AutoMinorLocator(5))
rect = Rectangle((2056,-0.05), 550, 0.75, clip_on=False, ec='k', fill=False)
ax5.add_patch(rect)
leg=ax5.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-1,2.8), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

for i in leg.legendHandles:
    i.set_linewidth(2)

box_parts = ax5.boxplot((ang_ss[-100000:].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax5.boxplot((s1i8_ss[-100000:].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red', clip_on=False)

box_parts = ax5.boxplot((n_ss[-100000:].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+2*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:purple', clip_on=False)

box_parts = ax5.boxplot((an_ss[-100000:].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+3*sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)

for line in plt.gca().get_lines(): line.set_clip_on(False)

ax.text(-0.24, 1.03, 'a', transform=ax.transAxes, ha='center', fontsize=14, fontweight='bold')
ax1.text(-0.24, 1.03, 'b', transform=ax1.transAxes, ha='center', fontsize=14, fontweight='bold')
ax2.text(-0.24, 1.03, 'c', transform=ax2.transAxes, ha='center', fontsize=14, fontweight='bold')
ax3.text(-0.24, 1.03, 'd', transform=ax3.transAxes, ha='center', fontsize=14, fontweight='bold')
ax4.text(-0.24, 1.03, 'e', transform=ax4.transAxes, ha='center', fontsize=14, fontweight='bold')
ax5.text(-0.24, 1.03, 'f', transform=ax5.transAxes, ha='center', fontsize=14, fontweight='bold')
fig = plt.gcf()

#left_top = plt.subplot(2,4,1)
#left_bottom = plt.subplot(2,4,5)
left_top = plt.axes([-0.03, 0.47, 0.3, 0.52])
left_bottom = plt.axes([-0.19, 0.01, 0.6, 0.98])
left_top.axis('off')
left_bottom.axis('off')
im1 = left_bottom.imshow(illustr, aspect='equal')
#im2 = left_bottom.imshow(bottomview, aspect='equal')

plt.subplots_adjust(top=0.90, bottom=0.115, left=0.02, right=0.95, hspace=0.43, wspace=0.7)
#plt.Figure.set_size_inches(fig,(7.5, 4.2))

#plt.subplots_adjust(top=0.94, bottom=0.115, left=0.08, right=0.965, hspace=0.43, wspace=0.5)
plt.Figure.set_size_inches(fig,(11, 4.2))
plt.savefig('Figure_5.png', dpi=300)
#plt.savefig('time_evolution.svg', dpi=900, bbox_inches='tight')
plt.close()
