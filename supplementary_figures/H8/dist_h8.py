

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



sopc_r1=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/production_run/descriptor/npxxy', delim_whitespace=True)
sopc_r1.columns=['time','TYR', 'OH', 'n', 'n']
sopc_r1=sopc_r1[['time','TYR', 'OH']]
sopc_r1=sopc_r1[:200000]
time_sopc=np.linspace(0,2000,len(sopc_r1))

sopc_r2=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/replica_2/descriptor/npxxy', delim_whitespace=True)
sopc_r2.columns=['time','TYR', 'OH', 'n', 'n']
sopc_r2=sopc_r2[['time','TYR', 'OH']]
#time_sopc=np.linspace(0,2000,len(sopc_r1))
sopc=pd.concat([sopc_r1[['OH']], sopc_r2[['OH']]], axis=1).mean(axis=1)*10
sopc_err=pd.concat([sopc_r1[['OH']], sopc_r2[['OH']]], axis=1).std(axis=1)*10
time_sopc=np.linspace(0,2000,len(sopc))


popc_r1=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/POPC/with_protein_only/ASPH74-125/descriptor/npxxy', delim_whitespace=True)
popc_r1.columns=['time','TYR', 'OH', 'n', 'n']
popc_r1=popc_r1[['time','TYR', 'OH']]
popc_r1=popc_r1[:197500]
time_popc=np.linspace(0,2000,len(popc_r1))


popc_r2=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/POPC/with_protein_only/replica_2/descriptor/npxxy1', delim_whitespace=True)
popc_r2.columns=['time','TYR', 'OH', 'n', 'n']
popc_r2=popc_r2[['time','TYR', 'OH']]
popc_r2=popc_r2[:197500]

time_popc=np.linspace(0,2000,len(popc_r2))

popc=pd.concat([popc_r1[['OH']], popc_r2[['OH']]], axis=1).mean(axis=1)*10
popc_err=pd.concat([popc_r1[['OH']], popc_r2[['OH']]], axis=1).std(axis=1)*10
time_popc=np.linspace(0,2000,len(popc))

dmpc_r1=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/DMPC/with_protein_only/replica_1/descriptor/npxxy', delim_whitespace=True)
dmpc_r1.columns=['time','TYR', 'OH', 'n', 'n']
dmpc_r1=dmpc_r1[['time','TYR', 'OH']]
dmpc_r1=dmpc_r1[:197500]



dmpc_r2=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/DMPC/with_protein_only/replica_2/descriptor/npxxy1', delim_whitespace=True)
dmpc_r2.columns=['time','TYR', 'OH', 'n', 'n']
dmpc_r2=dmpc_r2[['time','TYR', 'OH']]
dmpc_r2=dmpc_r2[:197500]

#time_dmpc=np.linspace(0,2000,len(dmpc))
dmpc=pd.concat([dmpc_r1[['OH']], dmpc_r2[['OH']]], axis=1).mean(axis=1)*10
dmpc_err=pd.concat([dmpc_r1[['OH']], dmpc_r2[['OH']]], axis=1).std(axis=1)*10
time_dmpc=np.linspace(0,2000,len(dmpc))


st5_r2=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/surface_tension/starting_from_active_structure/st_after_posres/st_5_r2/descriptor/npxxy', delim_whitespace=True)
st5_r2.columns=['time','TYR', 'OH', 'n', 'n']
st5_r2=st5_r2[['time','TYR', 'OH']]
st5_r2=st5_r2[:197500]
window=1

st5_r1=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/surface_tension/starting_from_active_structure/st_after_posres/st_5/descriptor/npxxy', delim_whitespace=True)
st5_r1.columns=['time','TYR', 'OH', 'n', 'n']
st5_r1=st5_r1[['time','TYR', 'OH']]
st5_r1=st5_r1[:197500]


st5=pd.concat([st5_r1[['OH']], st5_r2[['OH']]], axis=1).mean(axis=1)*10
st5_err=pd.concat([st5_r1[['OH']], st5_r2[['OH']]], axis=1).std(axis=1)*10
#time_st10=np.linspace(0,2000,len(st10))
time_st5=np.linspace(0,2000,len(st5))


st10_r1=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/surface_tension/starting_from_active_structure/st_after_posres/st_10/descriptor/npxxy', delim_whitespace=True)
st10_r1.columns=['time','TYR', 'OH', 'n', 'n']
st10_r1=st10_r1[['time','TYR', 'OH']]
st10_r1=st10_r1[:197500]
window=10
#time_st10=np.linspace(0,2000,len(st10_r1))

