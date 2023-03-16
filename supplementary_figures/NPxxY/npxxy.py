

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



sopc_r1=pd.read_csv('data/sopc_r1', delim_whitespace=True)
sopc_r1.columns=['time','TYR', 'OH', 'n', 'n']
sopc_r1=sopc_r1[['time','TYR', 'OH']]
sopc_r1=sopc_r1[:200000]
time_sopc=np.linspace(0,2000,len(sopc_r1))

sopc_r2=pd.read_csv('data/sopc_r2', delim_whitespace=True)
sopc_r2.columns=['time','TYR', 'OH', 'n', 'n']
sopc_r2=sopc_r2[['time','TYR', 'OH']]
#time_sopc=np.linspace(0,2000,len(sopc_r1))
sopc=pd.concat([sopc_r1[['OH']], sopc_r2[['OH']]], axis=1)*10
sopc_err=pd.concat([sopc_r1[['OH']], sopc_r2[['OH']]], axis=1).std(axis=1)*10
time_sopc=np.linspace(0,2000,len(sopc))


popc_r1=pd.read_csv('data/popc_r1', delim_whitespace=True)
popc_r1.columns=['time','TYR', 'OH', 'n', 'n']
popc_r1=popc_r1[['time','TYR', 'OH']]
popc_r1=popc_r1[:197500]
time_popc=np.linspace(0,2000,len(popc_r1))


popc_r2=pd.read_csv('data/popc_r2', delim_whitespace=True)
popc_r2.columns=['time','TYR', 'OH', 'n', 'n']
popc_r2=popc_r2[['time','TYR', 'OH']]
popc_r2=popc_r2[:197500]

time_popc=np.linspace(0,2000,len(popc_r2))

popc=pd.concat([popc_r1[['OH']], popc_r2[['OH']]], axis=1)*10
popc_err=pd.concat([popc_r1[['OH']], popc_r2[['OH']]], axis=1).std(axis=1)*10
time_popc=np.linspace(0,2000,len(popc))

dmpc_r1=pd.read_csv('data/dmpc_r1', delim_whitespace=True)
dmpc_r1.columns=['time','TYR', 'OH', 'n', 'n']
dmpc_r1=dmpc_r1[['time','TYR', 'OH']]
dmpc_r1=dmpc_r1[:197500]



dmpc_r2=pd.read_csv('data/dmpc_r2', delim_whitespace=True)
dmpc_r2.columns=['time','TYR', 'OH', 'n', 'n']
dmpc_r2=dmpc_r2[['time','TYR', 'OH']]
dmpc_r2=dmpc_r2[:197500]

#time_dmpc=np.linspace(0,2000,len(dmpc))
dmpc=pd.concat([dmpc_r1[['OH']], dmpc_r2[['OH']]], axis=1)*10
dmpc_err=pd.concat([dmpc_r1[['OH']], dmpc_r2[['OH']]], axis=1).std(axis=1)*10
time_dmpc=np.linspace(0,2000,len(dmpc))


st5_r2=pd.read_csv('data/st5_r1', delim_whitespace=True)
st5_r2.columns=['time','TYR', 'OH', 'n', 'n']
st5_r2=st5_r2[['time','TYR', 'OH']]
st5_r2=st5_r2[:197500]
window=1

st5_r1=pd.read_csv('data/st5_r2', delim_whitespace=True)
st5_r1.columns=['time','TYR', 'OH', 'n', 'n']
st5_r1=st5_r1[['time','TYR', 'OH']]
st5_r1=st5_r1[:197500]


st5=pd.concat([st5_r1[['OH']], st5_r2[['OH']]], axis=1)*10
st5_err=pd.concat([st5_r1[['OH']], st5_r2[['OH']]], axis=1).std(axis=1)*10
#time_st10=np.linspace(0,2000,len(st10))
time_st5=np.linspace(0,2000,len(st5))


st10_r1=pd.read_csv('data/st10_r1', delim_whitespace=True)
st10_r1.columns=['time','TYR', 'OH', 'n', 'n']
st10_r1=st10_r1[['time','TYR', 'OH']]
st10_r1=st10_r1[:197500]
window=10
#time_st10=np.linspace(0,2000,len(st10_r1))

st10_r2=pd.read_csv('data/st10_r2', delim_whitespace=True)
st10_r2.columns=['time','TYR', 'OH', 'n', 'n']
st10_r2=st10_r2[['time','TYR', 'OH']]
st10_r2=st10_r2[:197500]
window=50
st10=pd.concat([st10_r1[['OH']], st10_r2[['OH']]], axis=1)*10
st10_err=pd.concat([st10_r1[['OH']], st10_r2[['OH']]], axis=1).std(axis=1)*10
time_st10=np.linspace(0,2000,len(st10))


