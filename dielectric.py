import numpy as np
from itertools import islice
import os
#The dipole moment is d=sigma(ri-R)qi where qi is the charge of the i-th particle in the molecule and ri its position. R is the center around which a multipole moment expansion is done. Changing the center R to R+delR changes the dipole moment by deld=sigmai(-delR)qi=-delRQ, where Q is the total charge of the molecule. The book by Griffiths "Introduction to Electrodynamics" or "Classical Electrodynamics" by Jackson should contain ample information of multipole expansions.
#Reference https://www.physicsforums.com/threads/does-the-concept-of-dipole-moment-of-charged-molecule-exist-or-not.683247/


boxmapi = [6.234, 6.235, 6.162]

box = boxmapi
dumpfile = 'dump.cn'
unitcell = 2
system = [10, 10, 10]
syssize = system[0]*system[1]*system[2]
lines = 9+(unitcell*system[0]*system[1]*system[2])
dpfile = 'dielect'
qc = 0.84
qn = 0.52

def sort(array):
        i = 0
        while i < array.shape[0]-1:
                j = i
                while j < array.shape[0]:
                        if float(array[i,3]) > float(array[j,3]):
                                arraytemp = np.copy(array)
                                arraytemp[i], arraytemp[j] = array[j], array[i]
                                array = np.copy(arraytemp)
                        j+=1
                i+=1
        return array

dpfile = open(dpfile,'ab')
with open(dumpfile) as file:
        while True:
                data = list(islice(file,lines))
                if not data:
                        break
                else:
                        mat = np.zeros(3)
                        data = data[9:]
                        i = 0
                        if unitcell == 2:
                                boxs = np.array(box)
                                boxs = boxs * system
                                while i < len(data)/unitcell:
                                        datum = data[i*unitcell:(i+1)*unitcell]
                                        datum = np.genfromtxt(datum, dtype='str')
                                        imgm = datum[:,7:]
                                        datum = datum[:,3:7]
                                        imgm = imgm.astype(int)
                                        imgm = imgm*boxs
                                        datasort = datum[:,1:].astype(float) + imgm
                                        datum = np.column_stack((datum[:,0], datasort))
                                        datum = sort(datum)
                                        c = datum[np.where(datum[:,0] == 'C')][0][1:].astype(float)
                                        n = datum[np.where(datum[:,0] == 'N')][0][1:].astype(float)
                                        vec = np.reshape(np.asarray([n[0] - c[0], n[1] - c[1], n[2] - c[2]]), (1,3))
                                        mat = mat + vec
                                        i += 1
                                np.savetxt(dpfile, np.reshape(mat, (1,3)), delimiter=',')




'''
f = "dump.100"


d = dump(path,0)
#a = read_lammps_data("data.spce",style="full")
a = read_lammps_data("data.dielec",style="full")

dipole2 = []
time = d.next()
while ( time != -1 ) :
	print time
	id_no,types, mol_id, charge, x, y, z = d.vecs(time,"id","type","mol","q","x","y","z")
	types = [int(k) for k in types]
	id_no = [int(i) for i in id_no]
	mol_id  = [int(j) for j in mol_id]
	pos = []
	for i,j,k in zip(x,y,z) :
		pos.append([i,j,k])
	pos = np.asarray(pos)

	ohh_list = get_ohh_list(mol_id,types)
	ohh_list = np.asarray(ohh_list)
	#cell = np.array([[22.873998,0,0],[0,22.873998,0],[0,0,22.873998]])                       
	cell = a.get_cell()
	
	vec_a, vec_b, vec_c = cell
	vec_a = cell[0,:]
	vec_b = cell[1,:]
	vec_c = cell[2,:]
	lat =  np.array([vec_a,vec_b,vec_c])
	lat_inv = np.linalg.inv(lat)

	dipole1 = 0#[]
	for i in ohh_list :
		O, H1, H2 = pos[i[0],0:3], pos[i[1],0:3],  pos[i[2],0:3]
		tran_o, tran_h1, tran_h2 = O.dot(lat_inv), H1.dot(lat_inv), H2.dot(lat_inv)	
		tran_O = tran_o - (2 * tran_o - 1 ).astype(int)
		tran_H1 = tran_h1 - (2 * tran_h1 - 1 ).astype(int) 
		tran_H2 = tran_h2 - (2 * tran_h2 - 1 ).astype(int)
	
		################## 1st hydrogen ###########################

		tempH1 = tran_O - tran_H1
		temp1 = tempH1 - (2.0 * tempH1).astype(int)
		dis_OH1 = temp1.dot(lat)
		#r_OH1 = np.linalg.norm(dis_OH1)
		#if r_OH1 > 2 : print r_OH1 ,id_no[i[0]],id_no[i[1]],id_no[i[2]]

		##########################################################

		################## 2nd Hydrogen ##########################
	
		tempH2 = tran_O - tran_H2
		temp2 = tempH2 - (2.0 * tempH2).astype(int)
		dis_OH2 = temp2.dot(lat)
		#r_OH2 = np.linalg.norm(dis_OH2)
		#if r_OH2 > 2 : print r_OH2 ,id_no[i[0]],id_no[i[1]],id_no[i[2]]

		##########################################################

		dipole_OH1 = charge[i[1]] * dis_OH1
		dipole_OH2 = charge[i[2]] * dis_OH2
		dipole_total = (dipole_OH1 + dipole_OH2)   #/0.208226 
		#dipole1.append(dipole_total)
		dipole1 += dipole_total
	dipole2.append(dipole1)
	time = d.next()	

############## Dielectric calculation ##############################

net_dipole = np.asarray(dipole2)

V = 22.873998 ** 3    #SPCE
#V = 31.0448 ** 3     #REAX
k_b = 8.6173303 * 1E-5
ep = (8.854187 * 1E-12 * 6.242 * 1E18) / 1E10
T = 300

M_list = []


vec_M = 0
for config in net_dipole :
	vec_M = config
	M_list.append( np.linalg.norm(vec_M) )

M2_acc = 0, 0
dielectric = []
for (Nt,abs_M) in enumerate(M_list):

	M2_acc += abs_M**2
	var_M = M2_acc / (Nt+1) -
	
	eps_r = 1 + (var_M ) / (3 * V * k_b * T*ep)
	dielectric.append(eps_r)

#print dielectric

v = open('dielectric_spce','w')
for m in dielectric:
        v.write('%s \n' % m)
v.close()

'''

