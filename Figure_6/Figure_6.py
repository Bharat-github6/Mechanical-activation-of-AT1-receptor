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
#use('Agg')
font = {'family' : 'sans serif', 'size' : '10'}
rc('font', **font)
mathfont = {'fontset' : 'stix' ,'default' : 'it', 'it' : 'serif:italic'}
rc('mathtext', **mathfont)
rc('lines', linewidth=0.9)

simplify = {'simplify_threshold' : '0.5'}
rc('path', **simplify)
matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)





pepc_r1= pd.read_csv('data_Figure_6/PE_PC/replica_1/Deer_analysis_2us', delim_whitespace=True)
pepc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
pepc_r1=pepc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]


pepc_r2= pd.read_csv('data_Figure_6/PE_PC/replica_2/Deer_analysis_2us', delim_whitespace=True)
pepc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
pepc_r2=pepc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
pepc=pd.concat([pepc_r1, pepc_r2], axis=1)[:200000]
pepc=pepc[-20000:]
pepc=pepc.reset_index(drop=True)


pepc_TM1_TM6=pepc[['TM1-TM6']].dropna().to_numpy().flatten()*10-19.70
pepc_TM1_ICL2=pepc[['TM1-ICL2']].dropna().to_numpy().flatten()*10-19.50
pepc_TM5_ICL2=pepc[['TM5-ICL2']].dropna().to_numpy().flatten()*10-29.77
pepc_TM6_H8=pepc[['TM6-H8']].dropna().to_numpy().flatten()*10-17.30
pepc_TM3_TM6=pepc[['TM3-TM6-ASP241']].dropna().to_numpy().flatten()*10-9.12

pepc=[pepc_TM1_TM6, pepc_TM1_ICL2,pepc_TM5_ICL2,pepc_TM6_H8,pepc_TM3_TM6]
#pepc_err=[pepc_TM1_TM6.std(), pepc_TM1_ICL2.std(),pepc_TM5_ICL2.std(),pepc_TM6_H8.std(),pepc_TM3_TM6.std()]


popc_r1= pd.read_csv('data_Figure_6/POPC/replica_1/Deer_analysis2us', delim_whitespace=True)
popc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
popc_r1=popc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

popc_r2= pd.read_csv('data_Figure_6/POPC/replica_2/Deer_analysis2us', delim_whitespace=True)
popc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
popc_r2=popc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

popc=pd.concat([popc_r1,popc_r2], axis=1)

popc=popc[:197500]
popc=popc[-20000:]
popc=popc.reset_index(drop=True)


popc_TM1_TM6=popc[['TM1-TM6']].dropna().to_numpy().flatten()*10-19.70
popc_TM1_ICL2=popc[['TM1-ICL2']].dropna().to_numpy().flatten()*10-19.50
popc_TM5_ICL2=popc[['TM5-ICL2']].dropna().to_numpy().flatten()*10-29.77
popc_TM6_H8=popc[['TM6-H8']].dropna().to_numpy().flatten()*10-17.30
popc_TM3_TM6=popc[['TM3-TM6-ASP241']].dropna().to_numpy().flatten()*10-9.12

popc=[popc_TM1_TM6, popc_TM1_ICL2,popc_TM5_ICL2,popc_TM6_H8,popc_TM3_TM6]



st10_r1= pd.read_csv('data_Figure_6/ST_10/replica_1/Deer_analysis_2us', delim_whitespace=True)
st10_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
st10_r1=st10_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

st10_r2= pd.read_csv('data_Figure_6/ST_10/replica_2/Deer_analysis_2us', delim_whitespace=True)
st10_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
st10_r2=st10_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
st10=pd.concat([st10_r1, st10_r2], axis=1)
st10=st10[-20000:]
st10=st10.reset_index(drop=True)

st10_TM1_TM6=st10[['TM1-TM6']].dropna().to_numpy().flatten()*10-19.70
st10_TM1_ICL2=st10[['TM1-ICL2']].dropna().to_numpy().flatten()*10-19.50
st10_TM5_ICL2=st10[['TM5-ICL2']].dropna().to_numpy().flatten()*10-29.77
st10_TM6_H8=st10[['TM6-H8']].dropna().to_numpy().flatten()*10-17.30
st10_TM3_TM6=st10[['TM3-TM6-ASP241']].dropna().to_numpy().flatten()*10-9.12

st10=[st10_TM1_TM6, st10_TM1_ICL2,st10_TM5_ICL2,st10_TM6_H8,st10_TM3_TM6]
#st10_err=[st10_TM1_TM6.std(), st10_TM1_ICL2.std(),st10_TM5_ICL2.std(),st10_TM6_H8.std(),st10_TM3_TM6.std()]

ang_r2= pd.read_csv('data_Figure_6/angii/replica_2/Deer_analysis2us', delim_whitespace=True)
ang_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
ang_r2=ang_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

ang_r1= pd.read_csv('data_Figure_6/angii/replica_1/Deer_analysis2us', delim_whitespace=True)
ang_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
ang_r1=ang_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

ang=pd.concat([ang_r1,ang_r2], axis=1)[:200000]
ang=ang[-20000:]

ang=ang.reset_index(drop=True)

ang_TM1_TM6=ang[['TM1-TM6']].dropna().to_numpy().flatten()*10-19.70
ang_TM1_ICL2=ang[['TM1-ICL2']].dropna().to_numpy().flatten()*10-19.50
ang_TM5_ICL2=ang[['TM5-ICL2']].dropna().to_numpy().flatten()*10-29.77
ang_TM6_H8=ang[['TM6-H8']].dropna().to_numpy().flatten()*10-17.30
ang_TM3_TM6=ang[['TM3-TM6-ASP241']].dropna().to_numpy().flatten()*10-9.12

