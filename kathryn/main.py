# cibele
from _spy.vitollino.main import Cena, Elemento, Texto
cena11 = "https://i.imgur.com/8vImpkP.png"
elemento = "https://bit.ly/32y88Mk"

def Historia():
	cenaHolmes = Cena(img = cena11)
	elem = Elemento(img = elemento,
                     tit="Story",
                     style=dict(left=150, top=60, width=120, hight=200))
	elem.entra(cenaHolmes)
	txtElem = Texto (cenaHolmes,
    			 "Hello")
	elem.vai = txtElem.vai          
	cenaHolmes.vai()
Historia()