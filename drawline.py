# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt



def makeline(pointi, pointf):
	xi, yi, zi = pointi
	xf, yf, zf = pointf
	x = np.linspace(xi, xf, 101)
	y = np.linspace(yi, yf, 101)
	z = np.linspace(zi, zf, 101)
	return np.vstack((x, y, z)).T

x = np.arange(0, 10)
y = np.copy(x)
z = np.copy(x)

fig = plt.figure()
ax = plt.axes(projection='3d')

for i in range(len(x)):
	line = makeline([x[i], 0, 0],[x[i], 0, 10])
	ax.plot3D(line[:,0], line[:,1], line[:,2], 'green')
	line = makeline([0, 0, z[i]],[10, 0, z[i]])
	ax.plot3D(line[:,0], line[:,1], line[:,2], 'green')

for i in range(len(x)):
	line = makeline([10, 0, z[i]],[10, 10, z[i]])
	ax.plot3D(line[:,0], line[:,1], line[:,2], 'green')
	line = makeline([10, y[i], 0],[10, y[i], 10])
	ax.plot3D(line[:,0], line[:,1], line[:,2], 'green')

for i in range(len(x)):
	line = makeline([x[i], 0, 10],[x[i], 10, 10])
	ax.plot3D(line[:,0], line[:,1], line[:,2], 'green')
	line = makeline([0, y[i], 10],[10, y[i], 10])
	ax.plot3D(line[:,0], line[:,1], line[:,2], 'green')

line = makeline([10, 0, 10],[10, 10, 10])
ax.plot3D(line[:,0], line[:,1], line[:,2], 'green')

line = makeline([0, 10, 10],[10, 10, 10])
ax.plot3D(line[:,0], line[:,1], line[:,2], 'green')

line = makeline([10, 10, 0],[10, 10, 10])
ax.plot3D(line[:,0], line[:,1], line[:,2], 'green')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#ax._axis3don = False
#plt.savefig('order2.jpeg')
plt.show()
