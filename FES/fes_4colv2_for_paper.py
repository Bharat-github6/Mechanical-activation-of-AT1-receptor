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

matplotlib.rc('xtick', labelsize=9)
matplotlib.rc('ytick', labelsize=9)
#use('Agg')
font = {'family' : 'sans serif', 'size' : '9'}
rc('font', **font)
mathfont = {'fontset' : 'stix' ,'default' : 'it', 'it' : 'serif:italic'}
rc('mathtext', **mathfont)
rc('lines', linewidth=0.9)
#rc('text', usetex=True)
simplify = {'simplify_threshold' : '0.5'}
rc('path', **simplify)









#agonist_only S1I8

a_a = loadtxt('data/s1i8/fes_TM1TM6_TM6H8_reweight.dat')
a_d=  loadtxt('data/s1i8/fes_TM1ICL2_TM5ICL2_reweight.dat')



#APo with ST 10
p_a10 = loadtxt('data/ST_10/fes_TM1TM6_TM6H8_reweight.dat')
p_d10 = loadtxt('data/ST_10/fes_TM1ICL2_TM5ICL2_reweight.dat')
#APO
p_a1 = loadtxt('data/with_protein_only/fes_TM1TM6_TM6H8_reweight.dat')
p_d1 = loadtxt('data/with_protein_only/fes_TM1ICL2_TM5ICL2_reweight.dat')

##ANGii
ang_a = loadtxt('data/angii/fes_TM1TM6_TM6H8_reweight.dat')
ang_d = loadtxt('data/angii/fes_TM1ICL2_TM5ICL2_reweight.dat')

#popc

popc_a = loadtxt('data/popc/fes_TM1TM6_TM6H8_reweight.dat')
popc_d = loadtxt('data/popc/fes_TM1ICL2_TM5ICL2_reweight.dat')

pepc_a=loadtxt('data/SOPC_SOPE/fes_TM1TM6_TM6H8_reweight.dat')
pepc_d=loadtxt('data/SOPC_SOPE/fes_TM1ICL2_TM5ICL2_reweight.dat')


nx = 251
ny = 251
vmin = 0
vmax = 7
a_xlim=[14,40]
a_ylim=[10,40]

d_xlim=[12,40]
d_ylim=[18,40]
#for i,data in enumerate((ang_a,ang_d,a_a,a_d,popc_a,popc_d,p_a10,p_d10,pepc_a,pepc_d,p_a1,p_d1)):
for i,data in enumerate((p_a1,p_d1,p_a10,p_d10,ang_a,ang_d,pepc_a,pepc_d,a_a,a_d,popc_a,popc_d,)):
    x= (data[:,0].reshape((nx,ny)))*10
    y = (data[:,1].reshape((nx,ny)))*10
    z = (data[:,2].reshape((nx,ny)))/4.184
    ax = plt.subplot(3, 4, i+1)
    #ax.axis('equal')
    im = ax.pcolormesh(x,y,z, vmin=vmin, vmax=vmax, cmap='plasma',rasterized=True)
    ax.contour(x,y,z, arange(0,vmax,1), colors='c', linewidths=0.4,rasterized=True)
    #ax.text(-0.25, 0.95, letters[i], ha='left', transform=ax.transAxes, weight='bold', fontsize=8, fontname='sans-serif')
    #ax.text(0.065, 0.8, labels[i], ha='left', transform=ax.transAxes, fontsize=8)
    #ax.set_xlabel(r'$A$ (nm$^2$)', labelpad=1)
   # ax.set_ylabel(r'$r$ (nm)',labelpad=1)
    if i == 0:
        #cax = plt.axes([0.121, 0.961, 0.335, 0.013])
        cax = plt.axes([0.08, 0.95, 0.17, 0.018])
        cb = plt.colorbar(im,extend='max',fraction=1.0,cax=cax,orientation='horizontal',ticklocation='top')
        cb.set_label('$F$ (kcal/mol)',labelpad=-5,fontsize=9)
        cb.set_ticks([0,1,2,3,4,5,6,7])
        cb.set_ticklabels(['0','','','','','','','7'])
        cb.ax.tick_params(length=7, width=0.8,pad=0)
        #cb2.ax.xaxis.set_tick_params(pad=30)

    if i%2 == 0:
        ax.set_xlim(a_xlim)
        ax.set_ylim(a_ylim)
        ax.set_xticks([15,20,25,30,35,40])
        ax.set_yticks([15,20,25,30,35, 40])
        #ax.yaxis.set_major_locator(MaxNLocator(3))
        ax.yaxis.set_minor_locator(AutoMinorLocator(5))
        #ax.xaxis.set_major_locator(MaxNLocator(4))
        ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    else:
        ax.set_xlim(d_xlim)
        ax.set_ylim(d_ylim)
        #ax.set_xticks([])
        ax.set_xticks([15,20,25,30,35,40])
        ax.set_yticks([15,20,25,30,35,40])
        #ax.yaxis.set_major_locator(MaxNLocator(4))
        ax.yaxis.set_minor_locator(AutoMinorLocator(5))
        #ax.xaxis.set_major_locator(MaxNLocator(4))
        ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax = plt.subplot(3,4,5)
