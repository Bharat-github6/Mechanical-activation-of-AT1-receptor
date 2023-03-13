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

sopc_r1= pd.read_csv('data/ST_0/SOPC/replica_1/Deer_analysis_2us', delim_whitespace=True)
sopc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
sopc_r1=sopc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]


sopc_r2= pd.read_csv('data/ST_0/SOPC/replica_2/Deer_analysis2us', delim_whitespace=True)
sopc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
sopc_r2=sopc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
sopc=pd.concat([sopc_r1, sopc_r2], axis=1)
sopc=sopc[:197500]


st5_r1= pd.read_csv('data/ST_5/replica_1/Deer_analysis_2us', delim_whitespace=True)
st5_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
st5_r1=st5_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

st5_r2= pd.read_csv('data/ST_5/replica_2/Deer_analysis_2us', delim_whitespace=True)
st5_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
st5_r2=st5_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
st5=pd.concat([st5_r1, st5_r2], axis=1)
st5=st5[-20000:]

st10_r1= pd.read_csv('data/ST_10/replica_1/Deer_analysis_2us', delim_whitespace=True)
st10_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
st10_r1=st10_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

st10_r2= pd.read_csv('data/ST_10/replica_2/Deer_analysis_2us', delim_whitespace=True)
st10_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
st10_r2=st10_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
st10=pd.concat([st10_r1, st10_r2], axis=1)
st10=st10[-20000:]

st15_r1= pd.read_csv('data/ST_15/replica_1/Deer_analysis_2us', delim_whitespace=True)
st15_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
st15_r1=st15_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

st15_r2= pd.read_csv('data/ST_15/replica_2/Deer_analysis_2us', delim_whitespace=True)
st15_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
st15_r2=st15_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
st15=pd.concat([st15_r1, st15_r2], axis=1)
st15=st15[-20000:]





st20_r1=pd.read_csv('data/ST_20/replica_1/Deer_analysis_2us', delim_whitespace=True)
st20_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
st20_r1=st20_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
st20_r1=st20_r1[-20000:]
st20_r1=st20_r1.reset_index(drop=True)

st20_r2= pd.read_csv('data/ST_20/replica_2/Deer_analysis_part2', delim_whitespace=True)
st20_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
st20_r2=st20_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
st20_r2=st20_r2[-20000:]
st20_r2=st20_r2.reset_index(drop=True)
st20=pd.concat([st20_r1, st20_r2], axis=1)



