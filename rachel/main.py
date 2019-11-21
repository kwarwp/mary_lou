#Autor: Arthur Martins
# mary_lou.rachel.main.py
# https://addons.mozilla.org/pt-BR/firefox/addon/imgur-upload/
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import Elemento_ as Elemento
#from browser import html
ciencia = "https://i.imgur.com/nX5rixb.gif"
urso = "https://i.imgur.com/nyow6zY.png"
indio ="https://i.imgur.com/jmhXTbm.png"
indios ="https://i.imgur.com/RMc3y2v.png"
interrogav = "https://i.imgur.com/vHTik0T.png"
interrogab = "https://i.imgur.com/waqbg8W.png"
interrogap ="https://i.imgur.com/lnrSyCI.png"
terraMorta = "https://i.imgur.com/MVSeRMf.jpg"
#lavaArdente = "https://i.imgur.com/PskfkEy.jpg"
lavaArdente = "https://i.imgur.com/1PR5FzX.gif"
STYLE ["width"] = 1150
STYLE ["height"] = "600px"

def lavaArdente():
    cenaLava = Cena (img = lavaArdente)
    
def cicloagua():
    cenaAgua = Cena(img = ciencia)
#CHAMA O ELEMENTO URSO E O TEXTO 
    elementourso = Elemento(img = urso, 
                     tit = "Ursinho Pooh", 
                     style = dict (top = 420, left = 25, height = 100, width = 100, bottom = 100))
    
    elementourso.entra(cenaAgua)
    textourso = Texto(cenaAgua,
                      "Ursinho Pooh")
    elementourso.vai = textourso.vai
    
#CHAMA O ELEMENTO INDIO E O TEXTO 
    elementoindio = Elemento(img = indio, 
                     tit = "Indio", 
                     style = dict (top = 400, left = 190, height = 100, width = 200))
    elementoindio.entra(cenaAgua)
    textoindio = Texto(cenaAgua,
                      "Indio Pele vermelha")
    elementoindio.vai = textoindio.vai
    
    #CHAMA O ELEMENTO INDIOS E O TEXTO 
    elementoindios = Elemento(img = indios, 
                     tit = "Indio", 
                     style = dict (top = 420, left = 350, height = 60, width = 80))
    elementoindios.entra(cenaAgua)
    textoindios = Texto(cenaAgua,
                      "Familia de indios")
    elementoindios.vai = textoindios.vai

    #CHAMA O PONTO DE INTERROGAÇÃO VERMELHO
    elementopontov = Elemento(img = interrogav, 
                     tit = "Frase 1", 
                     style = dict (top = 500, left = 530, height = 60, width = 55, bottom = 100))
    
    elementopontov.entra(cenaAgua)
    textopontov = Texto(cenaAgua,
                      "Tá")
    elementopontov.vai = textopontov.vai
    
    #CHAMA O PONTO DE INTERROGAÇÃO AZUL
    elementopontob = Elemento(img = interrogab, 
                     tit = "Frase 2", 
                     style = dict (top = 220, left = 370, height = 60, width = 55, bottom = 100))
    
    elementopontob.entra(cenaAgua)
    textopontob = Texto(cenaAgua,
                      "Xuvendo")
    elementopontob.vai = textopontob.vai

#CHAMA O PONTO DE INTERROGAÇÃO PRETO
    elementopontop = Elemento(img = interrogap, 
                     tit = "Frase 3", 
                     style = dict (top = 30, left = 800, height = 60, width = 55, bottom = 100))
    
    elementopontop.entra(cenaAgua)
    textopontop = Texto(cenaAgua,
                      "Meu povo!")
    elementopontop.vai = textopontop.vai

    #criar uma nova cena a direita
    cenaErosao = Cena(img = terraMorta)
    cenaAgua.direita = cenaErosao
    cenaErosao.vai()
    
    #se quiser voltar para a cenaAgua
    cenaErosao.esquerda = cenaAgua

    #criar uma nova cena a esquerda
    cenaVulcao = Cena(img = lavaArdente)
    cenaAgua.esquerda = cenaLava
    cenaVulcao.vai()


    #se quiser voltar para a cenaAgua
    cenaVulcao.direita = cenaAgua



    cenaAgua.vai()
cicloagua()