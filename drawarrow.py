import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import math

x = np.arange(0, 10, 1)
y = np.arange(0, 10, 1)

theta =  np.random.randint(361, size=100)
phi =  np.random.randint(361, size=100)

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

carbs = np.zeros((100,3))
nitrs = np.ones((100,3))

for num in range(len(theta)):
	thet = theta[num]
	ph = phi[num]
	ang1 = math.radians(thet)
	ang2 = math.radians(ph)
	a = math.sin(ang1)
	b = math.cos(ang1)
	c = math.sin(ang2)
	d = math.cos(ang2)
	rotmat = np.array([[b, a*d, a*c], [-a, b*d, b*c], [0, -c, d]])
	vector = np.array([[nitrs[num,0]],[nitrs[num,1]],[nitrs[num,2]]])
	vector = np.dot(rotmat, vector)
	vector = vector.T
	nitrs[num] = vector

cmat = np.copy(carbs)
num = 0
for i in range(len(x)):
	for j in range(len(x)):
		cmat[num] = [x[i], x[j], 0]
		num += 1

cmat = cmat*3

carbs = carbs + cmat
nitrs = nitrs + cmat
c = np.copy(carbs)
n = np.copy(nitrs)

fig = plt.figure(figsize=(30,30))
ax = fig.add_subplot(111, projection='3d')

for i in range(c.shape[0]):
	xs = [c[i,0], n[i,0]]
	ys = [c[i,1], n[i,1]]
	zs = [c[i,2], n[i,2]]
	a = Arrow3D(xs, ys, zs, mutation_scale=30, lw=3, arrowstyle='-|>', color='b')
	ax.add_artist(a)

ax.view_init(azim=0, elev=90)
ax.set_top_view()
plt.axis('off')
ax.grid(False)
plt.xlim(0, 30)
plt.ylim(0, 30)
ax.set_zlim(-4, 4)
plt.savefig('randomarrows2.jpeg')
#plt.show()



'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

x = np.arange(0, 10, 1)
y = np.arange(0, 10, 1)

theta =  np.random.randint(361, size=100)
phi =  np.random.randint(361, size=100)

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

data = np.genfromtxt('image', dtype=str)
data = data[:,3:]
datamod = np.asarray(data[:,1:], dtype=float)
datamod[:,3] = datamod[:,3] * 62.34
datamod[:,0] = datamod[:,0] + datamod[:,3]
datamod[:,4] = datamod[:,4] * 62.35
datamod[:,1] = datamod[:,1] + datamod[:,4]
datamod[:,5] = datamod[:,5] * 61.62
datamod[:,2] = datamod[:,2] + datamod[:,5]
data = data[:,0:4]
data[:,1] = datamod[:,0]
data[:,2] = datamod[:,1]
data[:,3] = datamod[:,2]

c = data[np.where(data[:,0] == 'C')]
n = data[np.where(data[:,0] == 'N')]
c = np.around(np.asarray(c[:,1:], dtype=float),decimals=2)
n = np.around(np.asarray(n[:,1:], dtype=float), decimals=2)

directions = np.copy(n)
directions = c - directions

cmat = np.copy(c)
num = 0
for i in range(len(x)):
	for j in range(len(x)):
		cmat[num] = [x[i], x[j], 0]
		num += 1

directions = directions + cmat
c = np.copy(cmat)
n = np.copy(directions)

fig = plt.figure(figsize=(30,30))
ax = fig.add_subplot(111, projection='3d')

for i in range(c.shape[0]):
	xs = [c[i,0], n[i,0]]
	ys = [c[i,1], n[i,1]]
	zs = [c[i,2], n[i,2]]
	a = Arrow3D(xs, ys, zs, mutation_scale=30, lw=3, arrowstyle='-|>', color='b')
	ax.add_artist(a)

ax.view_init(azim=0, elev=90)
ax.set_top_view()
plt.axis('off')
ax.grid(False)
plt.xlim(0, 11)
plt.ylim(0, 11)
ax.set_zlim(-4, 4)
plt.savefig('randomarrows.jpeg')
#plt.show()
'''


