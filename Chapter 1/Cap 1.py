import time
import random
from enum import Enum


class EstadosDeJogo(Enum):
    Jogando = 1
    GameOver = 2


class Jogo:
    def __init__(self, estado):
        self.estado = estado

    def mostrarMensagem(self, mensagem, delay=True):
        print(mensagem)
        if (delay):
            time.sleep(2)


jogo = Jogo(EstadosDeJogo.Jogando)


class Personagem:
    def __init__(self, id, nome, classe, habilidade, dinheiro = 0):
        self.id = id
        self.nome = nome
        self.classe = classe
        self.habilidade = habilidade
        self.vida = 50
        self.dinheiro = 0

    def falar(self, mensagem):
        print(self.nome + " : " + mensagem)
        time.sleep(2)


pLegodas = Personagem(1, "Legolas", "arqueiro", "atirar à distância")
pVizir = Personagem(2, "Vizir", "assassino", "esconder-se e matar alvos rapidamente")
pDibrador = Personagem(3, "Dibrador", "negociante", "obter informações por meio de infiltração física")
pVlad = Personagem(4, "Vlad", "empalador", "grande força e dano em área em seu redor quando em estado de fúria")
pKrodz = Personagem(5, "Krodz", "mago", "fazer feitiçoes e atacar com magias")
pIonice = Personagem(6, "Ionice", "padre", "cura e destreza com maça")
pNarrador = Personagem(7, "Narrador", "", "")

pSaqueadores = Personagem(8, "Saqueadores", "Inimigo", "")
pCombradoresDeImpostos = Personagem(9, "Cobradores de Impostos", "Inimigo", "")
pSoldadosDoPartao = Personagem(10, "Soldados do Portão", "Inimigo", "")


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


def ataque():
    return random.randint(0, 10)

def barganhar():
    return random.randint(0, 20)

def steath():
    return random.randint(0, 20)


jogo.mostrarMensagem("Seis mercenários estavam tomando vinho em uma taverna.\n"
                     "De repente, aparece uma pessoa e oferece uma missão misteriosa.")

# for x in personagens:
#     print(x)
#     for y in personagens[x]:
#         print(y, ':', personagens[x][y])


# personagemEscolhido = input()

resposta1 = input("Você aceita a missão?\n"
                  "1 = Sim\n"
                  "2 = Não\n")

if (resposta1 == "1"):
    jogo.mostrarMensagem(
                         'Voce recebeu uma Missão\n'
                         "MISSÃO: Nomius deseja que os mercenários resgatem um animal sagrado chamado Viersan\n"
                         "que foi sequestrado e removido de seu lugar de equilíbrio do reino de Saint Louis.\n"
                         "A missão vale 10 bitcoins")
else:
    jogo.mostrarMensagem("Game Over!")

jogo.mostrarMensagem("Seguindo para a cidade NUDB")

resposta2 = input("Os mercenarios terão duas opções:\n"
                  "1 - Caminhar na estrada para a cidade a noite. (Menor change de ser atacado)\n"
                  "2 - Montar acampamento um acampamneto. (Maior change de ser atacado. Pequena change de recuperar vida)\n")

if (resposta2 == '1'):
    jogo.mostrarMensagem("Indo para a cidade...")
    ataque = ataque()
    if (ataque <= 2):
        jogo.mostrarMensagem("Você foi atacado por cobradores de impostos!")
        personagem.vida -= random.randint(0, 75)
    else:
        jogo.personagem.dinheiro += 100

elif (resposta2 == '2'):
    jogo.mostrarMensagem("Montando acampamento...")
    ataque = ataque()
    if (ataque <= 7):
        jogo.mostrarMensagem("Você foi atacado por saqueadores!")
        vida -= random.randint(0, 75)
    else:
        jogo.mostrarMensagem("Eles dormiram com os anjos")
        vida += 100
        jogo.personagem.dinheiro += 100

print("sua vida:", jogo.personagem.vida)

if (jogo.personagem.vida < 0):
    jogo.mostrarMensagem("Game Over")

jogo.mostrarMensagem("Os mercenários chegaram na portão da cidade")
jogo.mostrarMensagem("Eles não tinham como pagar o pedágio cobrado pelos guardas do portão. Você terá três opções: \n")
               

resposta3 = int(input("1 - Convencer os guardas a entrar em pagar. (Média change de ser atacado)\n"
               "2 - Contornar os muros e entrar escondido na cidade. (Maior change de ser atacado)\n"
               "3 - Subornar os guardas\n"))

if (resposta3 == 1):
    barganha = barganhar()
    if barganha >= 10:
        jogo.mostrarMensagem("Você conseguiu convencer os guardas")
    else:
        jogo.mostrarMensagem("Os guardas ficaram putos e eles os atacaram")
        ataque = ataque()
        if (ataque < 7):
            jogo.mostrarMensagem("Você levou um dedada!")
            jogo.personagem.vida -= random.randint(0, 75)
        else:
            jogo.mostrarMensagem("Eles eram fracos! HA HA HA!")
            jogo.personagem.dinheiro += 100

if (resposta3 == 2):
    steath = steath()
    if steath => 10:
       jogo.mostrarMensagem("Você conseguiu dibrar os guardas") 
    else:
        ataque = ataque()
        jogo.mostrarMensagem("Você foi avistado pelos guardas!")
        if (ataque <= 8):
            jogo.mostrarMensagem("Você foi atacado por saqueadores!")
            vida -= random.randint(0, 75)
        else:
            jogo.mostrarMensagem("Eles dormiram com os anjos")
            vida += 100
            jogo.personagem.dinheiro += 100








