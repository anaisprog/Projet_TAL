
from os import path
 
# ouverture du fichier texte 
listPays_path = 'Pays/liste_pays.txt'
LISTE_PAYS = []
with open(path.join(path.dirname(__file__), listPays_path)) as file_pointer:
		for lines in file_pointer.readlines():
			line = lines.split(" | ")
			LISTE_PAYS.append(line)

LISTE_MOIS = ["Janvier" , "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre","Decembre"]
mois = ""
pays = ""
plusInfo = False

#30 AVRIL 2018  : Cette partie de programme permet de retrouver des destinations interessantes selon le mois donnee en entree
#Cette fonction nous permet de verifier que le pays de départ et le mois de depart ont bien ete saisis par l'utilisateur

def info_manquantes(data):
  global count
  global pays
  global mois
  count = 2 # Par defaut toutes les informations sont manquantes
  if pays=="" or mois =="":
  	count =1 #1 info manquante
  	print(count)

  elif pays !="" and mois !="":
  	print("la valeur de pays est"+ pays + "mois " + mois)
  	count =0 #pas d'info manquante

  return count


def reponse2(data):
	print(info_manquantes(data))
	if(info_manquantes(data)!=0):
		print("Oups....\n" +"J'ai besoin des informations suivantes pour vous donner une destination \n : "
		+ " Votre pays de depart et votre mois de départ... \n ")
		if((data["pays_depart"]== None) and (data["mois_depart"]== None)):
			print("Il semblerait que vous n'ayez renseigné aucun des deux champs...")
		elif(data["pays_depart"]== None):
			print("Il semblerait que vous n'ayez par renseigné votre pays de départ...")
		elif(data["mois_depart"]== None):
			print("Il semblerait que vous n'ayez par renseigné votre mois de départ...")
	elif(info_manquantes(data) == 0): 
		print("Tous les champs ont ete saisis. Recherche en cours...")
		rechercheDestination(data)

# Cette fonction permet de reconnaitre le pays et le mois de depart saisi 
def reponse(data):
	global pays
	global mois
	mot = data.split(" ") 
	for i in range (0, len(mot)):
		for pays_ in LISTE_PAYS:
			for country in pays_:
				if(country.lower() in mot[i] or country.upper() in mot[i]): 
					pays = mot[i]	
		for mois_ in LISTE_MOIS:
			if(mois_.lower() in mot[i] or mois_.upper() in mot[i]):
				#print("Le mois est "+ mot[i] + mois)
				mois = mot[i]
				

	print(info_manquantes(data))
	if(info_manquantes(data)!=0):
		print("Oups....\n" +"J'ai besoin des informations suivantes pour vous donner une destination \n : "
		+ " Votre pays de depart et votre mois de départ... \n ")
		if(pays =="") and (mois==""):
			print("Il semblerait que vous n'ayez renseigné aucun des deux champs...")
		elif(pays ==""):
			print("Il semblerait que vous n'ayez par renseigné votre pays de départ...")
		elif(mois== ""):
			print("Il semblerait que vous n'ayez par renseigné votre mois de départ...")
	elif(info_manquantes(data) == 0): 
		print("Tous les champs ont ete saisis. Recherche en cours...")
		rechercheDestination(data)

def rechercheDestination(data):
	global mois
	global pays
	count_loc =0
	with open(path.join(path.dirname(__file__), "../data/baseDonnees.txt")) as file_pointer:
		for lines in file_pointer.readlines():
			line = lines.split("|")
			for word in line[2:]:
				if(count ==0):	
					if(mois in word.lower() or mois is word.upper()): 
						if(line[0].lower()!= pays): # on verifie qu'il ne sagit pas du pays d'origine de l'utilisateur
							if(count_loc ==1):
								print("D'autres destinations peuvent egalement satisfaire votre recherche.")
								count_loc+=1
							if(count_loc ==2):
								x = input('Pour plus de destinations disponibles taper I \n')
								if(x=='I' or x=='i'): 
									plusInfo = True 
									count_loc+=1
							if ((count_loc >2) and (plusInfo==True)): 
								print(line[0].lower() + "avec une temperature moyenne de" + line[1].lower())
				
							if(count_loc==0): 
								print("\n \n*************************Recherche en cours*********************\n"
								+"Nous vous avons trouve une destination  : "  + line[0].lower() +"avec une temperature moyenne de" + line[1].lower() 
								+ "pendant le mois de votre sejour ")
								count_loc +=1
			
        #if((mois in word for word in line[1:])==0):
			#print("Nous vous avons trouve une destination : "  + line[0].lower())            
