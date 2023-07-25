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

illustr = plt.imread('SOPC-SOPE.png')


plt.rcParams['agg.path.chunksize'] = 1000000

###Protein_only_Apo state

sopc_r1= pd.read_csv('data_Figure_4/SOPC/replica_1/Deer_analysis_2us', delim_whitespace=True)
sopc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
sopc_r1=sopc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]


sopc_r2= pd.read_csv('data_Figure_4/SOPC/replica_2/Deer_analysis2us', delim_whitespace=True)
sopc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
sopc_r2=sopc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
sopc=pd.concat([sopc_r1, sopc_r2], axis=1)

#sopc=sopc[:200000]

pepc_r1= pd.read_csv('data_Figure_4/PE_PC/replica_1/Deer_analysis_2us', delim_whitespace=True)
pepc_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
pepc_r1=pepc_r1[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]


pepc_r2= pd.read_csv('data_Figure_4/PE_PC/replica_2/Deer_analysis_2us', delim_whitespace=True)
pepc_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241','n','n']
pepc_r2=pepc_r2[['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM2-TM7','TM3-TM6','TM3-TM6-ASP241']]
pepc=pd.concat([pepc_r1, pepc_r2], axis=1)[:200000]

time_pepc=np.linspace(0,2000,len(pepc))
time_sopc=np.linspace(0,2000,len(sopc_r1[:200000]))



###seconadry Structure

pepc_r1_1us= pd.read_csv('data_Figure_4/PE_PC/replica_1/ICL2_1us.xvg', delim_whitespace=True, comment='#')
pepc_r1_1us.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']

