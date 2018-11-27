import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import argparse
#https://stackoverflow.com/questions/643699/how-can-i-use-numpy-correlate-to-do-autocorrelation/21863139


arr = ['mapi', 'fapi', 'n2', 'n3', 'n4']

def fitexp(t, a, tau):
        return a * np.exp((-1)*(t/tau))

def fitbiexp(t, a1, tau1, a2, tau2):
        return a1 * np.exp((-1)*(t/tau1)) + a2 * np.exp((-1)*(t/tau2))

def fittriexp(t, a1, tau1, a2, tau2, a3, tau3):
        return a1 * np.exp((-1)*(t/tau1)) + a2 * np.exp((-1)*(t/tau2)) + a3 * np.exp((-1)*(t/tau3))


for i in range(len(arr)):
	plotdata = np.genfromtxt(arr[i])
	timelength = 100
	chosefit = fitexp

	xaxis = np.linspace(0, timelength, plotdata.shape[0])
	popt, pcov = curve_fit(chosefit, xaxis, plotdata)
	print popt
#	plt.plot(xaxis, chosefit(xaxis, *popt), linewidth=3)
	plt.plot(xaxis, plotdata, linewidth=5)
	plt.ylim(-0.2, 1.0)

plt.legend(arr)
plt.xlabel('Time (picoseconds)')
plt.ylabel('Autocorrelation')
plt.savefig('allplot.png')
	#plt.savefig('totalplot.png')


