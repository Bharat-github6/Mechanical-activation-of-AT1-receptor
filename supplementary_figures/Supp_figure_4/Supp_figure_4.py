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


popc_r1= pd.read_csv('data_Supp_figure_4/popc_r1', delim_whitespace=True)
popc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
popc_r1=popc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

popc_r2= pd.read_csv('data_Supp_figure_4/popc_r2', delim_whitespace=True)
popc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
popc_r2=popc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

popc=pd.concat([popc_r1,popc_r2], axis=1)
time_popc=np.linspace(0,2000,len(popc))


sopc_r1= pd.read_csv('data_Supp_figure_4/sopc_r1', delim_whitespace=True)
sopc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
sopc_r1=sopc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]


sopc_r2= pd.read_csv('data_Supp_figure_4/sopc_r2', delim_whitespace=True)
sopc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
sopc_r2=sopc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
sopc=pd.concat([sopc_r1, sopc_r2], axis=1)

time_sopc=np.linspace(0,2000,len(sopc))

sopc_ssr1=pd.read_csv('data_Supp_figure_4/sopc_ICL2_r1.xvg', delim_whitespace=True, comment='#')
sopc_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']

sopc_ssr2=pd.read_csv('data_Supp_figure_4/sopc_ICL2_r2.xvg', delim_whitespace=True, comment='#')
sopc_ssr2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']

sopc_ssr1=sopc_ssr1[['A_Helix','Th_Helix', 'Fiv_Helix' ]].sum(axis=1)/11
sopc_ssr2=sopc_ssr2[['A_Helix','Th_Helix']].sum(axis=1)/11
sopc_ss=pd.concat([sopc_ssr1, sopc_ssr2], axis=1).mean(axis=1)
sopc_ss_err=(pd.concat([sopc_ssr1, sopc_ssr2], axis=1)).std(axis=1)
sopc_ss=sopc_ss[:400000]
sopc_ss_err=sopc_ss_err[:400000]


popc_ssr1=pd.read_csv('data_Supp_figure_4/popc_ICL2_r1.xvg', delim_whitespace=True, comment='#')
popc_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']


popc_ssr2=pd.read_csv('data_Supp_figure_4/popc_ICL2_r2.xvg', delim_whitespace=True, comment='#')
popc_ssr2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']

popc_ssr2=popc_ssr2[['A_Helix','Th_Helix', 'Fiv_Helix' ]].sum(axis=1)/11
popc_ssr1=popc_ssr1[['A_Helix','Th_Helix']].sum(axis=1)/11
popc_ss=pd.concat([popc_ssr1, popc_ssr2], axis=1).mean(axis=1)
popc_ss_err=(pd.concat([popc_ssr1, popc_ssr2], axis=1)).std(axis=1)
popc_ss=popc_ss[:400000]
popc_ss_err=popc_ss_err[:400000]

time_ss_sopc=np.linspace(0,2000,len(sopc_ssr1))
time_ss_popc=np.linspace(0,2000,len(popc_ssr1))

time_sopc=np.linspace(0,2000,len(sopc[['TM1-TM6']][:200000]))
time_popc=np.linspace(0,2000,len(popc[['TM1-TM6']][:200000]))

