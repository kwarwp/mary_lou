# Jacqueline
from _spy.vitollino.main import Cena, Elemento, Texto
cena11 = "https://i.imgur.com/VSPdalA.png "
elemento = "https://bit.ly/32y88Mk"

def Historia():
	cenaHolmes = Cena( img = cena11)
	elem = Elemento( img = elemento,
                     tit="Story",
                     style=dict(left=150, top=60, width=60, hight=200))
	elem.entra(cenaHolmes)
	txtElem= Texto (cenaHolmes,
			"The duchess is awaiting news of a possible pregnancy.")    
	cenaHolmes.vai()
Historia()