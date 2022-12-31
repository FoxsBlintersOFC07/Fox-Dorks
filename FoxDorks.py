#!/usr/bin/env/python3 know

from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time
import pyfiglet

# FOX DORK v1.0


if sys.version[0] in "2":
    print ("\n[x] ..n00b.. FOX DORK NAO É SUPORTADO Para Python 2.x Use Python 3.x \n")
    print ("\n\n\tFox Dorks \033[1;91mEu Estou te observando \033[0m👀\n\n")
    exit()


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

import os
os.system('clear')

from pyfiglet import Figlet
custom_fig = Figlet(font='cosmic')
print(custom_fig.renderText('F-Dorks'), 'green')
 
x = ("""
                Author:  FOX BLINTER
                Github:  https://github.com/FoxsBlintersOFC07
            Website:https://foxsblinters.simdif.com """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tSua mente é a sua maior arma, mas também sua maior fraqueza, controle seus pensamentos, ou eles irão controlar você ~~ Fox 2022\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\n[+] Você quer salvar o resultado em um arquivo?(Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] Interrupção detectada..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] Eu estou te observando  \033[0m👀\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] me dê o nome do arquivo: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Salvamento Pulado...")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input("\n[+] Digite sua Dork para consulta: ")
        amount = input("[+]  Insira a quantidade de sites a serem exibidos: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="pt", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] Interrupção Detectada..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] Eu estou te observando  \033[0m👀\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Saindo...")
    print ("\n\t\t\t\t\033[34mFoxDorks\033[0m")
    print ("\t\t\033[1;91m[!] Eu estou te observando \033[0m👀\n\n")
    sys.exit()


# =====# Menu #===== #
if __name__ == "__main__":
    dorks()
