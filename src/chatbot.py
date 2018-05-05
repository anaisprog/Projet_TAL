

import argparse
from mode3_reponse import reponse

def main():
  mauricius_bot()

def mauricius_bot():
  
  print("Bonjour, je m'appelle Mauricius, je suis un chatbot\n" 
  	  +"qui peut vous trouver votre meilleure destination dans le monde \n" 
  	  + "Est ce que vous pourriez s'il vous plait me raconter.... \n"
      +"Dans quel pays vivez vous? Quel mois avait vous choisi pour partir en vacances? "
  	  )

  prog = True
  while(prog):
    userInput = input(" >")
    print(reponse(userInput))


if __name__ == "__main__":
  main() 
