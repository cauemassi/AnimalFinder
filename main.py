from lib import db
from lib import animalHelper
import numpy as np
from sklearn.neighbors import NearestNeighbors

def main():
	print("Pense em um animal, iremos tentar acertar!")
	animal = animalHelper.animalHelper().createAnimal()
	data_base = db.db()
	allAnimals = data_base.executeQuery("select * from animais")
	listAnimalCharacteristics = []
	listAnimalNames = []
	for ani in allAnimals:
		listAnimalCharacteristics += [ani[1:len(ani) - 1]]
		listAnimalNames += [ani[0]]
	nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(listAnimalCharacteristics)

	distance, indice = nbrs.kneighbors(np.array([animal]))

	print("O animal que você pensou foi " + listAnimalNames[int(indice)])

main()