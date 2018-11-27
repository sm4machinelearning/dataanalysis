import numpy as np
from itertools import islice

dumpfile = 'coords.dat'
cell = 10
system = [cell, cell, cell]
box = [6.34065, 6.34065, 6.34065]
boxs = np.array(box)*np.array(system)
unitcell = 6
lines = 9+(unitcell*system[0]*system[1]*system[2])
lines = 6509
dipolefilename = 'hbonds'
buffer = 2.0

def caldist(a, b):
	return np.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)

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

methamhbonds = open('methamhbonds','ab')
formahbonds = open('methamhbonds','ab')

with open(dumpfile) as file:
	while True:
		data = list(islice(file,lines))
		if not data:
			break
		else:
			mat = np.zeros((1,5))
			data = data[9:]
			data = np.genfromtxt(data, dtype='str')
			data = np.delete(data, [1,3], axis=1)
			data = data.astype(float)
			imgm = data[:,5:]
			imgm = imgm.astype(int)
			imgm = boxs*imgm
			data = data[:,:5]
			data[:,2:] = data[:,2:] + imgm
			
			data[:,2] = data[:,2] - np.min(data[:,2]) 
			data[:,3] = data[:,3] - np.min(data[:,3]) 
			data[:,4] = data[:,4] - np.min(data[:,4]) 
		
			datamod = np.copy(data)
			datamod[:,2] = datamod[:,2] + (boxs[0])
			data = np.vstack((data, datamod))
			
			datamod = np.copy(data)
			datamod[:,3] = datamod[:,3] + (boxs[1])
			data = np.vstack((data, datamod))
			
			datamod = np.copy(data)
			datamod[:,4] = datamod[:,4] + (boxs[2])
			data = np.vstack((data, datamod))
			data = data[np.where((data[:,2] < (boxs[0] + 4.0)) & (data[:,3] < (boxs[1] + 4.0)) & (data[:,4] < (boxs[2] + 4.0)))]

			ids = data[:,1]
			ids = ids.astype(int)
			datai = data[np.where(ids == 2)]
			datahm = data[np.where(ids == 10)]
			datahf = data[np.where((ids == 6) | (ids == 7))]

			np.savetxt('sys.xyz', data[:,1:], delimiter='        ', fmt='%s')
'''
			#with methylammonium
			bonds = []
			for z in range(cell):
				for y in range(cell):
					for x in range(cell):
						lenxi = [(box[0] * x) - buffer, (box[0] * x) + box[0] + buffer] # dimensions in x
						lenyi = [(box[1] * y) - buffer, (box[1] * y) + box[1] + buffer] # dimensions in y
						lenzi = [(box[2] * z) - buffer, (box[2] * z) + box[2] + buffer] # dimensions in z
			
						sort = np.where((datai[:,2] > lenxi[0]) & (datai[:,2] < lenxi[1]) & 
								(datai[:,3] > lenyi[0]) & (datai[:,3] < lenyi[1]) & 
								(datai[:,4] > lenzi[0]) & (datai[:,4] < lenzi[1]))
						datasorti =  datai[sort]

						lenxh = [(box[0] * x), (box[0] * x) + box[0]] # dimensions in x
						lenyh = [(box[1] * y), (box[1] * y) + box[1]] # dimensions in y
						lenzh = [(box[2] * z), (box[2] * z) + box[2]] # dimensions in z
						
						datah = np.copy(datahm)
						sort = np.where((datah[:,2] > lenxh[0]) & (datah[:,2] < lenxh[1]) & 
								(datah[:,3] > lenyh[0]) & (datah[:,3] < lenyh[1]) & 
								(datah[:,4] > lenzh[0]) & (datah[:,4] < lenzh[1]))
						datasorth =  datah[sort]
						
						num = 0
						for ihs in range(datasorth.shape[0]):
							for ios in range(datasorti.shape[0]):
								if caldist(datasorth[ihs,2:], datasorti[ios,2:]) < 3.0:
									expr = str(int(datasorth[ihs,0])) + '-' + str(int(datasorti[ios,0]))
									bonds.append(expr)
			np.savetxt(methamhbonds, np.reshape(np.array(bonds), (1,len(bonds))), delimiter=',', fmt='%s')

			#with formamidinium
			bonds = []
			for z in range(cell):
				for y in range(cell):
					for x in range(cell):
						lenxi = [(box[0] * x) - buffer, (box[0] * x) + box[0] + buffer] # dimensions in x
						lenyi = [(box[1] * y) - buffer, (box[1] * y) + box[1] + buffer] # dimensions in y
						lenzi = [(box[2] * z) - buffer, (box[2] * z) + box[2] + buffer] # dimensions in z
			
						sort = np.where((datai[:,2] > lenxi[0]) & (datai[:,2] < lenxi[1]) & 
								(datai[:,3] > lenyi[0]) & (datai[:,3] < lenyi[1]) & 
								(datai[:,4] > lenzi[0]) & (datai[:,4] < lenzi[1]))
						datasorti =  datai[sort]

						lenxh = [(box[0] * x), (box[0] * x) + box[0]] # dimensions in x
						lenyh = [(box[1] * y), (box[1] * y) + box[1]] # dimensions in y
						lenzh = [(box[2] * z), (box[2] * z) + box[2]] # dimensions in z
			
						datah = np.copy(datahf)
						sort = np.where((datah[:,2] > lenxh[0]) & (datah[:,2] < lenxh[1]) & 
								(datah[:,3] > lenyh[0]) & (datah[:,3] < lenyh[1]) & 
								(datah[:,4] > lenzh[0]) & (datah[:,4] < lenzh[1]))
						datasorth =  datah[sort]
						
						num = 0
						for ihs in range(datasorth.shape[0]):
							for ios in range(datasorti.shape[0]):
								if caldist(datasorth[ihs,2:], datasorti[ios,2:]) < 3.0:
									expr = str(int(datasorth[ihs,0])) + '-' + str(int(datasorti[ios,0]))
									bonds.append(expr)
			np.savetxt(formahbonds, np.reshape(np.array(bonds), (1,len(bonds))), delimiter=',', fmt='%s')

methamhbonds.close()
formahbonds.close()
'''
