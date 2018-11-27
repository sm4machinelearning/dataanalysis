import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import argparse
#https://stackoverflow.com/questions/643699/how-can-i-use-numpy-correlate-to-do-autocorrelation/21863139


arr = ['100cordata', '150cordata', '200cordata', '250cordata', '300cordata', '350cordata']
arr = ['100a','150a','200a','250a','300a','350a']
arr = ['separated/300-cordata','blocks/300-cordata','random/300-50ma-cordata','planes/300-cordata','pillars/300-cordata','dots/300-cordata']
arr = ['separated/300-cordatafa','blocks/300-cordatafa','random/300-random-cordatafa','planes/300-cordatafa','pillars/300-cordatafa','dots/300-cordatafa', 'fapi_300_cordata']
arr = ['separated/300-cordatama','blocks/300-cordatama','random/300-random-cordatama','planes/300-cordatama','pillars/300-cordatama','dots/300-cordatama', 'mapi_300_cordata']



def fitbiexp(t, a1, tau1, tau2):
        return a1 * np.exp((-1)*(t/tau1)) + (1 - a1) * np.exp((-1)*(t/tau2))

fig, ax = plt.subplots(figsize=(12,10))
colors = ['k','g','c','y','m','b','r']

for i in range(len(arr)):
	plotdata = np.genfromtxt(arr[i])
	timelength = 100
	chosefit = fitbiexp

	xaxis = np.linspace(0, timelength, plotdata.shape[0])
	popt, pcov = curve_fit(chosefit, xaxis, plotdata, bounds=([0, 0, 0], [1, np.inf, np.inf]))
	print popt
	ax.plot(xaxis, plotdata, linewidth=1, color=colors[i])
#	ax.plot(xaxis, chosefit(xaxis, *popt), '--', linewidth=6, label='_nolegend_')
	plt.ylim(-0.2, 1.0)
	plt.xlim(0.0, 100.0)

ax.legend(['Separated','Blocks','Random','Planes','Pillars','Dots','FAPI'], fontsize=20)
plt.xlabel('Time (picoseconds)', fontsize=30)
plt.ylabel('Autocorrelation', fontsize=30)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
'''SMALL_SIZE = 15
MEDIUM_SIZE = 50
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title'''


#plt.savefig('allfitbiexp.png')
plt.show()
#plt.clf()


'''
xt = np.linspace(100, 350, 6)
timelin[:,0] = xt
timeexp[:,0] = xt

plt.plot(timelin[:,0], timelin[:,1])
plt.xlabel('Temperature (K)')
plt.ylabel('Linear decay constant')
plt.savefig('timelin.png')
#plt.show()
plt.clf()

plt.plot(timeexp[:,0], timeexp[:,1])
plt.xlabel('Temperature (K)')
plt.ylabel('Exponential decay constant')
#plt.savefig('timeexp.png')
plt.show()'''