st15_r1=pd.read_csv('data/st15_r1', delim_whitespace=True)
st15_r1.columns=['time','TYR', 'OH', 'n', 'n']
st15_r1=st15_r1[['time','TYR', 'OH']]
st15_r1=st15_r1[:200000]
window=10
#time_st10=np.linspace(0,2000,len(st10_r1))

st15_r2=pd.read_csv('data/st15_r2', delim_whitespace=True)
st15_r2.columns=['time','TYR', 'OH', 'n', 'n']
st15_r2=st15_r2[['time','TYR', 'OH']]
st15_r2=st15_r2[:200000]
window=50
st15=pd.concat([st15_r1[['OH']], st15_r2[['OH']]], axis=1)*10
st15_err=pd.concat([st15_r1[['OH']], st15_r2[['OH']]], axis=1).std(axis=1)*10
time_st15=np.linspace(0,2000,len(st15))

st20_r1=pd.read_csv('data/st20_r1', delim_whitespace=True)
st20_r1.columns=['time','TYR', 'OH', 'n', 'n']
st20_r1=st20_r1[['time','TYR', 'OH']]
#st20_r1=st20_r1[['rmsd']]
st20_r1=st20_r1[:190000]
st20_r1=st20_r1.reset_index(drop=True)
#print(len(st20_r1))

st20_r2=pd.read_csv('data/st20_r2', delim_whitespace=True)
st20_r2.columns=['time','TYR', 'OH', 'n', 'n']
st20_r2=st20_r2[['time','TYR', 'OH']]
#st20_r2=st20_r2[['rmsd']]
st20_r2=st20_r2[:190000]
#st20_r2=st20_r2#[:400000]
#print(len(st20_r2))
window=50
st20=pd.concat([st20_r1[['OH']], st20_r2[['OH']]], axis=1)*10
st20_err=pd.concat([st20_r1[['OH']], st20_r2[['OH']]], axis=1).std(axis=1)*10
time_st20=np.linspace(0,2000,len(st20))


ang_r1= pd.read_csv('data/angii_r1', delim_whitespace=True)
ang_r1.columns=['time','TYR', 'OH', 'n', 'n']
ang_r1=ang_r1[['time','TYR', 'OH']]
ang_r1=ang_r1[:200000]


ang_r2= pd.read_csv('data/angii_r2', delim_whitespace=True)
ang_r2.columns=['time','TYR', 'OH', 'n', 'n']
ang_r2=ang_r2[['time','TYR', 'OH']]
ang_r2=ang_r2[:200000]


window=50
ang=pd.concat([ang_r1[['OH']], ang_r2[['OH']]], axis=1)*10
ang_err=pd.concat([ang_r1[['OH']], ang_r2[['OH']]], axis=1).std(axis=1)*10
time_ang=np.linspace(0,2000,len(ang))


an_r1= pd.read_csv('data/an_r1', delim_whitespace=True)
an_r1.columns=['time','TYR', 'OH', 'n', 'n']
an_r1=an_r1[['time','TYR', 'OH']]
an_r1=an_r1[:197500]


an_r2= pd.read_csv('data/an_r2', delim_whitespace=True)
an_r2.columns=['time','TYR', 'OH', 'n', 'n']
an_r2=an_r2[['time','TYR', 'OH']]
an_r2=an_r2[:197500]


window=50
an=pd.concat([an_r1[['OH']], an_r2[['OH']]], axis=1)*10
an_err=pd.concat([an_r1[['OH']], an_r2[['OH']]], axis=1).std(axis=1)*10
time_an=np.linspace(0,2000,len(an))


pepc_r1= pd.read_csv('data/pepc_r1', delim_whitespace=True)
pepc_r1.columns=['time','TYR', 'OH', 'n', 'n']
pepc_r1=pepc_r1[['time','TYR', 'OH']]
pepc_r1=pepc_r1[:200000]

pepc_r2= pd.read_csv('data/pepc_r2', delim_whitespace=True)
pepc_r2.columns=['time','TYR', 'OH', 'n', 'n']
pepc_r2=pepc_r2[['time','TYR', 'OH']]
pepc_r2=pepc_r2[:200000]


window=50
pepc=pd.concat([pepc_r1[['OH']], pepc_r2[['OH']]], axis=1)*10
pepc_err=pd.concat([pepc_r1[['OH']], pepc_r2[['OH']]], axis=1).std(axis=1)*10
time_pepc=np.linspace(0,2000,len(pepc))


n_r1= pd.read_csv('data/n_r1', delim_whitespace=True)
n_r1.columns=['time','TYR', 'OH', 'n', 'n']
n_r1=n_r1[['time','TYR', 'OH']]
n_r1=n_r1[:197500]