#plt.figure(figsize=(15,10))
popc_st5= pd.read_csv('data_Supp_figure_4/popc_st5', delim_whitespace=True)
popc_st5.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
popc_st5=popc_st5[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

npxxy_st5= pd.read_csv('data_Supp_figure_4/npxxy_st5', delim_whitespace=True)
npxxy_st5.columns=['time','TYR', 'OH', 'n', 'n']


popc_st10= pd.read_csv('data_Supp_figure_4/popc_st10', delim_whitespace=True)
popc_st10.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
popc_st10=popc_st10[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]

npxxy_st10= pd.read_csv('data_Supp_figure_4/npxxy_st10', delim_whitespace=True)
npxxy_st10.columns=['time','TYR', 'OH', 'n', 'n']



st5_icl2= pd.read_csv('data_Supp_figure_4/popc_st5_ICL2.xvg', delim_whitespace=True, comment='#')
st5_icl2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']

st10_icl2= pd.read_csv('data_Supp_figure_4/popc_st10_ICL2.xvg', delim_whitespace=True, comment='#')
st10_icl2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']

st10_icl2=st10_icl2[['A_Helix','Th_Helix' ]].sum(axis=1)/11
time_st10icl2=np.linspace(0,2000,len(st10_icl2))



window=500

time_st5=np.linspace(0,2000,len(popc_st5))
time_st10=np.linspace(0,2000,len(popc_st10))
ax=plt.subplot(2,4,1)
ax.plot(time_st10,popc_st10[['TM1-TM6']].rolling(500).mean()*10, color='grey', label='POPC_ST10' )
ax.plot(time_st5,popc_st5[['TM1-TM6']].rolling(500).mean()*10, color='tab:red', label='POPC_ST5' )
ax.plot(time_popc,popc_r1[['TM1-TM6']][:200000].rolling(window).mean()*10, color='tab:green',label='POPC + 0mN/m')
ax.plot(time_sopc,sopc_r1[['TM1-TM6']][:200000].rolling(window).mean()*10, color='tab:blue',label='SOPC + 0mN/m')
ax.axhline(y=32.85, linestyle='dashed', color='tab:orange', lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
ax.set_ylabel( 'TM1-TM6 Dist. ($\AA$)', fontsize=12)
ax.set_xlim(0,2000)
#plt.legend()
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

ax1=plt.subplot(2,4,2)
plt.plot(time_st10,popc_st10[['TM1-ICL2']].rolling(500).mean()*10, color='grey', label='POPC_ST10' )
plt.plot(time_st5,popc_st5[['TM1-ICL2']].rolling(500).mean()*10, color='tab:red', label='POPC_ST5' )
plt.plot(time_popc,(popc_r1[['TM1-ICL2']][:200000].rolling(window).mean()*10),color='tab:green',label='POPC + 0mN/m')
plt.plot(time_sopc,(sopc_r1[['TM1-ICL2']][:200000].rolling(window).mean()*10),color='tab:blue',label='SOPC + 0mN/m')
plt.axhline(y=25.79, linestyle='dashed', color='tab:orange', lw=1.5)
plt.axhline(y=19.50, linestyle='dashed', color='0.5',lw=1.5)
plt.ylabel( 'TM1-ICL2 Dist. ($\AA$)', fontsize=12)
plt.xlim(0,2000)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

ax2=plt.subplot(2,4,3)
plt.plot(time_st10,popc_st10[['TM5-ICL2']].rolling(500).mean()*10, color='grey', label='POPC_ST10' )
plt.plot(time_st5,popc_st5[['TM5-ICL2']].rolling(500).mean()*10, color='tab:red', label='POPC_ST5' )
plt.plot(time_popc,(popc_r1[['TM5-ICL2']][:200000].rolling(window).mean()*10),color='tab:green',label='POPC + 0mN/m')
plt.plot(time_sopc,(sopc_r1[['TM5-ICL2']][:200000].rolling(window).mean()*10),color='tab:blue',label='SOPC + 0mN/m')
plt.axhline(y=23.42, linestyle='dashed', color='tab:orange', lw=1.5)
plt.axhline(y=29.77, linestyle='dashed', color='0.5',lw=1.5)
plt.ylabel( 'TM5-ICL2 Dist. ($\AA$)', fontsize=12)
plt.xlim(0,2000)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

ax3=plt.subplot(2,4,4)
plt.plot(time_st10,popc_st10[['TM6-H8']].rolling(500).mean()*10, color='grey', label='POPC_ST10' )
plt.plot(time_st5,popc_st5[['TM6-H8']].rolling(500).mean()*10, color='tab:red', label='POPC_ST5' )
plt.plot(time_popc,(popc_r1[['TM6-H8']][:200000].rolling(window).mean()*10),color='tab:green',label='POPC + 0mN/m')
plt.plot(time_sopc,(sopc_r1[['TM6-H8']][:200000].rolling(window).mean()*10),color='tab:blue',label='SOPC + 0mN/m')
plt.axhline(y=22.235, linestyle='dashed', color='tab:orange', lw=1.5)
plt.axhline(y=17.30, linestyle='dashed', color='0.5',lw=1.5)
plt.ylabel( 'TM6-H8 Dist. ($\AA$)', fontsize=12)
plt.xlim(0,2000)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

ax4=plt.subplot(2,4,5)
plt.plot(time_st10,popc_st10[['TM3-TM6-ASP241']].rolling(500).mean()*10, color='grey', label='POPC_ST10' )
plt.plot(time_st5,popc_st5[['TM3-TM6-ASP241']].rolling(500).mean()*10, color='tab:red', label='POPC_ST5' )
plt.plot(time_popc,(popc_r1[['TM3-TM6-ASP241']][:200000].rolling(window).mean()*10),color='tab:green',label='POPC + 0mN/m')
plt.plot(time_sopc,(sopc_r1[['TM3-TM6-ASP241']][:200000].rolling(window).mean()*10),color='tab:blue',label='SOPC + 0mN/m')
plt.axhline(y=17.67, linestyle='dashed', color='tab:orange', lw=1.5)
plt.axhline(y=9.12, linestyle='dashed', color='0.5',lw=1.5)
plt.ylabel( 'TM3-TM6 Dist. ($\AA$)', fontsize=12)
plt.xlim(0,2000)
#plt.legend(bbox_to_anchor=(1.5,1))
plt.xlabel('Time (ns)', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)


popc_r1=pd.read_csv('data_Supp_figure_4/popc_npxxy_r1', delim_whitespace=True)
popc_r1.columns=['time','TYR', 'OH', 'n', 'n']
popc_r1=popc_r1[['time','TYR', 'OH']]
popc_r1=popc_r1[:197500]
#time_popc_npxxy=np.linspace(0,2000,len(popc_r1))


popc_r2=pd.read_csv('data_Supp_figure_4/popc_npxxy_r2', delim_whitespace=True)
popc_r2.columns=['time','TYR', 'OH', 'n', 'n']
popc_r2=popc_r2[['time','TYR', 'OH']]
popc_r2=popc_r2[:197500]

#time_popc=np.linspace(0,2000,len(popc_r2))

popc_npxxy=pd.concat([popc_r1[['OH']], popc_r2[['OH']]], axis=1).mean(axis=1)*10
popc_npxxy_err=pd.concat([popc_r1[['OH']], popc_r2[['OH']]], axis=1).std(axis=1)*10
time_popc_npxxy=np.linspace(0,2000,len(popc_npxxy))

sopc_r1=pd.read_csv('data_Supp_figure_4/sopc_npxxy_r1', delim_whitespace=True)
sopc_r1.columns=['time','TYR', 'OH', 'n', 'n']
sopc_r1=sopc_r1[['time','TYR', 'OH']]
sopc_r1=sopc_r1[:200000]
#time_sopc=np.linspace(0,2000,len(sopc_r1))

sopc_r2=pd.read_csv('data_Supp_figure_4/sopc_npxxy_r2', delim_whitespace=True)
sopc_r2.columns=['time','TYR', 'OH', 'n', 'n']
sopc_r2=sopc_r2[['time','TYR', 'OH']]
#time_sopc=np.linspace(0,2000,len(sopc_r1))
sopc_npxxy=pd.concat([sopc_r1[['OH']], sopc_r2[['OH']]], axis=1).mean(axis=1)*10
sopc_npxxy_err=pd.concat([sopc_r1[['OH']], sopc_r2[['OH']]], axis=1).std(axis=1)*10
time_sopc_npxxy=np.linspace(0,2000,len(sopc_r1))

ax5=plt.subplot(2,4,6)
plt.plot(time_st10,npxxy_st10[['OH']].rolling(500).mean()*10, color='grey', label='POPC_ST10' )
plt.plot(time_st5,npxxy_st5[['OH']].rolling(500).mean()*10, color='tab:red', label='POPC_ST5' )
plt.plot(time_popc_npxxy, popc_r1[['OH']].rolling(window).mean()*10, color='tab:green', label='POPC + 0mN/m')
plt.plot(time_sopc_npxxy, sopc_r1[['OH']].rolling(window).mean()*10, color='tab:blue', label='SOPC + 0mN/m')
plt.axhline(y=4.3, linestyle='dashed', color='tab:orange', lw=1.5)
plt.axhline(y=11.2, linestyle='dashed', color='0.5',lw=1.5)
plt.ylabel( 'TYR215OH-TYR302OH Dist. ($\AA$)', fontsize=12)
plt.xlim(0,2000)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Time (ns)', fontsize=12)

ax6=plt.subplot(2,4,7)
plt.plot(time_ss_sopc, sopc_ssr1.rolling(window).mean(), color='tab:blue', label='SOPC')
plt.plot(time_ss_popc, popc_ssr1.rolling(window).mean(), color='tab:green', label='POPC')
plt.plot(st5_icl2[['time']]*0.001,st5_icl2[['A_Helix']].rolling(500).mean()/11.0,color='grey', label='POPC + 5 mN/m' )
plt.plot(time_st10icl2,st10_icl2.rolling(500).mean(),color='tab:red', label='POPC + 10 mN/m')

plt.xlim(0,2000)
plt.ylabel(r'ICL2 $\alpha$-helicity, $f_{\alpha}$', fontsize=12)
plt.ylim(-0.1,0.7)
plt.legend(bbox_to_anchor=(1.3,0.9), fontsize=12)
plt.xlabel('Time (ns)', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.axhline(y=0.66, linestyle='--', lw=1.5, color='tab:orange', label='6OS0, Active')
plt.axhline(y=0.0, linestyle='--', lw=1.5, color='0.5', label='4YAY, Inactive')

leg=plt.legend(ncol=1,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(1.8,1), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

ax.text(-0.10, 1.05, 'a', transform=ax.transAxes, ha='center', fontsize=14, fontweight='bold')
ax1.text(-0.10, 1.05, 'b', transform=ax1.transAxes, ha='center', fontsize=14, fontweight='bold')
ax2.text(-0.10, 1.05, 'c', transform=ax2.transAxes, ha='center', fontsize=14, fontweight='bold')
ax3.text(-0.10, 1.05, 'd', transform=ax3.transAxes, ha='center', fontsize=14, fontweight='bold')
ax4.text(-0.10, 1.05, 'e', transform=ax4.transAxes, ha='center', fontsize=14, fontweight='bold')
ax5.text(-0.10, 1.05, 'f', transform=ax5.transAxes, ha='center', fontsize=14, fontweight='bold')
ax6.text(-0.10, 1.05, 'g', transform=ax6.transAxes, ha='center', fontsize=14, fontweight='bold')


for i in leg.legendHandles:
    i.set_linewidth(2)
fig = plt.gcf()
plt.subplots_adjust(top=0.9, bottom=0.15, left=0.09, right=0.98, hspace=0.35, wspace=0.4)
plt.Figure.set_size_inches(fig,(12, 6))

plt.savefig('Supp_figure_4.png', dpi=300)