plt.ylabel('TM6-H8 Dist. ($\AA$)', fontsize=9)
plt.text(23,30,'SOPC - AngII', fontsize=9, ha='center', va='top')
plt.scatter(32.656,22.235, marker='X',s=50, color='tab:orange', label='Active (AngII), 6OS0')
plt.scatter(19.70,17.30, marker='X',s=50, color='0.5', label='Inactive, 4YAY')
#plt.legend(ncol=2,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(3.0,2.2), markerscale=1 ,columnspacing=1.5, handletextpad=0.4, handlelength=0.8, fontsize=9)
plt.xlabel('TM1-TM6 Dist. ($\AA$)', fontsize=9,labelpad=0)
#ax.xaxis.set_ticklabels([])
#ax.xaxis.set_ticklabels([])
#plt.xticks([])
plt.yticks(fontsize=10)


ax = plt.subplot(3,4,9)
plt.ylabel('TM6-H8 Dist. ($\AA$)', fontsize=9)
plt.text(23,30,'SOPC - S1I8', fontsize=9, ha='center', va='top')
plt.scatter(32.656,22.235, marker='X',s=50, color='tab:orange')
plt.scatter(19.70,17.30, marker='X',s=50, color='0.5')
plt.xlabel('TM1-TM6 Dist. ($\AA$)', fontsize=9,labelpad=0)
#ax.xaxis.set_ticklabels([])
#ax.xaxis.set_ticklabels([])
#plt.xticks([])
plt.yticks(fontsize=10)


ax = plt.subplot(3,4,11)
plt.ylabel('TM6-H8 Dist. ($\AA$)', fontsize=9)
plt.xlabel('TM1-TM6 Dist. ($\AA$)', fontsize=9,labelpad=0)
plt.text(23,30,'POPC', fontsize=9, ha='center', va='top')
plt.scatter(32.656,22.235, marker='X',s=50, color='tab:orange')
plt.scatter(19.70,17.30, marker='X',s=50, color='0.5')
#ax.xaxis.set_ticklabels([])
#ax.xaxis.set_ticklabels([])
#plt.xticks([])
plt.yticks(fontsize=10)


ax = plt.subplot(3,4,3)
plt.ylabel('TM6-H8 Dist. ($\AA$)', fontsize=9)
plt.text(27,16,'SOPC - $\gamma=10$ mN/m', fontsize=9, ha='center', va='top')
plt.scatter(32.656,22.235, marker='X',s=50, color='tab:orange', label='Active (AngII), 6OS0')
plt.scatter(19.70,17.30, marker='X',s=50, color='0.5', label='Inactive, 4YAY')
plt.xlabel('TM1-TM6 Dist. ($\AA$)', fontsize=9,labelpad=0)
plt.legend(ncol=2,frameon=False,borderpad=None, loc='upper center', bbox_to_anchor=(1.0,1.4), markerscale=1 ,columnspacing=1.5, handletextpad=0.4, handlelength=0.8, fontsize=9)
#ax.xaxis.set_ticklabels([])
#ax.xaxis.set_ticklabels([])
#plt.xticks([])
plt.yticks(fontsize=10)