n_r2= pd.read_csv('data/n_r2', delim_whitespace=True)
n_r2.columns=['time','TYR', 'OH', 'n', 'n']
n_r2=n_r2[['time','TYR', 'OH']]
n_r2=n_r2[:197500]


window=1
n=pd.concat([n_r1[['OH']], n_r2[['OH']]], axis=1)*10
n_err=pd.concat([n_r1[['OH']], n_r2[['OH']]], axis=1).std(axis=1)*10
time_n=np.linspace(0,2000,len(n))



s1i8_r1= pd.read_csv('data/s1i8_r1', delim_whitespace=True)
s1i8_r1.columns=['time','TYR', 'OH', 'n', 'n']
s1i8_r1=s1i8_r1[['time','TYR', 'OH']]
s1i8_r1=s1i8_r1[:197500]


s1i8_r2= pd.read_csv('data/s1i8_r2', delim_whitespace=True)
s1i8_r2.columns=['time','TYR', 'OH', 'n', 'n']
s1i8_r2=s1i8_r2[['time','TYR', 'OH']]
s1i8_r2=s1i8_r2[:197500]


window=50
s1i8=pd.concat([s1i8_r1[['OH']], s1i8_r2[['OH']]], axis=1)*10
s1i8_err=pd.concat([s1i8_r1[['OH']], s1i8_r2[['OH']]], axis=1)*10
time_s1i8=np.linspace(0,2000,len(s1i8))





plt.figure(figsize=(15,15))


