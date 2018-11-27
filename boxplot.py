# 1 = Step 
# 2 = PotEng 
# 3 = E_bond 
# 4 = E_angle 
# 5 = E_coul 
# 6 = E_vdwl 
# 7 = E_long 
# 8 = E_tail 
# 9 = E_pair 
# 10 = KinEng 
# 11 = TotEng 
# 12 = Time 
# 13 = Temp 

import numpy as np
import matplotlib.pyplot as plt

def lines(filename):
	start = []
	end = []
	with open(filename) as myfile:
		for num, line in enumerate(myfile, 1):
			if 'Step' in line:
				start.append(num)
			if 'Loop time' in line:
				end.append(num)
	return start, end

arr = ['order5','order6','random','order1','order2','order3']

whichen = 1

outputfile = arr[0]
start, end = lines(outputfile)
file = open(outputfile,'r')
data = file.readlines()
file.close()
prod = np.genfromtxt(data[start[1]:end[1]-2])
order5 = prod[:,whichen]

outputfile = arr[1]
start, end = lines(outputfile)
file = open(outputfile,'r')
data = file.readlines()
file.close()
prod = np.genfromtxt(data[start[1]:end[1]-2])
order6 = prod[:,whichen]

outputfile = arr[2]
start, end = lines(outputfile)
file = open(outputfile,'r')
data = file.readlines()
file.close()
prod = np.genfromtxt(data[start[1]:end[1]-2])
random = prod[:,whichen]

outputfile = arr[3]
start, end = lines(outputfile)
file = open(outputfile,'r')
data = file.readlines()
file.close()
prod = np.genfromtxt(data[start[1]:end[1]-2])
order1 = prod[:,whichen]

outputfile = arr[4]
start, end = lines(outputfile)
file = open(outputfile,'r')
data = file.readlines()
file.close()
prod = np.genfromtxt(data[start[1]:end[1]-2])
order2 = prod[:,whichen]

outputfile = arr[5]
start, end = lines(outputfile)
file = open(outputfile,'r')
data = file.readlines()
file.close()
prod = np.genfromtxt(data[start[1]:end[1]-2])
order3 = prod[:,whichen]

dataplot = [order5,order6,random, order1, order2, order3]

colors = ['k','g','c','y','m','b']

fig = plt.figure(1, figsize=(12,6))
ax = fig.add_subplot(111)
bp = ax.boxplot(dataplot, patch_artist=True)

for patch, color in zip(bp['boxes'], colors):
	patch.set_facecolor(color)

ax.set_xticklabels(['Separated','Blocks','Random', 'Planes', 'Pillars', 'Dots'], fontsize=20)
[t.set_color(i) for (i,t) in zip(colors,ax.xaxis.get_ticklabels())]
ax.tick_params(axis='y', which='major', labelsize=15)
ax.set_ylabel('Energy(Kcal/mole)', fontsize=20)


#plt.show()
plt.savefig('potenergy.tiff')




'''
data = np.copy(prod)
data = np.delete(data, [0, 2, 3, 7, 11], axis=1)
legendar = ['Epot', 'Ecoul', 'Evdw', 'Elong','Epair', 'KE', 'TotE', 'Temp']
fig = plt.figure(figsize=(24, 8))
for i in range(data.shape[1]):
	a = plt.subplot(2, 4, i+1)
	a.plot(data[:,i], label=legendar[i])
	a.set_title(legendar[i])
plt.savefig('energy.png')
'''


