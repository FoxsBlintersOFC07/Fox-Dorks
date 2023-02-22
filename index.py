# NÃO EDITE, REMOVA, EXCLUA, COLE, OU FAÇA QUAISQUER ALTERAÇÃO NESSE SCRIPT SEM A PERMISSÃO DE UM MEBRO OFICIAL DA "FOXS BLINTERS"

from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time
import pyfiglet

VERMELHO   = "\033[1;31m"  
AZUL  = "\033[1;34m"
CIANO  = "\033[1;36m"
VERDE = "\033[0;32m"
INCOLOR = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

# FOX DORK v2.0


if sys.version[0] in "2":
    print ("\n[x] ..f0x.. FOX DORK NAO É SUPORTADO Para Python 2.x Use Python 3.x \n")
    print ("\n\n\tFox Waynne \033[1;91mEu sou o Mestre dos Magos \033[0m🧙‍♂️\n\n")
    exit()


class cores:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

#banner 
print(VERMELHO + '''

███████╗░░░░░░██████╗░░█████╗░██████╗░██╗░░██╗░██████╗
██╔════╝░░░░░░██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝
█████╗░░█████╗██║░░██║██║░░██║██████╔╝█████═╝░╚█████╗░
██╔══╝░░╚════╝██║░░██║██║░░██║██╔══██╗██╔═██╗░░╚═══██╗
██║░░░░░░░░░░░██████╔╝╚█████╔╝██║░░██║██║░╚██╗██████╔╝
╚═╝░░░░░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
                █░█ ▀█░   █▀█
                ▀▄▀ █▄▄ ▄ █▄█
''' + INCOLOR); time.sleep(1.5)
print(VERDE + '''
╔╦══• •✠•❀•✠ • •══╦╗''' + INCOLOR )
print(VERMELHO + "AUTOR:" + AZUL + "Fox Waynne");time.sleep(0.8)
print(VERMELHO + "SITE:" + AZUL + "www.foxsblinters.simdif.com");time.sleep(0.8)
print(VERMELHO + "CANAL:" + AZUL + "www.youtube.com/@foxsblinters");time.sleep(0.8)
print(VERMELHO + "GITHUB:" + AZUL + "github.com/FoxsBlintersOFC07" + INCOLOR)
print( VERDE + '''
╚╩══• •✠•❀•✠ • •══╩╝'''+ INCOLOR)

y = "\n\t\tSua mente é a sua maior arma, mas também sua maior fraqueza, controle seus pensamentos, ou eles irão controlar você ~~ Fox 2022\n"
for col in y:
    print(cores.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(cores.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input(VERMELHO + "【BY FOX:】➤ " + INCOLOR + "VOCÊ DESEJA SALVAR O RESULTADO EM UM ARQUIVO DE TEXTO?").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print (VERMELHO + "【BY FOX:】➤ " + INCOLOR + "VOCÊ FECHOU O SCRIPT FORÇADAMENTE, SAINDO....")
        time.sleep(0.5)
        print ("\n\n\tFox Waynne \033[1;91mEu sou o Mestre dos Magos \033[0m🧙‍♂️\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input(VERMELHO + "【BY FOX:】➤ " + INCOLOR + "DIGITE O NOME DO arquivo.txt")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print (VERMELHO + "【BY FOX:】➤ " + INCOLOR + "SALVAMENTO PULADO")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input(VERMELHO + "【BY FOX:】➤ " + INCOLOR + "Cole a DORK que vc copiou, ou digite uma " + AZUL + "⤷ ")
        amount = input(INCOLOR + VERMELHO + "【BY FOX:】➤ " + INCOLOR + "Digite a quantidade de sites a serem exibidos " + AZUL + "⤷ ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="pt", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("▶ ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print (VERMELHO + "【BY FOX:】➤ " + INCOLOR + "VOCÊ FECHOU O SCRIPT FORÇADAMENTE, SAINDO....")
            time.sleep(0.5)
            print ("\n\n\tFox Waynne \033[1;91mEu sou o Mestre dos Magos \033[0m🧙‍♂️\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print (VERMELHO + "【BY FOX:】➤ " + AZUL + "TERMINEI, FECHANDO POGRAMA..." + INCOLOR)
    print ("\n\t\t\t\t\033[34mFoxDorks\033[0m")
    print ("\n\n\tFox Waynne \033[1;91mEu sou o Mestre dos Magos \033[0m🧙‍♂️\n\n")
    sys.exit()


# =====# Menu #===== #
if __name__ == "__main__":
    dorks()