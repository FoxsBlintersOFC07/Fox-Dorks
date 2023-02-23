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
   result = pyfiglet.figlet_format("COPIE E COLE UMA DORK ABAIXO", font = "slant") 
   print(result)
banner() 
#Pergunta

def Lista():
   print(f''''
\033[1;34m『1』➥\033[0;0m view_items.php?id=
\033[1;34m『3』➥\033[0;0m home.php?cat=
\033[1;34m『4』➥ \033[0;0m item_book.php?CAT=
\033[1;34m『5』➥ \033[0;0m www/index.php?page=
\033[1;34m『6』➥ \033[0;0m schule/termine.php?view=
\033[1;34m『7』➥ \033[0;0m goods_detail.php?data=
\033[1;34m『8』➥ \033[0;0m storemanager/contents/item.php?page_code=
\033[1;34m『9』➥ \033[0;0m view_items.php?id=
\033[1;34m『10』➥ \033[0;0m customer/board.htm?mode=
\033[1;34m『11』➥ \033[0;0m help/com_view.html?code=
\033[1;34m『12』➥ \033[0;0m n_replyboard.php?typeboard=
\033[1;34m『13』➥ \033[0;0m eng_board/view.php?T****=
\033[1;34m『14』➥ \033[0;0mprev_results.php?prodID=
\033[1;34m『15』➥ \033[0;0mbbs/view.php?no=
\033[1;34m『16』➥ \033[0;0m gnu/?doc=
\033[1;34m『17』➥ \033[0;0m zb/view.php?uid=
\033[1;34m『18』➥ \033[0;0m global/product/product.php?gubun=
\033[1;34m『19』➥ \033[0;0m m_view.php?ps_db=
\033[1;34m『20』➥ \033[0;0m productlist.php?tid=
\033[1;34m『21』➥ \033[0;0m product-list.php?id=
\033[1;34m『22』➥ \033[0;0m onlinesales/product.php?product_id=
\033[1;34m『23』➥ \033[0;0m garden_equipment/Fruit-Cage/product.php?pr=
\033[1;34m『24』➥ \033[0;0m product.php?shopprodid=
\033[1;34m『25』➥ \033[0;0m product_info.php?products_id=
\033[1;34m『26』➥ \033[0;0m productlist.php?tid=
\033[1;34m『27』➥ \033[0;0m showsub.php?id=
\033[1;34m『28』➥ \033[0;0m productlist.php?fid=
\033[1;34m『29』➥ \033[0;0m products.php?cat=
\033[1;34m『30』➥ \033[0;0m products.php?cat=
\033[1;34m『31』➥ \033[0;0m product-list.php?id=
\033[1;34m『32』➥ \033[0;0m product.php?sku=
\033[1;34m『33』➥ \033[0;0m store/product.php?productid=
\033[1;34m『34』➥ \033[0;0m products.php?cat=
\033[1;34m『35』➥ \033[0;0m productList.php?cat=
\033[1;34m『36』➥ \033[0;0m product_detail.php?product_id=
\033[1;34m『37』➥ \033[0;0m product.php?pid=
\033[1;34m『38』➥ \033[0;0m view_items.php?id=
\033[1;34m『39』➥ \033[0;0m more_details.php?id=
\033[1;34m『40』➥ \033[0;0m county-facts/diary/vcsgen.php?id=
\033[1;34m『41』➥ \033[0;0m idlechat/message.php?id=
\033[1;34m『42』➥ \033[0;0m podcast/item.php?pid=
\033[1;34m『43』➥ \033[0;0m products.php?act=
\033[1;34m『44』➥ \033[0;0m details.php?prodId=
\033[1;34m『45』➥ \033[0;0m socsci/events/full_details.php?id=
\033[1;34m『46』➥ \033[0;0m ourblog.php?categoryid=
\033[1;34m『47』➥ \033[0;0m mall/more.php?ProdID=
\033[1;34m『48』➥ \033[0;0m archive/get.php?message_id=
\033[1;34m『49』➥ \033[0;0m english/publicproducts.php?groupid=
\033[1;34m『50』➥ \033[0;0m news_and_notices.php?news_id=
\033[1;34m『51』➥ \033[0;0m rounds-detail.php?id=
\033[1;34m『52』➥ \033[0;0m gig.php?id=
\033[1;34m『53』➥ \033[0;0m board/view.php?no=
\033[1;34m『54』➥ \033[0;0m index.php?modus=
\033[1;34m『55』➥ \033[0;0m news_item.php?id=
''')

Lista()

#Autorizar para iniciar o menu de dork

autorizacao = input("APÓS COPIAR SUA DORK, DIIGTE: " + VERMELHO + '"Y"' + INCOLOR + " PARA PROSSEGUIR: \033[0;32m ")

if autorizacao == "Y" or "y":
   clear()
   os.system("python index.py")
elif autorizacao == "N" or "n":
   print("「!」➤ Comando Inválido");time.sleep(0.7)
   os.system("python dorks.sql.py")
elif autorizacao:
   print("「!」➤ Comando Inválido");time.sleep(0.7)
   os.system("python dorks.sql.py")