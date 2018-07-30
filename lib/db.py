import sqlite3
import csv

class db():
	def __init__(self):
		#self.conn = sqlite3.connect("C:\\Users\\Caue\\Documents\\Workshop Python\\Projeto\\db\\animals.db")
		self.conn = sqlite3.connect("C:\\Workshop Python\\AnimalFinder\\db\\animals.db")
		self.cursor = self.conn.cursor()		

	def createAnimalsTable(self):
		self.cursor.execute("""
		CREATE TABLE IF NOT EXISTS animais (
       	name		TEXT NOT NULL,
        hair 		INTEGER NOT NULL,
        featers		INTEGER NOT NULL,
        eggs 		INTEGER NOT NULL,
        milk 		INTEGER NOT NULL,
        airborne 	INTEGER NOT NULL,
        aquatic 	INTEGER NOT NULL,
        predator 	INTEGER NOT NULL,
        toothed 	INTEGER NOT NULL,
        backbone 	INTEGER NOT NULL,
        breathes 	INTEGER NOT NULL,
        venomous 	INTEGER NOT NULL,
        fins 		INTEGER NOT NULL,
        legs 		INTEGER NOT NULL,
        tail 		INTEGER NOT NULL,
        domestic 	INTEGER NOT NULL,
        catsize 	INTEGER NOT NULL,
        type 		INTEGER NOT NULL
		);
		""")

	def insertData(self, lista):
		self.cursor.executemany("""
			INSERT INTO animais (name, hair, featers, eggs,
			milk, airborne, aquatic, predator, toothed, backbone,
			breathes, venomous, fins, legs, tail, domestic, catsize, type)
			VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
			""", lista)
		self.conn.commit()

	def executeQuery(self, query):
		return self.cursor.execute(query)


