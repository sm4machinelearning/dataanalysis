# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(18,15))
ax = fig.add_subplot(111, projection='3d')
colorbar = ['r','lawngreen']

for j in range(10):
        for i in range(10):
                x = np.linspace(i, i+1, 11)
                y = np.linspace(0, 0.1, 11)
                X, Y = np.meshgrid(x, y)
                Y[:,:] = 0
                z = np.linspace(j, j+1, 11)
                Z,Z = np.meshgrid(z, z)
                c = (j)%2
                ax.plot_surface(X, Y, Z, color=colorbar[c])

for j in range(10):
        for i in range(10):
                x = np.linspace(i, i+1, 11)
                y = np.linspace(0, 0.1, 11)
                X, Y = np.meshgrid(x, y)
                Y = np.copy(X)
		X[:,:] = 10
                z = np.linspace(j, j+1, 11)
                Z,Z = np.meshgrid(z, z)
                c = (j)%2
                ax.plot_surface(X, Y, Z, color=colorbar[c])

for j in range(10):
        for i in range(10):
                x = np.linspace(i, i+1, 11)
                y = np.linspace(j, j+1, 11)
                X, Y = np.meshgrid(x, y)
                z = np.linspace(j, j+1, 11)
                Z,Z = np.meshgrid(z, z)
		Z[:,:] = 10
                ax.plot_surface(X, Y, Z, color=colorbar[1])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax._axis3don = False
#plt.show()
plt.savefig('order1new.jpeg')

