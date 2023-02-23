import os
import platform
import time
import pyfiglet

#CORES (
VERMELHO = "\033[1;31m"  
AZUL  = "\033[1;34m"
CIANO  = "\033[1;36m"
VERDE = "\033[0;32m"
INCOLOR = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
# )

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
######

def banner():   
 import pyfiglet 
 result = pyfiglet.figlet_format("COPIE UMA DORK ABAIXO ", font = "slant") 
 print(result) 
banner()
#Pergunta

def Lista():
   print('''
\033[1;34m『1』➥\033[0;0m inurl:".php?cmd="
\033[1;34m『3』➥\033[0;0m inurl:".php?z="
\033[1;34m『4』➥ \033[0;0m inurl:".php?q="
\033[1;34m『5』➥ \033[0;0m inurl:".php?search="
\033[1;34m『6』➥ \033[0;0m inurl:".php?query="
\033[1;34m『7』➥ \033[0;0m inurl:".php?searchst­ring="
\033[1;34m『8』➥ \033[0;0m inurl:".php?keyword=­"
\033[1;34m『9』➥ \033[0;0m inurl:".php?file="
\033[1;34m『10』➥ \033[0;0m inurl:".php?years="
\033[1;34m『11』➥ \033[0;0m inurl:".php?txt="
\033[1;34m『12』➥ \033[0;0m inurl:".php?tag="inurl:".php?max="
\033[1;34m『13』➥ \033[0;0m inurl:".php?from="
\033[1;34m『14』➥ \033[0;0m inurl:".php?author="
\033[1;34m『15』➥ \033[0;0m inurl:".php?pass="
\033[1;34m『16』➥ \033[0;0m inurl:".php?feedback­="
\033[1;34m『17』➥ \033[0;0m inurl:".php?mail="
\033[1;34m『18』➥ \033[0;0m inurl:".php?cat="
\033[1;34m『19』➥ \033[0;0m inurl:".php?vote="
\033[1;34m『20』➥ \033[0;0m inurl:search.php?q=
\033[1;34m『21』➥ \033[0;0m inurl:com_feedpostol­d/feedpost.php?url=
\033[1;34m『22』➥ \033[0;0m inurl:scrapbook.php?­id=
\033[1;34m『23』➥ \033[0;0m inurl:headersearch.p­hp?sid=
\033[1;34m『24』➥ \033[0;0m inurl:/poll/­default.asp?catid=
\033[1;34m『25』➥ \033[0;0m inurl:/­search_results.php?se­arch=
                 \033[1;31m (ESPECIAL)
\033[1;34m『26』➥ \033[1;31m inurl:categoryId inurl:storeId
\033[1;34m『27』➥ \033[1;31m inurl:”webapp/wcs”
\033[1;34m『28』➥ \033[1;31m inurl:”ProductListingView”
\033[1;34m『29』➥ \033[1;31m inurl:”AdvancedSearchDisplay”
\033[1;34m『30』➥ \033[1;31m inurl:”CompareProductsDisplayView”
\033[1;34m『31』➥ \033[1;31m inurl:parent_category_rn

''')
Lista()

#Autorizar para iniciar o menu de dork

autorizacao = input(VERDE + "APÓS COPIAR SUA DORK, DIIGTE: " + VERMELHO + '"Y"' + INCOLOR + " PARA PROSSEGUIR: \033[0;32m ")

if autorizacao == "Y" or "y":
   clear()
   os.system("python index.py")
elif autorizacao == "N" or "n":
   print("「!」➤ Comando Inválido");time.sleep(0.7)
   os.system("python dorks.sql.py")
elif autorizacao:
   print("「!」➤ Comando Inválido");time.sleep(0.7)
   os.system("python dorks.sql.py")