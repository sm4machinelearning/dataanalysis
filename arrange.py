import numpy as np

arr = ['Pb','I','C','HC','N','HN']
arr = ['Pb','I','C','HC','HN','N']
arr = ['Pb','I','C','HC','N','HN','C','HC','HN','N']
arr = ['Pb','I','C','HC','N','HN', 'HN','C','HC','HN','N']

file = open('pair','r')
data = file.readlines()
file.close()

for i in range(len(data)):
        data[i] = data[i].split()
        data[i][3] = ' '.join(data[i][3:])
        del data[i][4:]
data = np.asarray(data, dtype='str')

file = open('pairnow', 'w')

for i in range(len(arr)):
        for j in range(i,len(arr)):
                a, b = arr[i], arr[j]
                row = data[np.where((data[:,1] == a) & (data[:,2] == b))]
		if len(row) > 0:
			row[0][1], row[0][2] = i+1, j+1
                else:
                        row = data[np.where((data[:,1] == b) & (data[:,2] == a))]
			row[0][1], row[0][2] = i+1, j+1
		row = np.asarray(row, dtype='str')
		file.write(' '.join(map(str, row[0])))
		file.write('\n')

file.close()

