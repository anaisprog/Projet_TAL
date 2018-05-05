import re
import random
import string 



GREETING_KEYWORDS = ["hello", "hi", "Coucou", "salut", "hola", "wesh", "ca va ?", "bonjour"]
GREETING_RESPONSES = ["Hola l'humain!", "yooo", "*Atchoum*...salut ! ", " Bonjour Bonjour ! ", "Comment ca va aujourd'hui?"]

#Sujet de discussion - 5 sujets, 10 mots clé, 2 réponses

FAMILY_KEYWORDS = ["maman", "papa", "mere", "pere", "soeur", "frere", "famille", "oncle", "tante", "héritage", "cousins"]
FAMILY_RESPONSES = ["Penses-tu que la famille c'est important ?", "La famille c'est une richesse incroyable, ça donne des outils pour pouvoir affronter les moments extraordinaires, les moments plus difficiles, les hauts, les bas."]

LOVE_KEYWORDS = ["amour", "amoureuse", "trahison", "aimer", "mari", "femme", "mariage", "sentiment", "engagement", "fiancailles", "couple", "amoureux"]
LOVE_RESPONSES = ["L'amour est une catastrophe magnifique : savoir que l'on fonce dans un mur, et accélérer quand même.", "Chaque personne qu'on s'autorise à aimer, est quelqu'un qu'on prend le risque de perdre"]

HEALTH_KEYWORDS = ["sante", "malade", "cancer", "mort", "vivant", "hopital", "docteur", "maladie", "fatigue", "medicament"]
HEALTH_RESPONSES = ["Je pense que la santé est la plus grande des richesses", "La gaieté est la moitié de la santé."]

WORK_KEYWORDS = ["travail", "collegue", "promotion", "patron", "boss", "licencié", "entretien", "salaire", "congé"]
WORK_RESPONSES = ["Tu préfererais avoir des vacances de 6 mois 2 fois par an ?", "Oulala me parle pas boulot je suis en vacances !!!"]

TRAVEL_KEYWORDS = ["voyage", "avion", "plage", "mer", "soleil", "valise", "hotel", "aeroport", "jetlag", "vacances"]
TRAVEL_RESPONSES = ["Oh j'aimerais tellement allée aux Phillipines, t'y es allé toi ?", "J'adore les vacances, on devrait en avoir plus souvent tu ne penses pas ?"]

OTHER_RESPONSES = ["Je préférerais changer de sujet", "Tu veux pas me parler d'autre chose ?", "Et sinon tu fais quoi dans la vie ?", "Tu peux m'en dire plus ?", "Je vois", "Très intéressant", "Et sinon t'aimerais que je te raconte une histoire ?", "Désolé mais ... je m'ennuie un peu là", "Ohhhh je viens de me souvenir que j'ai oublié de sortir mon dogbot"]

# Le chatbot doit etre capable de reconnaitre ces differents mots-clés: 

mots_cles = {}


mots_cles["Salutations"] = ["bonjour", "hello", "hola", "salut", "coucou",
    "hey", "yo"]

mots_cles["Aurevoir"] = ["aurevoir", "au revoir", "quit", "bye", "exit", "a bientot", "ciao", "adieu"]

mots_cles["Oui"] = ["oui", "bien sur", "d'accord", "yes", "absolument"]

mots_cles["Remerciements"] = ["merci", "merci beaucoup"]

mots_cles["Non"] = ["non", "no", "jamais", "pas possible"]



class chatbot:

