##MENU DE ESCOLHA DAS DORKS
import time
import os
import platform
#"CRIANDO" AS CORES

VERMELHO   = "\033[1;31m"  
AZUL  = "\033[1;34m"
CIANO  = "\033[1;36m"
VERDE = "\033[0;32m"
INCOLOR = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def limpar(): #CRIA A FUNÇÃO PRA LIMPAR A TELA
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

#Tela de carregamento:

def atualizar():
      os.system("pip install --upgrade git+https://github.com/FoxsBlintersOFC07/Fox-Dork")
      atualizar()
limpar()
print(VERDE + "PROCURANDO ATUALIZAÇÕES.")
print(''' █▒▒▒▒▒▒▒▒▒ 10%''');time.sleep(2.0)
limpar()
print("PROCURANDO ATUALIZAÇÕES..")
print('''███▒▒▒▒▒▒▒ 30%''');time.sleep(1.0)
limpar()
print("PROCURANDO ATUALIZAÇÕES...")
print('''█████▒▒▒▒▒ 50%''');time.sleep(1.4)
limpar()
print("PROCURANDO ATUALIZAÇÕES.")
print('''███████▒▒▒ 70%''');time.sleep(1.3)
limpar()
print("PROCURANDO ATUALIZAÇÕES..")
print('''█████████▒ 90%''');time.sleep(1.2)
limpar()
print("PROCURANDO ATUALIZAÇÕES...")
print('''██████████ 100%''' + INCOLOR);time.sleep(1.2)
print(AZUL+ '''
・────━【   •   】━────・ 
   ___   _   ___ ___ ___ ___   _   __  __ ___ _  _ _____ ___      
  / __| /_\ | _ \ _ \ __/ __| /_\ |  \/  | __| \| |_   _/ _ \   
 | (__ / _ \|   /   / _| (_ |/ _ \| |\/| | _|| .` | | || (_) | 
  \___/_/ \_\_|_\_|_\___\___/_/ \_\_|  |_|___|_|\_| |_| \___/  
 
    ___ ___  _  _  ___ _   _   _ ___ ___   ___  
   / __/ _ \| \| |/ __| | | | | |_ _|   \ / _ \  
  | (_| (_) | .` | (__| |_| |_| || || |) | (_) | 
   \___\___/|_|\_|\___|____\___/|___|___/ \___/  
                                                                                                              
・────━【   •   】━────・
''' + INCOLOR);time.sleep(1.7)

limpar()

#BANNER 
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

print( CIANO + '''ESCOLHA SEU TIPO DE DORK:''' + INCOLOR)
print(''' 
        \033[1;34m [01] \033\033[;1m SQL
        \033[1;34m [02] \033\033[;1m XSS
        \033[1;34m [00] \033\033[;1m SAIR \033[0;0m
    ''')
pergunta=input( CIANO + 'DIGITE A OPÇÃO DESJEADA:' + VERMELHO) #PERGUNTA
if pergunta == "1":
        limpar()
        os.system("python dorks_sql.py")
elif pergunta == "01":
        limpar()
        os.system("python dorks_sql.py")
elif pergunta == "2":
        limpar()
        os.system("python dorks_xss.py")
elif pergunta == "02":
    limpar()
    os.system("python dorks_xss.py")
elif pergunta == "00":
        limpar()
        os.system("exit")
elif pergunta == "0":
        limpar()
        print(VERMELHO + "【BY FOX:】➤" + INCOLOR + "OBRIGADO POR USAR, VOLTE SEMPRE :)")
        os.system("exit")
else: 
        limpar()
        print(VERMELHO + "【BY FOX:】➤" + INCOLOR + "OPÇÃO INVALIDA [!]");time.sleep(0.6)
        limpar()
        os.system("python menu.py")