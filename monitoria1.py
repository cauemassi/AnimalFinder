#Monitoria que valida se os animais mamiferos estão certos

from lib import db

data_base = db.db()

consulta = data_base.executeQuery("select name, type from animais where milk = 1")

def vefiricaMamiferos(consulta):
	mensagem = ""
	num = 0
	for animal in consulta:
		if(animal[1] != 1):
			mensagem += "O animal " + animal[0] + " não é mamifero. "
			num = 2
	return mensagem, num
	
msg, num = vefiricaMamiferos(consulta)

if (num == 0):
	mensagem = "OK - Os dados dos mamíferos estão corretos"
else:
	mensagem = "CRITICAL - " + msg
	
print(mensagem)