# Sentences we'll respond with if the user greeted us

  def __init__(self):
    self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),reponsesPossibles))
    self.values = list(map(lambda x:x[1],reponsesPossibles))


  def respond(self,str):
    # find a match among keys
    repFound = 0;
    for i in range(0, len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        resp = random.choice(self.values[i])
        pos = resp.find('%')
        repFound = 1
        if pos == -1:
          print(resp[:pos] + "?")
        else:
          print(resp[:pos] + match.group(1) + "?")
 

    for word in GREETING_KEYWORDS:
      if word in str:
        print(random.choice(GREETING_RESPONSES))
        repFound = 1
    for word in LOVE_KEYWORDS:
      if word in str and repFound ==0:
        print(random.choice(LOVE_RESPONSES))
        repFound = 1
    for word in WORK_KEYWORDS:
      if word in str and repFound ==0:
        print(random.choice(WORK_RESPONSES))
        repFound = 1
    for word in FAMILY_KEYWORDS:
      if word in str and repFound ==0:
        print(random.choice(FAMILY_RESPONSES))
        repFound = 1
    for word in HEALTH_KEYWORDS:
      if word in str and repFound ==0:
        print(random.choice(HEALTH_RESPONSES))
        repFound = 1
    for word in TRAVEL_KEYWORDS:
      if word in str and repFound ==0:
        print(random.choice(TRAVEL_RESPONSES))
        repFound = 1


    if repFound == 0:
     print(random.choice(OTHER_RESPONSES))


  #Realisation d'une table de reponses:
reponsesPossibles= [
    [r'Je suis (.*)',  
      [ "Interessant. Donc tu me dis que tu es % ", 
        "Oh Vraiment! tu es % "]],

    [r'Je vais (.*)', 
      [ "Ok... Donc si je comprends bien, tu vas %", 
        "Oh! Tu vas %"]],

    [r'Je mange (.*)', 
      [ "Pourquoi aimes tu manger %", 
        "C'est intéressant, donc tu manges %"]],

    [r'Je serai (.*)', 
      ["Oh! Tu seras %", "C'est intéressant, donc tu seras %"]],

    [r'J\'étais (.*)', 
      [ "Pourquoi étais-tu %", 
        "C'est intéressant, donc tu étais %"]],

    [r'Tu vas (.*)', 
      [ "Interessant. Tu me dis que je vais %", 
        "Ah bon? Je vais %"]],

    [r'Tu es (.*)',
      [ "Vraiment! Je suis %", 
        "J'entends bien... Donc pour toi je suis %",
        "Tu préférerais que je ne sois pas %,"]],

    [r'Tu seras (.*)', 
      [ "Je serais %", 
        "C'est intéressant, tu me dis que je serai %"]],

    [r'J\'ai (.*)', 
      [ "Pourquoi as-tu %", 
        "Tu penses que moi aussi j'ai %"]],

    [r'J\'ai besoin (.*)', 
      [ "Pourquoi as-tu besoin %", 
        "Penses-tu vraiment avoir besoin %"]],

    [r'Pourquoi je ne peux pas (.*)', 
      [ "Que ferriez vous si vous pourriez %", 
        "Pourquoi tu penses que tu ne peux pas %"]],

    [r'Parce que (.*)', 
      [ "Est-ce vraiment la bonne raison", 
        "Quelle autre raison as-tu en tête ? "]],

    [r'Je pense (.*)', 
      [ "Tu doutes %", 
        "Donc tu n'es pas sur %"]],

    [r'Je pense à(.*)', 
      [ "Pouquoi penses-tu à %"]],

    [r'Je me sens (.*)', 
      [ "Pouquoi te sens-tu %"
        "Tu te sens souvent %"]],

    [r'Je veux (.*)', 
      [ "Pouquoi tu veux %"
        "Qu'est ce que tu ferais si tu avais %"]],


]


  

if __name__ == "__main__":
  #interface_chatbot()def interface_chatbot():
    #phrase entree par l'utilisateur 
  print('Coucou petit humain... Je suis un chatbot qui a été concu rien que pour discuter avec toi!  \n" ----Si tu veux me quitter, entre exit !')
  s = ''
  chatbot = chatbot()
  while s != 'exit':
    try:
      s = input('> ')
    except EOFError:
      s = 'exit'  
    #print(s)
    #while s[-1] in '!.':
     # s = s[:-1]
    chatbot.respond(s)
  

