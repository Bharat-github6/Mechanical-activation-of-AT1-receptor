

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



sopc_r1=pd.read_csv('../NPxxY/data/sopc_r1', delim_whitespace=True)
sopc_r1.columns=['time','TYR', 'OH', 'n', 'n']
sopc_r1=sopc_r1[['time','TYR', 'OH']]
sopc_r1=sopc_r1[:200000]
time_sopc=np.linspace(0,2000,len(sopc_r1))

sopc_r2=pd.read_csv('../NPxxY/data/sopc_r2', delim_whitespace=True)
sopc_r2.columns=['time','TYR', 'OH', 'n', 'n']
sopc_r2=sopc_r2[['time','TYR', 'OH']]
#time_sopc=np.linspace(0,2000,len(sopc_r1))
sopc=pd.concat([sopc_r1[['OH']], sopc_r2[['OH']]], axis=1)*10
sopc_err=pd.concat([sopc_r1[['OH']], sopc_r2[['OH']]], axis=1).std(axis=1)*10
time_sopc=np.linspace(0,2000,len(sopc))


popc_r1=pd.read_csv('../NPxxY/data/popc_r1', delim_whitespace=True)
popc_r1.columns=['time','TYR', 'OH', 'n', 'n']
popc_r1=popc_r1[['time','TYR', 'OH']]
popc_r1=popc_r1[:197500]
time_popc=np.linspace(0,2000,len(popc_r1))


popc_r2=pd.read_csv('../NPxxY/data/popc_r2', delim_whitespace=True)
popc_r2.columns=['time','TYR', 'OH', 'n', 'n']
popc_r2=popc_r2[['time','TYR', 'OH']]
popc_r2=popc_r2[:197500]

time_popc=np.linspace(0,2000,len(popc_r2))

popc=pd.concat([popc_r1[['OH']], popc_r2[['OH']]], axis=1)*10
popc_err=pd.concat([popc_r1[['OH']], popc_r2[['OH']]], axis=1).std(axis=1)*10
time_popc=np.linspace(0,2000,len(popc))



st10_r1=pd.read_csv('../NPxxY/data/st10_r1', delim_whitespace=True)
st10_r1.columns=['time','TYR', 'OH', 'n', 'n']
st10_r1=st10_r1[['time','TYR', 'OH']]
st10_r1=st10_r1[:197500]
window=10
#time_st10=np.linspace(0,2000,len(st10_r1))

st10_r2=pd.read_csv('../NPxxY/data/st10_r2', delim_whitespace=True)
st10_r2.columns=['time','TYR', 'OH', 'n', 'n']
st10_r2=st10_r2[['time','TYR', 'OH']]
st10_r2=st10_r2[:197500]
window=50
st10=pd.concat([st10_r1[['OH']], st10_r2[['OH']]], axis=1)*10
st10_err=pd.concat([st10_r1[['OH']], st10_r2[['OH']]], axis=1).std(axis=1)*10
time_st10=np.linspace(0,2000,len(st10))


pepc_r1= pd.read_csv('../NPxxY/data/pepc_r1', delim_whitespace=True)
pepc_r1.columns=['time','TYR', 'OH', 'n', 'n']
pepc_r1=pepc_r1[['time','TYR', 'OH']]
pepc_r1=pepc_r1[:200000]

pepc_r2= pd.read_csv('../NPxxY/data/pepc_r2', delim_whitespace=True)
pepc_r2.columns=['time','TYR', 'OH', 'n', 'n']
pepc_r2=pepc_r2[['time','TYR', 'OH']]
pepc_r2=pepc_r2[:200000]


window=50
pepc=pd.concat([pepc_r1[['OH']], pepc_r2[['OH']]], axis=1)*10
pepc_err=pd.concat([pepc_r1[['OH']], pepc_r2[['OH']]], axis=1).std(axis=1)*10
time_pepc=np.linspace(0,2000,len(pepc))



popch8_r1= pd.read_csv('../NPxxY/data/popch8_r1', delim_whitespace=True)
popch8_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
popch8_r1=popch8_r1[['OH']]


popch8_r2= pd.read_csv('../NPxxY/data/popch8_r2', delim_whitespace=True)
popch8_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
popch8_r2=popch8_r2[[ 'OH']]


popch8=pd.concat([popch8_r1, popch8_r2], axis=1)
popch8_err=pd.concat([popch8_r1, popch8_r2], axis=1).std(axis=1)
#popch8=popch8[:200000]
time_popch8=np.linspace(0,2000,len(popch8))

sopch8_r1= pd.read_csv('../NPxxY/data/sopch8_r1', delim_whitespace=True)
sopch8_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
sopch8_r1=sopch8_r1[['OH']]


