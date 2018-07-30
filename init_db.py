from lib import db
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

def main():
	tup = csv2Tuple("C:\\Users\\Caue\\Documents\\Workshop Python\\Projeto\\docs\\zoo.data")
	data_base = db.db()
	data_base.createAnimalsTable()
	data_base.insertData(tup)

main()