st10_r2=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/surface_tension/starting_from_active_structure/st_after_posres/st_10_r2/descriptor/npxxy', delim_whitespace=True)
st10_r2.columns=['time','TYR', 'OH', 'n', 'n']
st10_r2=st10_r2[['time','TYR', 'OH']]
st10_r2=st10_r2[:197500]
window=50
st10=pd.concat([st10_r1[['OH']], st10_r2[['OH']]], axis=1).mean(axis=1)*10
st10_err=pd.concat([st10_r1[['OH']], st10_r2[['OH']]], axis=1).std(axis=1)*10
time_st10=np.linspace(0,2000,len(st10))


st15_r1=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/surface_tension/starting_from_active_structure/st_after_posres/st_15/descriptor/npxxy', delim_whitespace=True)
st15_r1.columns=['time','TYR', 'OH', 'n', 'n']
st15_r1=st15_r1[['time','TYR', 'OH']]
st15_r1=st15_r1[:200000]
window=10
#time_st10=np.linspace(0,2000,len(st10_r1))

st15_r2=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/surface_tension/starting_from_active_structure/st_after_posres/st_15_r2/descriptor/npxxy', delim_whitespace=True)
st15_r2.columns=['time','TYR', 'OH', 'n', 'n']
st15_r2=st15_r2[['time','TYR', 'OH']]
st15_r2=st15_r2[:200000]
window=50
st15=pd.concat([st15_r1[['OH']], st15_r2[['OH']]], axis=1).mean(axis=1)*10
st15_err=pd.concat([st15_r1[['OH']], st15_r2[['OH']]], axis=1).std(axis=1)*10
time_st15=np.linspace(0,2000,len(st15))

st20_r1=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/surface_tension/starting_from_active_structure/st_after_posres/st_20/descriptor/npxxy', delim_whitespace=True)
st20_r1.columns=['time','TYR', 'OH', 'n', 'n']
st20_r1=st20_r1[['time','TYR', 'OH']]
#st20_r1=st20_r1[['rmsd']]
st20_r1=st20_r1[:190000]
st20_r1=st20_r1.reset_index(drop=True)
#print(len(st20_r1))

st20_r2=pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/surface_tension/starting_from_active_structure/st_after_posres/st_20_r2/descriptor/npxxy1', delim_whitespace=True)
st20_r2.columns=['time','TYR', 'OH', 'n', 'n']
st20_r2=st20_r2[['time','TYR', 'OH']]
#st20_r2=st20_r2[['rmsd']]
st20_r2=st20_r2[:190000]
#st20_r2=st20_r2#[:400000]
#print(len(st20_r2))
window=50
st20=pd.concat([st20_r1[['OH']], st20_r2[['OH']]], axis=1).mean(axis=1)*10
st20_err=pd.concat([st20_r1[['OH']], st20_r2[['OH']]], axis=1).std(axis=1)*10
time_st20=np.linspace(0,2000,len(st20))


ang_r1= pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_agonist_6os0/production_run/descriptor/npxxy1', delim_whitespace=True)
ang_r1.columns=['time','TYR', 'OH', 'n', 'n']
ang_r1=ang_r1[['time','TYR', 'OH']]
ang_r1=ang_r1[:200000]


ang_r2= pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_agonist_6os0/replica_2/descriptor/npxxy1', delim_whitespace=True)
ang_r2.columns=['time','TYR', 'OH', 'n', 'n']
ang_r2=ang_r2[['time','TYR', 'OH']]
ang_r2=ang_r2[:200000]


window=50
ang=pd.concat([ang_r1[['OH']], ang_r2[['OH']]], axis=1).mean(axis=1)*10
ang_err=pd.concat([ang_r1[['OH']], ang_r2[['OH']]], axis=1).std(axis=1)*10
time_ang=np.linspace(0,2000,len(ang))


an_r1= pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_agonist_nanobody/ASPH74-125/production_run/descriptor/npxxy', delim_whitespace=True)
an_r1.columns=['time','TYR', 'OH', 'n', 'n']
an_r1=an_r1[['time','TYR', 'OH']]
an_r1=an_r1[:197500]


an_r2= pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_agonist_nanobody/ASPH74-125/replica_2/descriptor/npxxy', delim_whitespace=True)
an_r2.columns=['time','TYR', 'OH', 'n', 'n']
an_r2=an_r2[['time','TYR', 'OH']]
an_r2=an_r2[:197500]


window=50
an=pd.concat([an_r1[['OH']], an_r2[['OH']]], axis=1).mean(axis=1)*10
an_err=pd.concat([an_r1[['OH']], an_r2[['OH']]], axis=1).std(axis=1)*10
time_an=np.linspace(0,2000,len(an))


pepc_r1= pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/SOPC_SOPE/replica_1/descriptor/npxxy1', delim_whitespace=True)
pepc_r1.columns=['time','TYR', 'OH', 'n', 'n']
pepc_r1=pepc_r1[['time','TYR', 'OH']]
pepc_r1=pepc_r1[:200000]

