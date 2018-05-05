import random

# Les differents Backchannels
def reponse1():
    return "ChatBot : uh huh."

def reponse2():
    return "ChatBot : Hum...."

def reponse3():
    return "ChatBot : Continuez"

def reponse4():
    return "ChatBot : Oui..."

def reponse5():
    return "ChatBot : Intéressant"

def reponse6():
    return "ChatBot : Oh ! Je vois"

def mode1():

	print('Coucou petit humain... Je suis un chatbot qui a été concu rien que pour discuter avec toi!' )
	lastRep = -1
	
	while(1):
		rep = input('> ')
		nombre = random.randint(0,3)

		#Pour empecher deux repetitions consecutives de la meme replique
		if nombre == lastRep:
			while nombre == lastRep:
				nombre = random.randint(0,3)

		if nombre == 0:
			print(reponse1())
		if(nombre == 1):
			print(reponse2())
		else:
			print(reponse3())

		lastRep = nombre
	

test = mode1()
