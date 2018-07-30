class animalHelper():

	def createAnimal(self):
		print("Digite 0 para não e 1 para sim!")
		hair = self.possibleValues([0,1], "O animal tem pelos? ")
		feathers = self.possibleValues([0,1], "O animal tem penas? ")
		eggs = self.possibleValues([0,1], "O animal bota ovos? ")
		milk = self.possibleValues([0,1], "O animal é mamifero? ")
		airborne = self.possibleValues([0,1], "O animal voa? ")
		aquatic = self.possibleValues([0,1], "O animal é aquatico? ")
		predator = self.possibleValues([0,1], "O animal é predador? ")
		toothed = self.possibleValues([0,1], "O animal tem dentes? ")
		backbone = self.possibleValues([0,1], "O animal tem espinha dorsal? ")
		breathes = self.possibleValues([0,1], "O animal possui respiração pulmonar? ")
		venomous = self.possibleValues([0,1], "O animal é venenoso? ")
		fins = self.possibleValues([0,1], "O animal tem barbatanas? ")
		legs = self.possibleValues([0,2,4,5,6,8], "Quantas pernas o animal tem? [0,2,4,5,6,8] ")
		tail = self.possibleValues([0,1], "O animal tem cauda? ")
		domestic = self.possibleValues([0,1], "O animal é domestico? ")
		catsize = self.possibleValues([0,1], "Catsize? ")
		return[hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize]

	def possibleValues(self, list, msg):
		value = 99999999999
		try:
			value = int(input(msg))
		except:
			print("Valor incorreto, digite um válido")
			return self.possibleValues(list, msg)
		if value in list:
			return value
		print("Valor incorreto, digite um válido")
		return self.possibleValues(list, msg)

