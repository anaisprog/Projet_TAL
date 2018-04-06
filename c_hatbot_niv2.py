
  class chatbot:

  def __init__(self):
    self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),gPats))
    self.values = list(map(lambda x:x[1],gPats))
  	#Traduction des expressions de l'utilisateur en expressions pour le chatbot: 

  traduction = {
    "suis"   : "es",
    "je"    : "tu",
    "je voudrais"  : "tu voudrais",
    "j'ai"  : "tu as",
    "je serais"  : "tu seras",
    "mon"  : "ton",
    "suis"  : "es",
    "tu as": "j'ai",
    "tu auras": "j'aurai",
    "ton"  : "mon",
    "le tien"  : "le mien",
    "toi"  : "moi",
    "moi"  : "toi"
  }



  #Réalisation d'une table de réponses:

  reponsesPossibles = [
  [r'Je suis (.*)',
  [  "Tu es venu parce que tu es %1?"]]
  ]


  def interface_chatbot():
    #phrase entree par l'utilisateur 
     	s=''
    	#chatbot = chatbot();

     	print('Hello how are you? ')
     	while (s!= 'quit'):
     	  try:
     		   s=input(' -->')

  if __name__ == "__main__":
  interface_chatbot()
