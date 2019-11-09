# joice
from _spy.vitollino.main import Cena, Elemento, Texto
cena2 = "https://i.imgur.com/JcgDwgJ.png"
elemento = "https://bit.ly/32y88Mk"

def Historia():
	cenaHolmes = Cena( img = cena2)
	elem = Elemento(img = elemento, 
                       tit="Story",
                       style=dict(left=150, top=60, width=150, hight=200))
	elem.entra(cenaHolmes)
	txtElem = Texto (cenaHolmes,
    			"I entered the room and Holmes was analyzing a hat")
	elem.vai = txtElem.vai
	cenaHolmes.vai()
Historia()