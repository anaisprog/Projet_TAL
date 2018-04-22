import random

# define the function blocks
def reponse1():
    return "ChatBot : uh huh.\n"

def reponse2():
    return "ChatBot : Hum....\n"

def reponse3():
    return "ChatBot : Continuez\n"

def reponse4():
    return "ChatBot : Oui...\n"

def mode1():

	rep = raw_input("ChatBot : I am ready to talk with you: \n")
	while(1):
		nombre = random.randint(0,3)

		if(nombre == 0):
			rep = raw_input(reponse1())
		if(nombre == 1):
			rep = raw_input(reponse2())
		else:
			rep = raw_input(reponse3())

test = mode1()

