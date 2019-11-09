# larissa
from _spy.vitollino.main import Cena, Elemento, Texto
cena9 = "https://i.imgur.com/LhZvA0Q.png"
elemento = "https://bit.ly/32y88MK"

def Historia():
	cenaHolmes = Cena( img = cena9)
	elem = Elemento( img = elemento,
                     tit="Story",  
                     style=dict(left=150, top=60, width=60, hight=200))
	elem.entra(cenaHolmes)
	txtElem = Texto (cenaHolmes,
    			"Holmes gave an old newspaper")
	elem.vai = txtElem.vai
	cenaHolmes.vai()
Historia()