pepc_r1_2us= pd.read_csv('data_Figure_4/PE_PC/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
pepc_r1_2us.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix', 'Th_Helix']

ss_pepc_r1_1us=pepc_r1_1us[['A_Helix','Th_Helix' ]].sum(axis=1)/11
ss_pepc_r1_2us=pepc_r1_2us[['A_Helix','Th_Helix','Fiv_Helix' ]].sum(axis=1)/11
ss_pepc_r1=pd.concat([ss_pepc_r1_1us,ss_pepc_r1_2us], axis=0)[:400000]


ss_pepc_r2= pd.read_csv('data_Figure_4/PE_PC/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
ss_pepc_r2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix', 'Th_Helix']
ss_pepc_r2=ss_pepc_r2[['A_Helix','Th_Helix','Fiv_Helix' ]].sum(axis=1)/11
#len(pepc_r1), len(pepc_r2)
ss_pepc_r1=ss_pepc_r1.reset_index(drop=True)

ss_pepc_r1
ss_pepc=pd.concat([ss_pepc_r1,ss_pepc_r2], axis=1)
ss_pepc_err=pd.concat([ss_pepc_r1,ss_pepc_r2], axis=1)

sopc_ssr1=pd.read_csv('data_Figure_4/SOPC/replica_1/ICL2_2us.xvg', delim_whitespace=True, comment='#')
sopc_ssr1.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Fiv_Helix','Th_Helix']

sopc_ssr2=pd.read_csv('data_Figure_4/SOPC/replica_2/ICL2_2us.xvg', delim_whitespace=True, comment='#')
sopc_ssr2.columns=['time', 'structure', 'coil', 'Bend', 'Turn', 'A_Helix','Th_Helix']

sopc_ssr1=sopc_ssr1[['A_Helix','Th_Helix', 'Fiv_Helix' ]].sum(axis=1)/11
sopc_ssr2=sopc_ssr2[['A_Helix','Th_Helix']].sum(axis=1)/11
sopc_ss=pd.concat([sopc_ssr1, sopc_ssr2], axis=1).mean(axis=1)
sopc_ss_err=(pd.concat([sopc_ssr1, sopc_ssr2], axis=1)).std(axis=1)
sopc_ss=sopc_ss[:400000]
sopc_ss_err=sopc_ss_err[:400000]




time_ss_pepc=np.linspace(0,2000, len(ss_pepc))
time_ss_sopc=np.linspace(0,2000,len(sopc_ss))

exp=[33.48,25.57,23.65,22.56]

delta_fyay=[16.509851568627454, 3.890564117647055, -15.710935098039215, 5.308243921568627]


time_sopc=np.linspace(0,2000,len(sopc_r1[:200000]))
time_pepc=np.linspace(0,2000,len(pepc))


fyay=[19.70,19.50,29.77,17.30]

#exp=[33.48,25.57,23.65,22.56] 6DO1
exp=[32.656,25.796,23.422,22.235] #6OS0


window = 500
width=75
start=2150
sp = 150
ax=plt.subplot(2,4,2)

ax.plot(time_pepc,(pepc_r1[['TM1-TM6']][:200000].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (SOPC-SOPE)')
ax.plot(time_sopc,(sopc_r1[['TM1-TM6']][:200000].rolling(window).mean()*10),color='tab:blue', label='AT1R/-/- (SOPC)')
ax.axhline(y=32.65, linestyle='dashed', color='tab:orange', lw=1.5)
ax.axhline(y=19.70, linestyle='dashed', color='0.5',lw=1.5)
ax.set_ylim(17,35)
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('TM1-TM6 Dist. ($\AA$)', fontsize=11)
ax.set_xlim(0,2000)
#ax.set_xlabel('Time (ns)', fontsize=11)
ax.set_xlabel('Time (ns)', fontsize=11)
rect = Rectangle((2056,17), 370, 18, clip_on=False, ec='k', fill=False)
ax.add_patch(rect)

box_parts = ax.boxplot((sopc[['TM1-TM6']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue', clip_on=False)

box_parts = ax.boxplot((pepc[['TM1-TM6']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)
for line in plt.gca().get_lines(): line.set_clip_on(False)
ax1=plt.subplot(2,4,3)


ax1.plot(time_pepc,(pepc_r1[['TM1-ICL2']][:200000].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (SOPC-SOPE)')
ax1.plot(time_sopc,(sopc_r1[['TM1-ICL2']][:200000].rolling(window).mean()*10),color='tab:blue', label='AT1R/-/- (SOPC)')
ax1.axhline(y=19.50, linestyle='--', lw=1.5, color='0.5')
ax1.axhline(y=25.57, linestyle='--', lw=1.5, color='tab:orange')
ax1.set_ylim(16,30)
ax1.set_xlim(0,2000)
ax1.set_ylabel('TM1-ICL2 Dist. ($\AA$)', fontsize=11)
ax1.set_xlabel('Time (ns)', fontsize=11)
ax1.yaxis.set_major_locator(MultipleLocator(2))
ax1.yaxis.set_minor_locator(AutoMinorLocator(2))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax1.set_yticks([ 20, 25], minor=True)
#leg=ax1.legend(ncol=3,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(2.2,1.15), markerscale=8 ,columnspacing=1, handletextpad=1, handlelength=1, fontsize=15)

#for i in leg.legendHandles:
#    i.set_linewidth(3)
rect = Rectangle((2056,16), 370, 14, clip_on=False, ec='k', fill=False)
ax1.add_patch(rect)
box_parts = ax1.boxplot((sopc[['TM1-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax1.boxplot((pepc[['TM1-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)
for line in plt.gca().get_lines(): line.set_clip_on(False)



ax2=plt.subplot(2,4,4)
ax2.plot(time_pepc,(pepc_r1[['TM5-ICL2']][:200000].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (SOPC-SOPE)')
ax2.plot(time_sopc,(sopc_r1[['TM5-ICL2']][:200000].rolling(window).mean()*10),color='tab:blue', label='AT1R/-/- (SOPC)')
ax2.set_xlim(0,2000)
ax2.set_xlabel('Time (ns)', fontsize=11)
ax2.axhline(y=23.65, linestyle='--', lw=1.5, color='tab:orange')
ax2.axhline(y=29.77, linestyle='--', lw=1.5, color='0.5')
ax2.set_ylim(20,32)
ax2.set_xlabel('Time (ns)', fontsize=11)
ax2.set_ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=11)
ax2.yaxis.set_major_locator(MultipleLocator(2))
ax2.yaxis.set_minor_locator(AutoMinorLocator(2))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax1.set_yticks([ 20, 25], minor=True)
rect = Rectangle((2056,20), 370, 12, clip_on=False, ec='k', fill=False)
ax2.add_patch(rect)
box_parts = ax2.boxplot((sopc[['TM5-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax2.boxplot((pepc[['TM5-ICL2']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)
for line in plt.gca().get_lines(): line.set_clip_on(False)

ax3=plt.subplot(2,4,6)

ax3.plot(time_pepc,(pepc_r1[['TM6-H8']][:200000].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (SOPC-SOPE)')
ax3.plot(time_sopc,(sopc_r1[['TM6-H8']][:200000].rolling(window).mean()*10),color='tab:blue', label='AT1R/-/- (SOPC)')
ax3.set_ylabel( 'TM6-H8 Dist. ($\AA$)', fontsize=11)
ax3.axhline(y=17.30, linestyle='--', lw=1.5, color='0.5')
ax3.axhline(y=22.56, linestyle='--', lw=1.5, color='tab:orange')
ax3.set_ylim(10,26)
ax3.set_xlim(0,2000)
ax3.set_xlabel('Time (ns)', fontsize=11)
ax3.yaxis.set_major_locator(MultipleLocator(5))
#ax3.set_yticks([10,15,20,25])
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))
rect = Rectangle((2056,10), 370, 16, clip_on=False, ec='k', fill=False)
ax3.add_patch(rect)
box_parts = ax3.boxplot((sopc[['TM6-H8']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax3.boxplot((pepc[['TM6-H8']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)
for line in plt.gca().get_lines(): line.set_clip_on(False)



ax6=plt.subplot(2,4,7)

ax6.plot(time_pepc,(pepc_r1[['TM3-TM6-ASP241']][:200000].rolling(window).mean()*10),color='tab:green',label='AT1R/-/- (SOPC-SOPE)')
ax6.plot(time_sopc,(sopc_r1[['TM3-TM6-ASP241']][:200000].rolling(window).mean()*10),color='tab:blue', label='AT1R/-/- (SOPC)')
ax6.set_ylabel('TM3-TM6 Dist. ($\AA$)', fontsize=11)
ax6.axhline(y=9.12, linestyle='--', lw=1.5, color='0.5')
ax6.axhline(y=17.67, linestyle='--', lw=1.5, color='tab:orange')
ax6.set_ylim(6,23)
ax6.set_xlim(0,2000)
ax6.set_xlabel('Time (ns)', fontsize=11)
ax6.yaxis.set_major_locator(MultipleLocator(5))
#ax3.set_yticks([10,15,20,25])
ax6.yaxis.set_minor_locator(AutoMinorLocator(5))
ax6.xaxis.set_minor_locator(AutoMinorLocator(5))
rect = Rectangle((2056,6), 370, 17, clip_on=False, ec='k', fill=False)
ax6.add_patch(rect)
box_parts = ax6.boxplot((sopc[['TM3-TM6-ASP241']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax6.boxplot((pepc[['TM3-TM6-ASP241']][150000:200000].dropna().to_numpy().flatten()*10,),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green', clip_on=False)
for line in plt.gca().get_lines(): line.set_clip_on(False)

#time_pe_ss=(np.linspace(0,1000,len(ss_pe)))
#time_p_ss=(np.linspace(0,1000,len(ss_p)))

ax7=plt.subplot(2,4,8)

ax7.plot(time_ss_sopc,sopc_ssr1[:400000].rolling(500).mean(), color='tab:blue', label='SOPC', rasterized=True)
ax7.plot(time_ss_pepc,ss_pepc_r1[:400000].rolling(500).mean(), color='tab:green',label='SOPC:SOPE', rasterized=True)
#ax4.set_xticklabels(d,rotation=0,zorder=100)
#ax4.set_xticks(d1)
#print('sopc=',ss_sopc,'popc=',ss_popc,'dmpc=',ss_dmpc)
ax7.set_xlim(0,2000)
ax7.set_xlabel('Time (ns)', fontsize=11)
ax7.set_ylabel(r'ICL2 $\alpha$-helicity, $f_{\alpha}$', fontsize=11)
ax7.axhline(y=0.66, linestyle='--', lw=1.5, color='tab:orange', label='6OS0, Active')
ax7.axhline(y=0.0, linestyle='--', lw=1.5, color='0.5', label='4YAY, Inactive')
ax7.set_ylim(-0.05,0.7)
ax7.yaxis.set_major_locator(MaxNLocator(4))
ax7.yaxis.set_minor_locator(AutoMinorLocator(2))
ax7.xaxis.set_minor_locator(AutoMinorLocator(5))
rect = Rectangle((2056,-0.05), 370, 0.75, clip_on=False, ec='k', fill=False)
ax7.add_patch(rect)

box_parts = ax7.boxplot((sopc_ss[-100000:].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:blue',clip_on=False)

box_parts = ax7.boxplot((ss_pepc[-100000:].dropna().to_numpy().flatten(),),
                        vert=True, positions=(start+sp,), widths=(width,),
                        medianprops=dict(color='k'), boxprops=dict(color='k'), showfliers=False, patch_artist=True, manage_ticks=False)
for patch in box_parts['boxes']:
    patch.set(facecolor='tab:green',clip_on=False)
for line in plt.gca().get_lines(): line.set_clip_on(False)


leg=ax7.legend(ncol=4,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(-1,2.8), markerscale=8 ,columnspacing=1, handletextpad=0.5, handlelength=1.5, fontsize=12)

for i in leg.legendHandles:
    i.set_linewidth(2)


ax.text(-0.24, 1.03, 'a', transform=ax.transAxes, ha='center', fontsize=14, fontweight='bold')
ax1.text(-0.24, 1.03, 'b', transform=ax1.transAxes, ha='center', fontsize=14, fontweight='bold')
ax2.text(-0.24, 1.03, 'c', transform=ax2.transAxes, ha='center', fontsize=14, fontweight='bold')
ax3.text(-0.24, 1.03, 'd', transform=ax3.transAxes, ha='center', fontsize=14, fontweight='bold')
ax6.text(-0.24, 1.03, 'e', transform=ax6.transAxes, ha='center', fontsize=14, fontweight='bold')
ax7.text(-0.24, 1.03, 'f', transform=ax7.transAxes, ha='center', fontsize=14, fontweight='bold')
fig = plt.gcf()

#left_top = plt.subplot(2,4,1)
#left_bottom = plt.subplot(2,4,5)
left_top = plt.axes([-0.03, 0.47, 0.3, 0.52])
left_bottom = plt.axes([-0.19, 0.01, 0.6, 0.98])
left_top.axis('off')
left_bottom.axis('off')
im1 = left_bottom.imshow(illustr, aspect='equal')
#im2 = left_bottom.imshow(bottomview, aspect='equal')

plt.subplots_adjust(top=0.90, bottom=0.115, left=0.02, right=0.95, hspace=0.43, wspace=0.65)
plt.Figure.set_size_inches(fig,(10, 4.2))

plt.savefig('Figure_4.png' ,dpi=300) ## block=False, agg_filter=None)
#plt.savefig('time_evolution.svg', dpi=900, bbox_inches='tight')
plt.close()
