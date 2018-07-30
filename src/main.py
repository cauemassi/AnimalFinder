import csv

def csv2Tuple(path):
	file = csv.reader(open(path), delimiter= ',')
	tup = []
	for row in file:
		aux = []
		for element in row:
			try:
				aux += [int(element)]
			except:
				aux += [element]
		tup += [aux]
	return tup

print(csv2Tuple("C:\\Users\\Caue\\Documents\\Workshop Python\\Projeto\\docs\\zoo.data"))	

