import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import argparse
from scipy.optimize import minimize
#https://stackoverflow.com/questions/643699/how-can-i-use-numpy-correlate-to-do-autocorrelation/21863139

parser = argparse.ArgumentParser(description = 'read correlation file')
parser.add_argument('correlationfile', type=str, help='correlation file')
args = parser.parse_args()
b = open(args.correlationfile, 'r')
correlationfile = b.readlines()

def fitexp(t, tau):
        return np.exp((-1)*(t/tau))

def fitexp2(t, tau):
        return plotdata2[0]*np.exp((-1)*(t/tau))

def fitbiexp(t, a1, tau1, tau2):
        return a1 * np.exp((-1)*(t/tau1)) + (plotdata2[0] - a1) * np.exp((-1)*(t/tau2))

def fittriexp(t, a1, tau1, a2, tau2, a3, tau3):
        return a1 * np.exp((-1)*(t/tau1)) + a2 * np.exp((-1)*(t/tau2)) + a3 * np.exp((-1)*(t/tau3))

def fitstrexp(t, tau, mu):
        return np.exp((-1)*((t/tau)**(mu)))

def fitlinexp(t, al, taul, taue):
        return al * taul*t + (1 - al) * np.exp((-1)*(t/taue))

def fitlinstrexp(t, taul, taue, mu):
        return taul*t + (1 - taul) * np.exp((-1)*((t/taue)**mu))

plotdata = np.genfromtxt(correlationfile)
timelength = 100

x = np.linspace(0, timelength, plotdata.shape[0])
x1, x2 = np.copy(x), np.copy(x)
x1 = x1[x1<=1.0]
x2 = x2[x2>1.0]
x2 = x2 - 1.0

plotdata1 = plotdata[:len(x1)]
plotdata2 = plotdata[len(x1):]
chosefit1 = fitexp
chosefit2 = fitbiexp

popt1, pcov1 = curve_fit(chosefit1, x1, plotdata1, bounds=([0],[np.inf]))
popt2, pcov2 = curve_fit(chosefit2, x2, plotdata2, bounds=([0,0,0],[1,np.inf,np.inf]))

plt.plot(x1, plotdata1, linewidth=6)
plt.plot(x1, chosefit1(x1, *popt1), '--', linewidth=3)

plt.plot(x2+1, plotdata2, linewidth=6)
plt.plot(x2+1, chosefit2(x2, *popt2), '--', linewidth=3)

print popt1
print popt2

plt.ylim(-0.2, 1.2)
plt.show()

'''
chosefit = fittriexp

xaxis = np.linspace(0, timelength, plotdata.shape[0])
#popt, pcov = curve_fit(chosefit, xaxis, plotdata, bounds=([-np.inf, 0, 0], [0, np.inf, 1]))
#popt, pcov = curve_fit(chosefit, xaxis, plotdata, bounds=([0, 0, 0],[1, np.inf, np.inf]), p0=[0.3,0.0002,200])
popt, pcov = curve_fit(chosefit, xaxis, plotdata, bounds=([0,0,0],[1,np.inf,np.inf]))
#popt, pcov = curve_fit(chosefit, xaxis, plotdata, bounds=([0,0,0,0,0,0],[1,np.inf,1,np.inf,1,np.inf]))

print popt
plt.plot(xaxis, plotdata, linewidth=6)
plt.plot(xaxis, chosefit(xaxis, *popt), '--', linewidth=3)
plt.ylim(-0.2, 1.2)
plt.show()
'''
