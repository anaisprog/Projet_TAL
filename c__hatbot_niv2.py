import re
import random
import string 



GREETING_KEYWORDS = ["hello", "hi", "coucou", "salut", "hola"]
GREETING_RESPONSES = ["Hola l'humain!", "yooo", "*Atchoum*...salut ! ", " Bonjour Bonjour ! "]

# Le chatbot doit etre capable de reconnaitre ces differents mots-clés: 

mots_cles = {}


mots_cles["Salutations"] = ["bonjour", "hello", "salut", "coucou",
    "hey", "yo"]

mots_cles["Aurevoir"] = ["aurevoir", "au revoir", "quit", "bye", "exit", "a bientot"]

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
    for i in range(0, len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        resp = random.choice(self.values[i])
        pos = resp.find('%')
        print(resp[:pos] +match.group(1) + '?')

    for word in GREETING_KEYWORDS:
      if word in str:
            print(random.choice(GREETING_RESPONSES))


  #Realisation d'une table de reponses:
reponsesPossibles= [[r'Je suis (.*)',  [ "Interessant. Donc tu me dis que tu es %", 
 "Oh Vraiment! tu es %"]],
[r'Je vais (.*)', ["Ok... Donc si je comprends bien, tu vas %", "Oh! Tu vas %"]],
[r'Je mange (.*)', ["Pourquoi aimes tu manger %", "C'est intéressant, donc tu manges %"]],
[r'Je serai (.*)', ["Oh! Tu seras %", "C'est intéressant, donc tu seras %"]],
[r"J\'étais (.*)", ["Pourquoi étais-tu %", "C'est intéressant, donc tu étais %"]],
[r'Tu vas (.*)', ["Interessant. Tu me dis que je vais %", "Ah bon? Je vais %"]],
[r'Tu es (.*)', ["Vraiment! Je suis %", "J'entends bien... Donc pour toi je suis %"]],
[r'Tu seras (.*)', ["Je serais %", "C'est intéressant, tu me dis que je serai %"]]
]


  

if __name__ == "__main__":
  #interface_chatbot()def interface_chatbot():
    #phrase entree par l'utilisateur 
  print('Coucou petit humain... Je suis un chatbot qui a été concu rien que pour discuter avec toi!  \n" ----Press exit to stop the chatbot')
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
  