sopch8_r2= pd.read_csv('../NPxxY/data/sopch8_r2', delim_whitespace=True)
sopch8_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
sopch8_r2=sopch8_r2[['OH']]


sopch8=pd.concat([sopch8_r1, sopch8_r2], axis=1)
sopch8_err=pd.concat([sopch8_r1, sopch8_r2], axis=1).std(axis=1)
#sopch8=sopch8[:200000]
time_sopch8=np.linspace(0,2000,len(sopch8))

pepch8_r1= pd.read_csv('../NPxxY/data/pepch8_r1', delim_whitespace=True)
pepch8_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
pepch8_r1=pepch8_r1[['OH']]


pepch8_r2= pd.read_csv('../NPxxY/data/pepch8_r2', delim_whitespace=True)
pepch8_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
pepch8_r2=pepch8_r2[['OH']]


pepch8=pd.concat([pepch8_r1, pepch8_r2], axis=1)
pepch8_err=pd.concat([pepch8_r1, pepch8_r2], axis=1).std(axis=1)
#pepch8=pepch8[:200000]
time_pepch8=np.linspace(0,2000,len(pepch8))


st10h8_r1= pd.read_csv('../NPxxY/data/st10h8_r1', delim_whitespace=True)
st10h8_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
st10h8_r1=st10h8_r1[['OH']]


st10h8_r2= pd.read_csv('../NPxxY/data/st10h8_r2', delim_whitespace=True)
st10h8_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
st10h8_r2=st10h8_r2[['OH']]


st10h8=pd.concat([st10h8_r1, st10h8_r2], axis=1)
st10h8_err=pd.concat([st10h8_r1, st10h8_r2], axis=1).std(axis=1)
#st10h8=st10h8[:200000]

time_st10h8=np.linspace(0,2000,len(st10h8))


plt.figure(figsize=(8,6))

ax = plt.subplot(2,2,3)
plt.plot(time_popch8,popch8.rolling(window).mean()*10, label='POPC + F309P/F314P' )
#plt.fill_between(time_popch8, (popch8.rolling(window).mean()*10)-(popch8_err.rolling(window).mean()*10), (popch8.rolling(window).mean()*10)+(popch8_err.rolling(window).mean()*10),color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.ylim(0,20)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.yticks([0,5,10,15])
#plt.xticks([0,500,1000,1500,2000])
plt.title('POPC + F309P/F313P', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'c', ha='center', fontsize=20, fontweight='bold')
plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=12)
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))


ax = plt.subplot(2,2,1)
plt.plot(time_sopch8,sopch8.rolling(window).mean()*10, label='SOPC + F309P/F314P' )
#plt.fill_between(time_popch8, (sopch8.rolling(window).mean()*10)-(sopch8_err.rolling(window).mean()*10), (sopch8.rolling(window).mean()*10)+(sopch8_err.rolling(window).mean()*10),color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.ylim(0,20)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.yticks([0,5,10,15])
#plt.xticks([0,500,1000,1500,2000])
plt.title('SOPC + F309P/F313P', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'a', ha='center', fontsize=20, fontweight='bold')
plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=12)
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))


ax=plt.subplot(2,2,4)
plt.plot(time_pepch8,pepch8.rolling(window).mean()*10, label='SOPC:SOPE + F309P/F314P' )
#plt.fill_between(time_pepch8, (pepch8.rolling(window).mean()*10)-(pepch8_err.rolling(window).mean()*10), (pepch8.rolling(window).mean()*10)+(pepch8_err.rolling(window).mean()*10),color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.ylim(0,20)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xticks([0,500,1000,1500,2000])
#plt.yticks([0,5,10,15])
plt.title('SOPC:SOPE + F309P/F313P', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'd', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))


ax = plt.subplot(2,2,2)
plt.plot(time_st10h8,st10h8.rolling(window).mean()*10, label='SOPC +10mN/m + F309P/F314P' )
#plt.fill_between(time_st10h8, (st10h8.rolling(window).mean()*10)-(st10h8_err.rolling(window).mean()*10), (st10h8.rolling(window).mean()*10)+(st10h8_err.rolling(window).mean()*10),color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.ylim(0,20)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xticks([0,500,1000,1500,2000])
#plt.yticks([0,5,10,15])
plt.title('SOPC + 10mN/m  + F309P/F313P', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'b', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))


plt.subplots_adjust(top=0.92, bottom=0.115, left=0.1, right=0.975, hspace=0.35, wspace=0.25)
plt.savefig('Figure_S6.png', dpi=300)
