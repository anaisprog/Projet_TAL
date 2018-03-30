



VocabulaireBienvenue = ["Bonjour", "Bienvenue", "Salut", "Hello", "hello"]
VocabulaireAurevoir = ["Adieu", "Au revoir", "Aurevoir", "goodbye", "A bientot"]

#Sujets de discussions : 5 sujets autour de la famille, la meteo, les transports, les langues, les activités
VocabulaireFamille = ["enfants", "frère", "soeur", "frères", "soeurs", "mère" , "maman", "papa", "cousins", "cousines"]
VocabulaireMeteo = ["beau temps", "soleil", "pluie", "vent", "°C", "froid", "chaud"]
VocabulaireEmotions = ["heureux", "triste", "mélancolique", "euphorique", "furieux", "enervé", "méprisé", "trahit", "fier", "rassuré"]
VocabulaireLangues = ["anglais", "francais", "espagnol", "chinois", "mandarin", "allemand", "italien", "japon", "grec", "arabe"]
VocabulaireActivites = ["parc", "parc d'attraction", "piscine", "mer", "ski", "surf", "plongée", "saut en parachute"]

while(1):
	n = (input())
	
	for i in VocabulaireFamille:   
		if i in n:
			print("Ca doit etre agréable d'avoir une famille..! ")

	for i in VocabulaireAurevoir:   
		if i in n:
			print("Oh! On se quitte déja? ")
		else: 
			print("Je ne te comprends pas... Tu pourrais reformuler s'il te plait?")  
		
	for i in VocabulaireBienvenue:   
		if i in n:
			print("Bonjour nouvel utilisateur ! Je suis heureux de te renconrer!")
	