##ICL2
st5_ssr1=pd.read_csv('data/ST_5/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
st5_ssr1.columns=['time', 'structure', 'coil', 'B_bridge','Bend', 'Turn', 'A_Helix','Th_Helix']
st5_ssr1=st5_ssr1[-40000:]

st5_ssr2=pd.read_csv('data/ST_5/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
st5_ssr2.columns=['time', 'structure', 'coil','Bend', 'Turn', 'A_Helix','Th_Helix']
st5_ssr2=st5_ssr2[-40000:]

st5_ssr1=st5_ssr1[['A_Helix','Th_Helix' ]].sum(axis=1)/11
st5_ssr2=st5_ssr2[['A_Helix','Th_Helix' ]].sum(axis=1)/11
st5_ss=pd.concat([st5_ssr1, st5_ssr2], axis=1).mean(axis=1).mean()
st5_ss_err=pd.concat([st5_ssr1, st5_ssr2], axis=1).mean(axis=1).std()




st10_ssr1=pd.read_csv('data/ST_10/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
st10_ssr1.columns=['time', 'structure', 'coil','Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']
st10_ssr1=st10_ssr1[-40000:]

st10_ssr2=pd.read_csv('data/ST_10/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
st10_ssr2.columns=['time', 'structure', 'coil','Bend', 'Turn', 'A_Helix','Th_Helix']
st10_ssr2=st10_ssr2[-40000:]

st10_ssr1=st10_ssr1[['A_Helix','Th_Helix','Fiv_Helix' ]].sum(axis=1)/11
st10_ssr2=st10_ssr2[['A_Helix','Th_Helix' ]].sum(axis=1)/11
st10_ss=pd.concat([st10_ssr1, st10_ssr2], axis=1).mean(axis=1).mean()
st10_ss_err=pd.concat([st10_ssr1, st10_ssr2], axis=1).mean(axis=1).std()


st15_ssr1=pd.read_csv('data/ST_15/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
st15_ssr1.columns=['time', 'structure', 'coil','Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']
st15_ssr1=st15_ssr1[-40000:]

st15_ssr2=pd.read_csv('data/ST_15/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
st15_ssr2.columns=['time', 'structure', 'coil','Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']
st15_ssr2=st15_ssr2[-40000:]

st15_ssr1=st15_ssr1[['A_Helix','Th_Helix','Fiv_Helix' ]].sum(axis=1)/11
st15_ssr2=st15_ssr2[['A_Helix','Th_Helix','Fiv_Helix' ]].sum(axis=1)/11
st15_ss=pd.concat([st15_ssr1, st15_ssr2], axis=1).mean(axis=1).mean()
st15_ss_err=pd.concat([st15_ssr1, st15_ssr2], axis=1).mean(axis=1).std()


st20_ssr1=pd.read_csv('data/ST_20/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
st20_ssr1.columns=['time', 'structure', 'coil','B-bridge','Bend', 'Turn', 'A_Helix','Th_Helix']
st20_ssr1=st20_ssr1[-40000:]

st20_ssr1=st20_ssr1[['A_Helix','Th_Helix']].sum(axis=1)
st20_ss=(st20_ssr1*0.09).mean()
st20_ss_err=(st20_ssr1*0.09).std()




sopc_ssr1=pd.read_csv('data/ST_0/SOPC/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
sopc_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']

sopc_ssr2=pd.read_csv('data/ST_0/SOPC/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
sopc_ssr2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']

sopc_ssr1=sopc_ssr1[['A_Helix','Th_Helix', 'Fiv_Helix' ]].sum(axis=1)/11
sopc_ssr2=sopc_ssr2[['A_Helix','Th_Helix']].sum(axis=1)/11
sopc_ss=pd.concat([sopc_ssr1, sopc_ssr2], axis=1).mean(axis=1)
sopc_ss_err=(pd.concat([sopc_ssr1, sopc_ssr2], axis=1)).std(axis=1)
sopc_ss=sopc_ss[:400000]
sopc_ss_err=sopc_ss_err[:400000]

sopc_ss=sopc_ss[-40000:]
sopc_ss_err=sopc_ss_err[-40000:]

exp=[33.48,25.57,23.65,22.56]

delta_fyay=[16.509851568627454, 3.890564117647055, -15.710935098039215, 5.308243921568627]

fyay=[19.70,19.50,29.77,17.30]

#exp=[33.48,25.57,23.65,22.56] 6DO1
exp=[32.656,25.796,23.422,22.235] #6OS0


window = 500

width=5
ax=plt.subplot(2,3,1)
ax.bar(0,(sopc[['TM1-TM6']][180000:].mean(axis=1)*10).mean(), width,yerr=(sopc[['TM1-TM6']][180000:].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='0mN/m')
ax.bar(5,(st5[['TM1-TM6']].mean(axis=1)*10).mean(), width,yerr=(st5[['TM1-TM6']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='5mN/m')
ax.bar(10,(st10[['TM1-TM6']].mean(axis=1)*10).mean(), width,yerr=(st10[['TM1-TM6']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='10mN/m')
ax.bar(15,(st15[['TM1-TM6']].mean(axis=1)*10).mean(), width,yerr=(st15[['TM1-TM6']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='15mN/m')
ax.bar(20,(st20[['TM1-TM6']].mean(axis=1)*10).mean(), width,yerr=(st20[['TM1-TM6']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='20mN/m')
ax.axhline(y=exp[0], linestyle='dashed', color='tab:orange',lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
ax.set_xlabel('Tension (mN/m)', fontsize=11)
ax.set_ylim(17,36)
ax.set_xticks([0,5,10,15,20])
ax.set_ylabel('TM1-TM6 Dist. ($\AA$)', fontsize=11)
#ax.set_xlabel('Tension (mN/m)', fontsize=11)
ax.yaxis.set_major_locator(MaxNLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))



ax1=plt.subplot(2,3,2)
ax1.bar(0,(sopc[['TM1-ICL2']].mean(axis=1)*10).mean(), width,yerr=(sopc[['TM1-ICL2']][180000:].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='0mN/m')
ax1.bar(5,(st5[['TM1-ICL2']].mean(axis=1)*10).mean(), width,yerr=(st5[['TM1-ICL2']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='5mN/m')
ax1.bar(10,(st10[['TM1-ICL2']].mean(axis=1)*10).mean(), width,yerr=(st10[['TM1-ICL2']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='10mN/m')
ax1.bar(15,(st15[['TM1-ICL2']].mean(axis=1)*10).mean(), width,yerr=(st15[['TM1-ICL2']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='15mN/m')
ax1.bar(20,(st20[['TM1-ICL2']].mean(axis=1)*10).mean(), width,yerr=(st20[['TM1-ICL2']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='20mN/m')
ax1.axhline(y=19.50, linestyle='--', lw=1.5, color='0.5')
ax1.axhline(y=25.57, linestyle='--', lw=1.5, color='tab:orange')
ax1.set_xlabel('Tension (mN/m)', fontsize=11)
ax1.set_ylim(17,28)
ax1.set_ylabel('TM1-ICL2 Dist. ($\AA$)', fontsize=11)
ax1.set_xticks([0,5,10,15,20])
ax1.yaxis.set_major_locator(MultipleLocator(2))
ax1.yaxis.set_minor_locator(AutoMinorLocator(2))
#ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax1.set_yticks([ 20, 25], minor=True)
#leg=ax1.legend(ncol=3,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(2.2,1.15), markerscale=8 ,columnspacing=1, handletextpad=1, handlelength=1, fontsize=15)

#for i in leg.legendHandles:
#    i.set_linewidth(3)

ax2=plt.subplot(2,3,3)
ax2.bar(0,(sopc[['TM5-ICL2']][180000:].mean(axis=1)*10).mean(), width,yerr=(sopc[['TM5-ICL2']][180000:].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='0mN/m')
ax2.bar(5,(st5[['TM5-ICL2']].mean(axis=1)*10).mean(), width,yerr=(st5[['TM5-ICL2']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='5mN/m')
ax2.bar(10,(st10[['TM5-ICL2']].mean(axis=1)*10).mean(), width,yerr=(st10[['TM5-ICL2']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='10mN/m')
ax2.bar(15,(st15[['TM5-ICL2']].mean(axis=1)*10).mean(), width,yerr=(st15[['TM5-ICL2']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='15mN/m')
ax2.bar(20,(st20[['TM5-ICL2']].mean(axis=1)*10).mean(), width,yerr=(st20[['TM5-ICL2']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='20mN/m')
ax2.axhline(y=23.65, linestyle='--', lw=1.5, color='tab:orange')
ax2.axhline(y=29.77, linestyle='--', lw=1.5, color='0.5')
ax2.set_ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=11)
ax2.set_xlabel('Tension (mN/m)', fontsize=11)
ax2.set_xticks([0,5,10,15,20])
ax2.set_ylim(20,31)
ax2.yaxis.set_major_locator(MultipleLocator(2))
ax2.yaxis.set_minor_locator(AutoMinorLocator(2))
#ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax1.set_yticks([ 20, 25], minor=True)

ax3=plt.subplot(2,3,4)
ax3.bar(0,(sopc[['TM6-H8']][180000:].mean(axis=1)*10).mean(), width,yerr=(sopc[['TM6-H8']][180000:].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='0mN/m')
ax3.bar(5,(st5[['TM6-H8']].mean(axis=1)*10).mean(), width,yerr=(st5[['TM6-H8']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='5mN/m')
ax3.bar(10,(st10[['TM6-H8']].mean(axis=1)*10).mean(), width,yerr=(st10[['TM6-H8']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='10mN/m')
ax3.bar(15,(st15[['TM6-H8']].mean(axis=1)*10).mean(), width,yerr=(st15[['TM6-H8']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='15mN/m')
ax3.bar(20,(st20[['TM6-H8']].mean(axis=1)*10).mean(), width,yerr=(st20[['TM6-H8']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='20mN/m')
ax3.axhline(y=17.30, linestyle='--', lw=1.5, color='0.5')
ax3.axhline(y=22.56, linestyle='--', lw=1.5, color='tab:orange')
ax3.set_ylim(10,26)
ax3.set_xticks([0,5,10,15,20])
ax3.set_ylabel('TM6-H8 Dist. ($\AA$)', fontsize=11)
ax3.yaxis.set_major_locator(MultipleLocator(5))
ax3.set_xlabel('Tension (mN/m)', fontsize=11)
#ax3.set_yticks([10,15,20,25])
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
#ax3.xaxis.set_minor_locator(AutoMinorLocator(5))



ax7=plt.subplot(2,3,5)
ax7.bar(0,(sopc[['TM3-TM6-ASP241']][180000:].mean(axis=1)*10).mean(), width,yerr=(sopc[['TM3-TM6-ASP241']][180000:].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='0mN/m')
ax7.bar(5,(st5[['TM3-TM6-ASP241']].mean(axis=1)*10).mean(), width,yerr=(st5[['TM3-TM6-ASP241']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='5mN/m')
ax7.bar(10,(st10[['TM3-TM6-ASP241']].mean(axis=1)*10).mean(), width,yerr=(st10[['TM3-TM6-ASP241']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='10mN/m')
ax7.bar(15,(st15[['TM3-TM6-ASP241']].mean(axis=1)*10).mean(), width,yerr=(st15[['TM3-TM6-ASP241']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='15mN/m')
ax7.bar(20,(st20[['TM3-TM6-ASP241']].mean(axis=1)*10).mean(), width,yerr=(st20[['TM3-TM6-ASP241']].std(axis=1)*10).mean(), color='lightblue',edgecolor='black', label='20mN/m')
ax7.axhline(y=9.12, linestyle='--', lw=1.5, color='0.5')
ax7.axhline(y=17.67, linestyle='--', lw=1.5, color='tab:orange')
ax7.set_ylim(6,23)
ax7.set_ylabel('TM3-TM6 Dist. ($\AA$)', fontsize=11)
ax7.set_xticks([0,5,10,15,20])
ax7.set_xlabel('Tension (mN/m)', fontsize=11)
ax7.yaxis.set_major_locator(MaxNLocator(4))
ax7.yaxis.set_minor_locator(AutoMinorLocator(5))
#ax.set_ylabel('TM3-TM6(ASP) Dist. ($\AA$)', fontsize=11)

ax5=plt.subplot(2,3,6)
ax5.bar(0,sopc_ss,width,yerr=sopc_ss_err,color='lightblue',edgecolor='black', label='0mN/m')
ax5.bar(5,st5_ss,width,yerr=st5_ss_err,color='lightblue', edgecolor='black', label='5mN/m')
ax5.bar(10,st10_ss,width,yerr=st10_ss_err,color='lightblue',edgecolor='black', label='10mN/m')
ax5.bar(15,st15_ss,width,yerr=st15_ss_err,color='lightblue',edgecolor='black', label='15mN/m')
ax5.bar(20,st20_ss,width,yerr=st20_ss_err,color='lightblue',edgecolor='black', label='20mN/m')
ax5.axhline(y=0.65, linestyle='--', lw=1.5, color='tab:orange')
ax5.set_ylim(0,0.7)
ax5.set_xticks([0,5,10,15,20])
ax5.set_xlabel('Tension (mN/m)', fontsize=11)
ax5.set_ylabel(r'ICL2 $\alpha$-helicity, $f_{\alpha}$', fontsize=11)
ax5.yaxis.set_major_locator(MaxNLocator(4))
ax5.yaxis.set_minor_locator(AutoMinorLocator(3))


#x_label=['0','5','10','15','20']
#x=[0,5,10,15,20]
#st_thickness=[41.05,40.35,38.45,37.25,35.5]
#thickness_err=[0.77,0.35,0.35,0.63,0.98]
#popc_thickness=38.2
#dmpc_thickness=35.6
#pe_pc_thickness=42.85
#ax6=plt.subplot(2,4,8)
#ax6.plot(x,st_thickness,marker='s',markersize=4,color='tab:blue', label='SOPC')
#ax6.plot(0,popc_thickness,marker='>',markersize=4, color='tab:green', label='POPC')
#ax6.plot(0,dmpc_thickness,marker='D', markersize=4,color='tab:red', label='DMPC')
#ax6.plot(0,pe_pc_thickness,marker='o',markersize=4, color='grey', label='SOPC:SOPE')
#plt.errorbar(x,st_thickness, yerr=thickness_err ,color='tab:blue')
#plt.errorbar(0,38.4, yerr=0.14, color='tab:green')
#plt.errorbar(0,33.87, yerr=0.20,color='tab:red')
#plt.errorbar(0,42.25, yerr=0.51,color='grey')
##plt.xticks(x,x_label)
#plt.ylabel('Bilayer Thicknes', fontsize=10)
#ax6.text(1.0,33.5, 'DMPC', color='tab:red', fontsize=11, fontweight='medium')
#ax6.text(1.0,37.8, 'POPC', color='tab:green', fontsize=11, fontweight='medium')
#ax6.text(12.5,39.5, 'SOPC', color='tab:blue', fontsize=11, fontweight='medium')
#ax6.text(1.0,41.9, 'SOPC:SOPE', color='grey', fontsize=11, fontweight='medium')
#ax6.set_ylim(33,44)
#ax6.set_ylabel('Bilayer thickness ($\AA$)', fontsize=11)
#ax6.xaxis.set_major_locator(MultipleLocator(5))
##ax4.yaxis.set_minor_locator(AutoMinorLocator(5))
#ax6.yaxis.set_major_locator(MultipleLocator(2))
#ax6.yaxis.set_minor_locator(AutoMinorLocator(2))
#ax6.set_xlabel('Tension (mN/m)', fontsize=11)



#leg=ax1.legend(ncol=1,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(1.9,1.1), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

#for i in leg.legendHandles:
#    i.set_linewidth(2)


ax.text(-0.21, 1.05, 'a', transform=ax.transAxes, ha='center', fontsize=14, fontweight='bold')
ax1.text(-0.22, 1.05, 'b', transform=ax1.transAxes, ha='center', fontsize=14, fontweight='bold')
ax2.text(-0.22, 1.05, 'c', transform=ax2.transAxes, ha='center', fontsize=14, fontweight='bold')
ax3.text(-0.21, 1.05, 'd', transform=ax3.transAxes, ha='center', fontsize=14, fontweight='bold')
ax7.text(-0.22, 1.05, 'e', transform=ax7.transAxes, ha='center', fontsize=14, fontweight='bold')
ax5.text(-0.22, 1.05, 'f', transform=ax5.transAxes, ha='center', fontsize=14, fontweight='bold')


fig = plt.gcf()
plt.subplots_adjust(top=0.92, bottom=0.115, left=0.1, right=0.975, hspace=0.43, wspace=0.5)
plt.Figure.set_size_inches(fig,(10, 4))

#plt.subplots_adjust(top=0.94, bottom=0.115, left=0.08, right=0.965, hspace=0.43, wspace=0.5)
#plt.Figure.set_size_inches(fig,(7.5, 4))
plt.savefig('Figure_2.png', dpi=300)
#plt.savefig('time_evolution.svg', dpi=900, bbox_inches='tight')
plt.close()