ang=[ang_TM1_TM6,ang_TM1_ICL2,ang_TM5_ICL2,ang_TM6_H8,ang_TM3_TM6]
#ang_err=[ang_TM1_TM6.std(),ang_TM1_ICL2.std(),ang_TM5_ICL2.std(),ang_TM6_H8.std(),ang_TM3_TM6.std()]

#/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_agonist_only/ASPH74-125/production_run/descriptor
s1i8_r1= pd.read_csv('data_Figure_6/s1i8/replica_1/Deer_analysis2us', delim_whitespace=True)
s1i8_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
s1i8_r1=s1i8_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

s1i8_r2= pd.read_csv('data_Figure_6/s1i8/replica_2/Deer_analysis_2us', delim_whitespace=True)
s1i8_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
s1i8_r2=s1i8_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

s1i8=pd.concat([s1i8_r1,s1i8_r2], axis=1)[:200000]
s1i8=s1i8[-20000:]
s1i8=s1i8.reset_index(drop=True)

s1i8_TM1_TM6=s1i8[['TM1-TM6']].dropna().to_numpy().flatten()*10-19.70
s1i8_TM1_ICL2=s1i8[['TM1-ICL2']].dropna().to_numpy().flatten()*10-19.50
s1i8_TM5_ICL2=s1i8[['TM5-ICL2']].dropna().to_numpy().flatten()*10-29.77
s1i8_TM6_H8=s1i8[['TM6-H8']].dropna().to_numpy().flatten()*10-17.30
s1i8_TM3_TM6=s1i8[['TM3-TM6-ASP241']].dropna().to_numpy().flatten()*10-9.12

s1i8=[s1i8_TM1_TM6, s1i8_TM1_ICL2,s1i8_TM5_ICL2,s1i8_TM6_H8,s1i8_TM3_TM6]
#s1i8_err=[s1i8_TM1_TM6.std(),s1i8_TM1_ICL2.std(),s1i8_TM5_ICL2.std(),s1i8_TM6_H8.std(),s1i8_TM3_TM6.std()]

a=['TM1-TM6']
a1 = np.arange(len(a))  # the label locations
b=['TM1-ICL2']
b1 = np.arange(len(b))
c=['TM5-ICL2']
c1 = np.arange(len(c))
d=['TM6-H8']
d1 = np.arange(len(d))
e=['TM3-TM6']
e1=np.arange(len(e))
#protein.astype(int)
#print(protein)#protein=np.vectorize(protein)
x=['TM1-TM6','TM1-ICL2','TM5-ICL2','TM6-H8', 'TM3-TM6']
x1=np.arange(len(x))
width=0.125
sp = 0.16
ax=plt.subplot(1,1,1)
box_parts = ax.boxplot(st10, vert=True, positions=x1-sp, widths=[width,width,width,width,width], medianprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='lightblue')

box_parts = ax.boxplot(pepc, vert=True, positions=x1, widths=[width,width,width,width,width], medianprops=dict(color='k'), showfliers=False, patch_artist=True)
for patch in box_parts['boxes']:
    patch.set(facecolor='grey')

box_parts = ax.boxplot(popc, vert=True, positions=x1+sp, widths=[width,width,width,width,width], medianprops=dict(color='k'), showfliers=False, patch_artist=True)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green')

box_parts = ax.boxplot(s1i8, vert=True, positions=x1+2*sp, widths=[width,width,width,width,width], medianprops=dict(color='k'), showfliers=False, patch_artist=True)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:red')

box_parts = ax.boxplot(ang, vert=True, positions=x1+3*sp, widths=[width,width,width,width,width], medianprops=dict(color='k'), showfliers=False, patch_artist=True)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:purple')


# these lines below are just needed for labels
rect1=ax.bar(-20,0, width,align='edge', color='lightblue', edgecolor='black', label='SOPC + 10 mN/m', rasterized=True)
rect2=ax.bar(-20,0, width,align='edge', color='grey', edgecolor='black', label='SOPC:SOPE', rasterized=True)
rect2=ax.bar(-20,0, width,align='edge', color='tab:green', edgecolor='black', label='POPC', rasterized=True)
rect2=ax.bar(-20,0, width,align='edge', color='tab:red', edgecolor='black', label='SOPC + S1I8', rasterized=True)
rect2=ax.bar(-20,0, width,align='edge', color='tab:purple', edgecolor='black', label='SOPC + AngII', rasterized=True)

ax.set_xticks(x1)
ax.set_xticklabels(x,rotation=45,zorder=100)

ax.legend(ncol=2,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(0.45,1.36), markerscale=5 ,columnspacing=2, handletextpad=0.6, handlelength=0.6, fontsize=10)
#ax.set_yticklabels(rotation=0,fontsize=12)
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel( r'$\Delta$$d$ $(\AA$)', fontsize=12)
ax.set_xlim(-0.5,4.7)
#ax.set_ylim(-8,15)
ax.axhline(y=0.0, linestyle='--', lw=1.5, color='0.5')

fig = plt.gcf()
plt.subplots_adjust(top=0.8, bottom=0.22, left=0.19, right=0.97, hspace=0.4, wspace=0.2)
plt.Figure.set_size_inches(fig,(4, 3.5))
plt.savefig('Figure_6.png', dpi=900)
#plt.savefig('distinct_activation.svg', dpi=900)