pepc_r2= pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_protein_only/ASPH74-125/SOPC_SOPE/replica_2/descriptor/npxxy', delim_whitespace=True)
pepc_r2.columns=['time','TYR', 'OH', 'n', 'n']
pepc_r2=pepc_r2[['time','TYR', 'OH']]
pepc_r2=pepc_r2[:200000]


window=50
pepc=pd.concat([pepc_r1[['OH']], pepc_r2[['OH']]], axis=1).mean(axis=1)*10
pepc_err=pd.concat([pepc_r1[['OH']], pepc_r2[['OH']]], axis=1).std(axis=1)*10
time_pepc=np.linspace(0,2000,len(pepc))


n_r1= pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_nanobody_only/ASPH74-125/production_run/descriptor/npxxy', delim_whitespace=True)
n_r1.columns=['time','TYR', 'OH', 'n', 'n']
n_r1=n_r1[['time','TYR', 'OH']]
n_r1=n_r1[:197500]


n_r2= pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_nanobody_only/ASPH74-125/replica_2/descriptor/npxxy1', delim_whitespace=True)
n_r2.columns=['time','TYR', 'OH', 'n', 'n']
n_r2=n_r2[['time','TYR', 'OH']]
n_r2=n_r2[:197500]


window=1
n=pd.concat([n_r1[['OH']], n_r2[['OH']]], axis=1).mean(axis=1)*10
n_err=pd.concat([n_r1[['OH']], n_r2[['OH']]], axis=1).std(axis=1)*10
time_n=np.linspace(0,2000,len(n))



s1i8_r1= pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_agonist_only/ASPH74-125/production_run/descriptor/npxxy1', delim_whitespace=True)
s1i8_r1.columns=['time','TYR', 'OH', 'n', 'n']
s1i8_r1=s1i8_r1[['time','TYR', 'OH']]
s1i8_r1=s1i8_r1[:197500]


s1i8_r2= pd.read_csv('/home/bpoudel/projects/gpcr/6do1-active-state/SOPC/with_agonist_only/ASPH74-125/replica_2/descriptor/npxxy1', delim_whitespace=True)
s1i8_r2.columns=['time','TYR', 'OH', 'n', 'n']
s1i8_r2=s1i8_r2[['time','TYR', 'OH']]
s1i8_r2=s1i8_r2[:197500]


window=50
s1i8=pd.concat([s1i8_r1[['OH']], s1i8_r2[['OH']]], axis=1).mean(axis=1)*10
s1i8_err=pd.concat([s1i8_r1[['OH']], s1i8_r2[['OH']]], axis=1).std(axis=1)*10
time_s1i8=np.linspace(0,2000,len(s1i8))



popch8_r1= pd.read_csv('/home/projects/gpcr/6do1-active-state/H8/correct_one/replica_1/POPC/descriptor/Deer_analysis_2us', delim_whitespace=True)
popch8_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
popch8_r1=popch8_r1[['OH']]


popch8_r2= pd.read_csv('/home/projects/gpcr/6do1-active-state/H8/correct_one/replica_2/POPC/descriptor/Deer_analysis_2us', delim_whitespace=True)
popch8_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
popch8_r2=popch8_r2[[ 'OH']]


popch8=pd.concat([popch8_r1, popch8_r2], axis=1).mean(axis=1)
popch8_err=pd.concat([popch8_r1, popch8_r2], axis=1).std(axis=1)
#popch8=popch8[:200000]
time_popch8=np.linspace(0,2000,len(popch8))

sopch8_r1= pd.read_csv('/home/projects/gpcr/6do1-active-state/H8/correct_one/replica_1/SOPC/descriptor/Deer_analysis_2us', delim_whitespace=True)
sopch8_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
sopch8_r1=sopch8_r1[['OH']]


sopch8_r2= pd.read_csv('/home/projects/gpcr/6do1-active-state/H8/correct_one/replica_2/SOPC/descriptor/Deer_analysis_2us', delim_whitespace=True)
sopch8_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
sopch8_r2=sopch8_r2[['OH']]


sopch8=pd.concat([sopch8_r1, sopch8_r2], axis=1).mean(axis=1)
sopch8_err=pd.concat([sopch8_r1, sopch8_r2], axis=1).std(axis=1)
#sopch8=sopch8[:200000]
time_sopch8=np.linspace(0,2000,len(sopch8))

pepch8_r1= pd.read_csv('/home/projects/gpcr/6do1-active-state/H8/correct_one/replica_1/SOPC_SOPE/descriptor/Deer_analysis_2us', delim_whitespace=True)
pepch8_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
pepch8_r1=pepch8_r1[['OH']]


