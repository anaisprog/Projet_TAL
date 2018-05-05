import random

#Reponses possibles
def reponse1():
    return "ChatBot : uh huh."

def reponse2():
    return "ChatBot : Hum...."

def reponse3():
    return "ChatBot : Continuez"

def reponse4():
    return "ChatBot : Oui..."

def reponse5():
    return "ChatBot : Interessant.."

def reponse6():
    return "ChatBot : Oh ! Je vois..."

def mode1():

	print('Coucou petit humain... Je suis un chatbot qui a été concu rien que pour discuter avec toi!')
	
	repfind = False
	lastRep = -1
	
	while(1):
		rep = input()
		nombre = random.randint(0,7)

		if nombre == lastRep:
			nombre = random.randint(0,7)

		if(nombre == 0) and repfind == False:
			print(reponse1())
			repfind = True
		if(nombre == 1) and repfind == False:
			print(reponse2())
			repfind = True
		if(nombre == 2) and repfind == False:
			print(reponse3())
			repfind = True
		if(nombre == 3) and repfind == False:
			print(reponse4())
			repfind = True
		else:
			print(reponse5())
			repfind = True

		lastRep = nombre

test = mode1()

#Faire en sorte d'avoir des réponses différentes