ax = plt.subplot(3,4,7)
plt.ylabel('TM6-H8 Dist. ($\AA$)', fontsize=9)
plt.text(27,13,'SOPC:SOPE', fontsize=9, ha='center', va='top')
plt.scatter(32.656,22.235, marker='X',s=50, color='tab:orange')
plt.scatter(19.70,17.30, marker='X',s=50, color='0.5')
plt.xlabel('TM1-TM6 Dist. ($\AA$)', fontsize=9,labelpad=0)
#ax.xaxis.set_ticklabels([])
#ax.xaxis.set_ticklabels([])
#plt.xticks([])
plt.yticks(fontsize=10)


plt.subplot(3,4,1)
plt.ylabel('TM6-H8 Dist. ($\AA$)', fontsize=9)
plt.text(23,30,'SOPC', fontsize=9, ha='center', va='top')
plt.xlabel('TM1-TM6 Dist. ($\AA$)', fontsize=9,labelpad=0)
plt.scatter(32.656,22.235, marker='X',s=50, color='tab:orange')
plt.scatter(19.70,17.30, marker='X',s=50, color='0.5')
#plt.xticks([])
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)

ax = plt.subplot(3,4,2)
plt.xlabel('TM1-ICL2 Dist. ($\AA$)', fontsize=9,labelpad=0)
plt.ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=9)
plt.scatter(25.796,23.422, marker='X',s=50, color='tab:orange')
plt.scatter(19.50,29.7, marker='X',s=50, color='0.5')
#ax.xaxis.set_ticklabels([])
#ax.xaxis.set_ticklabels([])
#plt.xticks([])
#plt.xlim(10,33)
plt.yticks(fontsize=10)


ax = plt.subplot(3,4,4)
plt.xlabel('TM1-ICL2 Dist. ($\AA$)', fontsize=9,labelpad=0)
plt.ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=9)
plt.scatter(25.796,23.422, marker='X',s=50, color='tab:orange')
plt.scatter(19.50,29.7, marker='X',s=50, color='0.5')
#ax.xaxis.set_ticklabels([])
#ax.xaxis.set_ticklabels([])
#plt.xticks([])
#plt.xlim(10,33)
plt.yticks(fontsize=10)
plt.yticks(fontsize=10)

ax = plt.subplot(3,4,6)
plt.xlabel('TM1-ICL2 Dist. ($\AA$)', fontsize=9,labelpad=0)
plt.ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=9)
plt.scatter(25.796,23.422, marker='X',s=50, color='tab:orange')
plt.scatter(19.50,29.7, marker='X',s=50, color='0.5')
#ax.xaxis.set_ticklabels([])
#ax.xaxis.set_ticklabels([])
#plt.xticks([])
#plt.xlim(10,33)
plt.yticks(fontsize=10)


ax = plt.subplot(3,4,8)
plt.xlabel('TM1-ICL2 Dist. ($\AA$)', fontsize=9,labelpad=0)
plt.ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=9)
plt.scatter(25.796,23.422, marker='X',s=50, color='tab:orange')
plt.scatter(19.50,29.7, marker='X',s=50, color='0.5')
#ax.xaxis.set_ticklabels([])
#ax.xaxis.set_ticklabels([])
#plt.xticks([])
#plt.xlim(10,33)
plt.yticks(fontsize=10)


plt.subplot(3,4,10)
plt.xlabel('TM1-ICL2 Dist. ($\AA$)', fontsize=9,labelpad=0)
plt.ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=9)
plt.scatter(25.796,23.422, marker='X',s=50, color='tab:orange')
plt.scatter(19.50,29.7, marker='X',s=50, color='0.5')
#plt.xlim(10,33)
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)

plt.subplot(3,4,12)
plt.xlabel('TM1-ICL2 Dist. ($\AA$)', fontsize=9,labelpad=0)
plt.ylabel('TM5-ICL2 Dist. ($\AA$)', fontsize=9)
plt.scatter(25.796,23.422, marker='X',s=50, color='tab:orange')
plt.scatter(19.50,29.7, marker='X',s=50, color='0.5')
#plt.xlim(10,33)
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)

fig = plt.gcf()
#plt.subplot
plt.subplots_adjust(top=0.925, bottom=0.1, left=0.07, right=0.975, hspace=0.40, wspace=0.50)
plt.Figure.set_size_inches(fig,(8.0, 5.5))
plt.savefig('final_fes_4colv2.png', dpi=300)
plt.savefig('final_fes_4colv2.svg', dpi=300)
#plt.savefig('time_evolution.svg', dpi=900, bbox_inches='tight')
plt.close()