pepch8_r2= pd.read_csv('/home/projects/gpcr/6do1-active-state/H8/correct_one/replica_2/SOPC_SOPE/descriptor/Deer_analysis_2us', delim_whitespace=True)
pepch8_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
pepch8_r2=pepch8_r2[['OH']]


pepch8=pd.concat([pepch8_r1, pepch8_r2], axis=1).mean(axis=1)
pepch8_err=pd.concat([pepch8_r1, pepch8_r2], axis=1).std(axis=1)
#pepch8=pepch8[:200000]
time_pepch8=np.linspace(0,2000,len(pepch8))


st10h8_r1= pd.read_csv('/home/projects/gpcr/6do1-active-state/H8/correct_one/replica_1/ST_10/descriptor/Deer_analysis_2us', delim_whitespace=True)
st10h8_r1.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
st10h8_r1=st10h8_r1[['OH']]


st10h8_r2= pd.read_csv('/home/projects/gpcr/6do1-active-state/H8/correct_one/replica_2/ST_10/descriptor/Deer_analysis_2us', delim_whitespace=True)
st10h8_r2.columns=['time', 'TM1-TM6', 'TM1-ICL2', 'TM5-ICL2','TM6-H8','TM3-TM6-ASP241','OH','n','n']
st10h8_r2=st10h8_r2[['OH']]


st10h8=pd.concat([st10h8_r1, st10h8_r2], axis=1).mean(axis=1)
st10h8_err=pd.concat([st10h8_r1, st10h8_r2], axis=1).std(axis=1)
#st10h8=st10h8[:200000]

time_st10h8=np.linspace(0,2000,len(st10h8))







plt.figure(figsize=(8,6))

plt.subplot(2,2,3)
plt.plot(time_popch8,popch8.rolling(window).mean()*10,color='tab:blue', label='POPC + F309P/F314P' )
plt.fill_between(time_popch8, (popch8.rolling(window).mean()*10)-(popch8_err.rolling(window).mean()*10), (popch8.rolling(window).mean()*10)+(popch8_err.rolling(window).mean()*10),color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.ylim(0,15)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.yticks([0,5,10,15])
plt.xticks([0,500,1000,1500,2000])
plt.title('POPC + F309P/F313P', y=1, pad=-16, fontsize=12)
plt.text(-150, 16, 'c', ha='center', fontsize=20, fontweight='bold')
plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=12)

plt.subplot(2,2,1)
plt.plot(time_sopch8,sopch8.rolling(window).mean()*10,color='tab:blue', label='SOPC + F309P/F314P' )
plt.fill_between(time_popch8, (sopch8.rolling(window).mean()*10)-(sopch8_err.rolling(window).mean()*10), (sopch8.rolling(window).mean()*10)+(sopch8_err.rolling(window).mean()*10),color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.ylim(0,15)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.yticks([0,5,10,15])
plt.xticks([0,500,1000,1500,2000])
plt.title('SOPC + F309P/F313P', y=1, pad=-16, fontsize=12)
plt.text(-150, 16, 'a', ha='center', fontsize=20, fontweight='bold')
plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=12)


plt.subplot(2,2,4)
plt.plot(time_pepch8,pepch8.rolling(window).mean()*10,color='tab:blue', label='SOPC:SOPE + F309P/F314P' )
plt.fill_between(time_pepch8, (pepch8.rolling(window).mean()*10)-(pepch8_err.rolling(window).mean()*10), (pepch8.rolling(window).mean()*10)+(pepch8_err.rolling(window).mean()*10),color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.ylim(0,15)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xticks([0,500,1000,1500,2000])
plt.yticks([0,5,10,15])
plt.title('SOPC:SOPE + F309P/F313P', y=1, pad=-16, fontsize=12)
plt.text(-150, 16, 'd', ha='center', fontsize=20, fontweight='bold')

plt.subplot(2,2,2)
plt.plot(time_st10h8,st10h8.rolling(window).mean()*10,color='tab:blue', label='SOPC +10mN/m + F309P/F314P' )
plt.fill_between(time_st10h8, (st10h8.rolling(window).mean()*10)-(st10h8_err.rolling(window).mean()*10), (st10h8.rolling(window).mean()*10)+(st10h8_err.rolling(window).mean()*10),color='tab:blue', alpha=0.1)
plt.xlim(0,2000)
plt.ylim(0,15)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xticks([0,500,1000,1500,2000])
plt.yticks([0,5,10,15])
plt.title('SOPC +10mN/m  + F309P/F313P', y=1, pad=-16, fontsize=12)
plt.text(-150, 16, 'b', ha='center', fontsize=20, fontweight='bold')

plt.subplots_adjust(top=0.92, bottom=0.115, left=0.1, right=0.975, hspace=0.35, wspace=0.25)
plt.savefig('npxxy_h8.png', dpi=300)
