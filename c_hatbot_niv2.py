import re

class chatbot:

  def __init__(self):
    self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),reponsesPossibles))
    self.values = list(map(lambda x:x[1],reponsesPossibles))
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

  def respond(self,str):
    # find a match among keys
    for i in range(0, len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        resp = random.choice(self.values[i])
        # we've got a response... stuff in reflected text where indicated
        pos = resp.find('%')
        while pos > -1:
          num = int(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num),traduction) + \
            resp[pos+2:]
          pos = resp.find('%')
        # fix munged punctuation at the end
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        return resp

  def translate(self,str,dict):
    words = str.lower().split()
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
    return ' '.join(words)


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
reponsesPossibles= [r'Je suis (.*)',  [ "Tu es venu parce que tu es %1?"]],
[r'Je vais (.*)', ["Tu vas %1"]],
[r'Je mange (.*)', ["Pourquoi aimes tu manger %1 ?"]]

def interface_chat():
  print('Hello.  How are you ?')

  s = ''
  chatbot = chatbot();
  while s != 'quit':
    try:
      s = input('> ')
    except EOFError:
      s = 'quit'
    print(s)
    while s[-1] in '!.':
      s = s[:-1]
    print(chatbot.respond(s))
  

if __name__ == "__main__":
  #interface_chatbot()def interface_chatbot():
    #phrase entree par l'utilisateur 
  print('Hello.  How are you ?')
  s = ''
  chatbot = chatbot()
  while s != 'quit':
    try:
      s = input('> ')
    except EOFError:
      s = 'quit'
    print(s)
    while s[-1] in '!.':
      s = s[:-1]
    print(chatbot.respond(s))
  
