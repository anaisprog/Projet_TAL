

# Ce fichier contient des fonctions que nous n'avons pas pu faire marcher et abandonnées dans la suite du projet.
# Inspirées du TP spam/ham nous voulions que le chatbot puisse orienter ses reponses en fonction de celles de l'utilisateur
import re

LISTE_PAYS = ["France", "Angleterre", "Espagne", "Italie", "Chine", "Russie"]
LISTE_MOIS = ["Janvier" , "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre","Decembre"]

#Mots clés que le chatbot doit etre capable de reconnaitre 
keywords = {}

keywords["Salutations"] = ["hi", "bonjour", "salut"]

keywords["Voyage"] = ["voyage", "avion", "plage", "mer", "soleil", "valise", "hotel", "aeroport", "jetlag", "vacances"]

keywords["Aurevoir"] = ["aurevoir" "bye"]

keywords["Oui"] = ["oui", "bien sur", "yes", "sure"]

keywords["Merci"] = ["merci", "thanks", "thank you"]

keywords["Non"] = ["non", "no"]

keywords["Pays"] = ["France", "Angleterre", "Espagne", "Italie", "Chine", "Russie"] # A completer...

keywords["Mois"] = ["Janvier" , "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre","Decembre"]




def choisir_reponse(message_utilisateur, data):
  # la fonction permet de reconnaitre certains mot avec leurs "familles" définis ci dessus 
  for cle, valeurs in keywords.items():
    for valeur in valeurs:
      message_utilisateur = re.sub(r"\b" + valeur + r"\b", cle, message_utilisateur)

  oddsOffset = {}

  for cle, valeur in data.items():
      if valeur != None:
        oddsOffset[cle] = 0
      else:
        oddsOffset[cle] = 1

  words = message_utilisateur.split(" ")
  
  traitement_txt = {}
  for mot_cle in keywords:
      for word in words:
        if word == mot_cle:
          traitement_txt[mot_cle] = traitement_txt.get(mot_cle, 0) + 1

  # Odds and position of values
  odds = []
  intern_data = []
  s = ""
  for pays in LISTE_PAYS:
    for i in range(0, len(words)):    
      intern_data.append(i)
      odds.append(calculateOdds(words, i, oddsOffset))

    for index in range(0, len(intern_data)):
      valeur = words[intern_data[index]]
      max_ = 0

    for cle, valeur in traitement_txt.items():
     # Differents cas a traiter

      if valeur > max_:
        max_ = value
        highestKey = cle

      

def calcule(words, n, example):
  odds = {}
  result = dict.fromkeys(example, 0)

  oddsMult = 1

  for i in range(n, 0, -1):
    if words[i] == "Pays":
      odds["pays_depart"] = 1
      oddsMult *= infDecrease
    if words[i] == "Mois":
      odds["mois_depart"] = 1
      oddsMult *= infDecrease

    for cle, valeur in odds.items():
      result[cle] += valeur * oddsMult

  return result

