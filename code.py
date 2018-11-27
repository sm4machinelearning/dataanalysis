import numpy as np
import random
import math

percentma = int(raw_input('Give percentage of MA: '))

################Rotation function#############
def rot(mol):
	theta = math.radians(np.random.randint(361, size=1))
	phi = math.radians(np.random.randint(361, size=1))
	a = math.sin(theta)
	b = math.cos(theta)
	c = math.sin(phi)
	d = math.cos(phi)
	rotmat = np.array([[b, a*d, a*c], [-a, b*d, b*c], [0, -c, d]])
	for i in range(mol.shape[0]):
		vector = np.array([[mol[i,0]], [mol[i,1]], [mol[i,2]]])
		vector = np.dot(rotmat,vector)
		vector = vector.T
		mol[i,0], mol[i,1], mol[i,2] = vector[0,0], vector[0,1], vector[0,2]
	return mol

################Cations treatment################
ma = open('ma.xyz', 'r').readlines()
ma = ma[2:]
ma = np.genfromtxt(ma, dtype='str')
mapos = ma[:,1:].astype(float)
meanx, meany, meanz = np.mean(mapos[:,0]), np.mean(mapos[:,1]), np.mean(mapos[:,2])
mapos[:,0] = mapos[:,0] - meanx
mapos[:,1] = mapos[:,1] - meany
mapos[:,2] = mapos[:,2] - meanz
ma[:,1:] = mapos
manames = ['C4','H4','H4','H4','H5','H5','H5','N5']

fa = open('fa.xyz', 'r').readlines()
fa = fa[2:]
fa = np.genfromtxt(fa, dtype='str')
fapos = fa[:,1:].astype(float)
meanx, meany, meanz = np.mean(fapos[:,0]), np.mean(fapos[:,1]), np.mean(fapos[:,2])
fapos[:,0] = fapos[:,0] - meanx
fapos[:,1] = fapos[:,1] - meany
fapos[:,2] = fapos[:,2] - meanz
fa[:,1:] = fapos
fanames = ['C1','H1','N1','H2','H3','N1','H3','H2']

###############Systems########################
fapi = float(6.3613)
mapi = float(6.320)
#fa85ma15pbi = 6.375
#fa15ma85pbi = 6.319

##############Criterias#######################
lcar = np.linspace(fapi, mapi, 101)
lc = lcar[percentma]
percentma = percentma*10
systemsize = 10
inx, iny, inz = systemsize, systemsize, systemsize
lenx, leny, lenz = lc*systemsize, lc*systemsize, lc*systemsize

#############Form the system##################
mapos = random.sample(range(1, 999), percentma)
cats = np.zeros((1000,1), dtype='str')
cats[:] = 'F'
#mapos = np.arange(1, 1000, 2)
#cats[mapos] = 'M'

alls = np.zeros((1000, 3))
num = 0
for i in range(systemsize):
	for j in range(systemsize):
		for k in range(systemsize):
			alls[num] = np.asarray([i, j, k])
			num +=1


alls = alls*lc
alls = np.around(alls, decimals=3)

###########Writing system positions###########
file = open('system.xyz', 'w')
file.write('12000')
file.write('\n')
file.write('Lattice="' + '%s 0.0 0.0 0.0 %s 0.0 0.0 0.0 %s' % (lc*10, lc*10, lc*10) + '" Properties=species:S:1:pos:R:3:molid:I:1:type:S:1 pbc="T T T"')
file.write('\n')
for i in range(alls.shape[0]):
	file.write(' '.join(map(str, np.array(['Pb', alls[i,0], alls[i,1], alls[i,2]]))))
	file.write(' ' + str(i + 1) + ' P1'  + '\n')
	file.write(' '.join(map(str, np.array(['I' , alls[i,0]+lc/2., alls[i,1], alls[i,2]]))))
	file.write(' ' + str(i + 1) + ' I1'  + '\n')
	file.write(' '.join(map(str, np.array(['I' , alls[i,0], alls[i,1]+lc/2., alls[i,2]]))))
	file.write(' ' + str(i + 1) + ' I1'  + '\n')
	file.write(' '.join(map(str, np.array(['I' , alls[i,0], alls[i,1], alls[i,2]+lc/2.]))))
	file.write(' ' + str(i + 1) + ' I1'  + '\n')
	if cats[i] == 'M':
		mamod = np.copy(ma)
		maposit = mamod[:,1:].astype(float)
		maposit = rot(maposit)
		maposit = np.around(maposit + alls[i] + lc/2., decimals=3)
		mamod[:,1:] = maposit
		for j in range(mamod.shape[0]):
			file.write(' '.join(map(str, mamod[j])))
			file.write(' ' + str(i + 1) + ' '  + str(manames[j]) + '\n')
	else:
		famod = np.copy(fa)
		faposit = famod[:,1:].astype(float)
		faposit = rot(faposit)
		faposit = np.around(faposit + alls[i] + lc/2., decimals=3)
		famod[:,1:] = faposit
		for j in range(famod.shape[0]):
			file.write(' '.join(map(str, famod[j])))
			file.write(' ' + str(i + 1) + ' '  + str(fanames[j]) + '\n')
file.close()	
