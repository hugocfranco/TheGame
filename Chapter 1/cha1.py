import time
import random
from enum import Enum
import sys, traceback

class EstadosDeJogo(Enum):
   Jogando = 1
   GameOver = 2

class Jogo:
   def _init_(self, estado, personagem):
       self.estado = estado
       self.personagem = personagem

   def mostrarMensagem(self, mensagem, delay = True):
       print(mensagem)
       if (delay):
           time.sleep(2)

class Personagem:
   def _init_(self, id, nome, classe, habilidade):
       self.id = id
       self.nome = nome
       self.classe = classe
       self.habilidade = habilidade
       self.vida = 50

   def falar(self, mensagem):
       print(self.nome + " : " + mensagem)
       time.sleep(2)

jogo = Jogo(EstadosDeJogo.GameOver, None)

narrador = Personagem(7, "Narrador", "", "")

def escolherPersonagem():
   personagem = 0
   while personagem < 1 or personagem > 6:
       jogo.mostrarMensagem("Escolha um personagem:\n", False)
       jogo.mostrarMensagem("1 - Legolas", False)
       jogo.mostrarMensagem("2 - Vizir", False)
       jogo.mostrarMensagem("3 - Dibrador", False)
       jogo.mostrarMensagem("4 - Vlad", False)
       jogo.mostrarMensagem("5 - Krodz", False)
       jogo.mostrarMensagem("6 - Ionice\n", False)
       personagem = int(input())
       print("\n")
   if (personagem == 1):
       jogo.personagem = Personagem(1, "Legolas", "arqueiro", "atirar à distância")
   elif (personagem == 2):
       jogo.personagem = Personagem(2, "Vizir", "assassino", "esconder-se e matar alvos rapidamente")
   elif (personagem == 3):
       jogo.personagem = Personagem(3, "Dibrador", "negociante", "obter informações por meio de infiltração física")
   elif (personagem == 4):
       jogo.personagem = Personagem(4, "Vlad", "empalador", "grande força e dano em área em seu redor quando em estado de fúria")
   elif (personagem == 5):
       jogo.personagem = Personagem(5, "Krodz", "mago", "fazer feitiçoes e atacar com magias")
   else:
       jogo.personagem = Personagem(6, "Ionice", "padre", "cura e destreza com maça")
   jogo.mostrarMensagem("Seu personagem escolhido é: " + jogo.personagem.nome)
   print("\n")

escolherPersonagem()
narrador.falar("Seis mercenários estavam  tomando vinho em uma taverna. De repente, aparece uma pessoa e oferece uma missão misteriosa.")
aceiteDaMissao = input("Você aceita a missão?\n 1 = Sim, 2 = Não\n")

if (aceiteDaMissao == 1):
   jogo.mostrarMensagem("Voce recebeu uma Missão")
   jogo.mostrarMensagem("MISSÃO: Nomius deseja que os mercenários resgatem um animal sagrado chamado Viersan que foi sequestrado e removido de seu lugar de equilíbrio do reino de Saint Louis.")
else:
   jogo.estado = EstadosDeJogo.GameOver
   sys.exit(0)

narrador.falar("Seguindo para a cidade indicada ...")
narrador.falar("Cidade UNDB")
narrador.falar("Os mercenarios terão duas opções, procurar Viersan ou montar acampamento.")