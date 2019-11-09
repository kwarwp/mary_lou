# andre
from _spy.vitollino.main import Cena, Elemento, Texto
cena11 = "https://i.imgur.com/E7aDjws.png" 
elemento = "https://bit.ly/32y88mk"

def Historia():
	cenaHolmes = Cena( img = cena11)
	elem = Elemento( img = elemento,
                     tit="Story",
                     style=dict(left=150, top=60, width=60, hight=200))
	elem.entra(cenaHolmes,
	txElem = Texto (cenaHolmes,
    			"The diamond is on the floor. At the entrance of the house")
        elem.vai = txElem.vai
	cenaHolmes.vai()
Historia()