ax=plt.subplot(3,4,1)
plt.plot(time_sopc,sopc.rolling(window).mean(), label='SOPC (C18:0,C18:1)' )
#plt.fill_between(time_sopc,sopc.rolling(window).mean()+sopc_err.rolling(window).mean(), sopc.rolling(window).mean()- sopc_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=12)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
#plt.legend(fontsize=20)
plt.xlim(0,2000)
plt.xlabel('Time (ns)', fontsize=12)
plt.ylim(0,20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xticks([0,500,1000,1500,2000])
#plt.yticks([0,5,10,15])
plt.title('SOPC', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'a', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax=plt.subplot(3,4,2)
plt.plot(time_popc,popc.rolling(window).mean(), label='POPC (C16:0,C18:1)' )
#plt.fill_between(time_popc,popc.rolling(window).mean()+popc_err.rolling(window).mean(), popc.rolling(window).mean()- popc_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
#plt.ylabel('RMSD', fontsize=12)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
#plt.legend(fontsize=20)
plt.xlim(0,2000)
plt.xlabel('Time (ns)', fontsize=12)
plt.ylim(0,20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xticks([0,500,1000,1500,2000])
#plt.yticks([0,5,10,15])
plt.title('POPC', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'b', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax=plt.subplot(3,4,3)
plt.plot(time_dmpc,dmpc.rolling(window).mean(), label='DMPC(di-C14:0)' )
#plt.fill_between(time_dmpc,dmpc.rolling(window).mean()+dmpc_err.rolling(window).mean(), dmpc.rolling(window).mean()- dmpc_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
#plt.ylabel('RMSD', fontsize=12)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
#plt.legend(fontsize=20)
plt.xlabel('Time (ns)', fontsize=12)
plt.xlim(0,2000)
plt.ylim(0,20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xticks([0,500,1000,1500,2000])
#plt.yticks([0,5,10,15])
plt.title('DMPC', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'c', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax=plt.subplot(3,4,4)
plt.plot(time_pepc,pepc.rolling(window).mean(), label='AT1R-SOPC:SOPE' )
#plt.fill_between(time_pepc,pepc.rolling(window).mean()+pepc_err.rolling(window).mean(), pepc.rolling(window).mean()- pepc_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
plt.xlim(0,2000)
plt.ylim(0,20)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xticks([0,500,1000,1500,2000])
#plt.yticks([0,5,10,15])
plt.title('SOPC:SOPE', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'd', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax=plt.subplot(3,4,5)
plt.plot(time_st5,st5.rolling(window).mean(), label=r'$\gamma$ = 5 mN/m' )
#plt.fill_between(time_st5,st5.rolling(window).mean()+st5_err.rolling(window).mean(), st5.rolling(window).mean()- st5_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=12)
#plt.ylabel('RMSD', fontsize=12)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
#plt.legend(fontsize=20)
plt.xlim(0,2000)
plt.ylim(0,20)
plt.xlabel('Time (ns)', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xticks([0,500,1000,1500,2000])
#plt.yticks([0,5,10,15])
plt.title('SOPC + 5 mN/m', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'e', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))


ax=plt.subplot(3,4,6)
plt.plot(time_st10,st10.rolling(window).mean(), label=r'$\gamma$ = 10 mN/m'  )
#plt.fill_between(time_st10,st10.rolling(window).mean()+st10_err.rolling(window).mean(), st10.rolling(window).mean()- st10_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
#plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=15)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
#plt.legend(fontsize=20)
plt.xlim(0,2000)
plt.ylim(0,20)
plt.xlabel('Time (ns)', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.yticks([0,5,10,15])
#plt.xticks([0,500,1000,1500,2000])
plt.title('SOPC + 10 mN/m', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'f', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))


ax=plt.subplot(3,4,7)
plt.plot(time_st15,st15.rolling(window).mean(), label=r'$\gamma$ = 15 mN/m'  )
#plt.fill_between(time_st15,st15.rolling(window).mean()+st15_err.rolling(window).mean(), st15.rolling(window).mean()- st15_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
#plt.ylabel('RMSD', fontsize=12)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xlim(0,2000)
plt.ylim(0,20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xticks([0,500,1000,1500,2000])
#plt.yticks([0,5,10,15])
plt.title('SOPC + 15 mN/m', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'g', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax=plt.subplot(3,4,8)
plt.plot(time_st20,st20.rolling(1).mean(), label=r'$\gamma$ = 20 mN/m'  )
#plt.fill_between(time_st20,st20.rolling(1).mean()+st20_err.rolling(1).mean(), st20.rolling(1).mean()- st20_err.rolling(1).mean(), color='tab:blue', alpha=0.1 )
plt.xlim(0,2000)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.ylim(0,20)
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xticks([0,500,1000,1500,2000])
#plt.yticks([0,5,10,15])
plt.title('SOPC + 20 mN/m', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'h', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax=plt.subplot(3,4,11)
plt.plot(time_an,an.rolling(window).mean(), label='AT1R + S1I8 + Nanobody' )
#plt.fill_between(time_an,an.rolling(window).mean()+an_err.rolling(window).mean(), an.rolling(window).mean()- an_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
plt.xlim(0,2000)
plt.ylim(0,20)
#plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=15)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
#plt.legend(fontsize=15)
plt.xlabel('Time (ns)', fontsize=12)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.yticks([0,5,10,15])
#plt.xticks([0,500,1000,1500,2000])
plt.title('AT1R + S1I8 + Nanobody', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'k', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax=plt.subplot(3,4,12)
plt.plot(time_n,n.rolling(window).mean(), label='AT1R + Nanobody' )
#plt.fill_between(time_n,n.rolling(window).mean()+n_err.rolling(window).mean(), n.rolling(window).mean()- n_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
#plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=15)
#plt.legend(fontsize=20)
plt.xlabel('Time (ns)', fontsize=12)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlim(0,2000)
plt.ylim(0,20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xticks([0,500,1000,1500,2000])
#plt.yticks([0,5,10,15])
plt.title('AT1R + Nanobody', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'l', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))


ax=plt.subplot(3,4,9)
plt.plot(time_ang,ang.rolling(window).mean(), label='AT1R + AngII' )
#plt.fill_between(time_ang,ang.rolling(window).mean()+ang_err.rolling(window).mean(), ang.rolling(window).mean()- ang_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
plt.xlim(0,2000)
plt.ylim(0,20)
plt.xlabel('Time (ns)', fontsize=12)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
#plt.ylabel('RMSD', fontsize=12)
#plt.legend(fontsize=20)
plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.yticks([0,5,10,15])
#plt.xticks([0,500,1000,1500,2000])
plt.title('AT1R + AngII', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'i', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))


ax=plt.subplot(3,4,10)
plt.plot(time_s1i8,s1i8.rolling(window).mean(), label='AT1R + S1I8' )
#plt.fill_between(time_s1i8,s1i8.rolling(window).mean()+s1i8_err.rolling(window).mean(), s1i8.rolling(window).mean()- s1i8_err.rolling(window).mean(), color='tab:blue', alpha=0.1 )
plt.xlim(0,2000)
plt.ylim(0,20)
plt.axhline(y=11.71, linestyle='--', lw=1.5, color='0.5')
plt.axhline(y=4.43, linestyle='--', lw=1.5, color='tab:orange')
plt.xlabel('Time (ns)', fontsize=12)
#plt.ylabel('TYR215(OH) - TYR302(OH) ($\AA$)', fontsize=12)
plt.title('AT1R + S1I8', y=1, pad=-13, fontsize=20)
#plt.legend(fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.yticks([0,5,10,15])
#plt.xticks([0,500,1000,1500,2000])
plt.title('AT1R + S1I8 ', y=1, pad=-16, fontsize=12)
plt.text(-150, 22, 'j', ha='center', fontsize=20, fontweight='bold')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

plt.subplots_adjust(top=0.95, bottom=0.08, left=0.07, right=0.975, hspace=0.35, wspace=0.25)
plt.savefig('Figure_S2.png', dpi=300)
