# callie
from _spy.vitollino.main import Cena, Elemento, Texto
cena7 = "https://i.imgur.com/sXTvNpA.png"
elemento = "https://bit.ly/32y88Mk"

def Historia():
	cenaHolmes = Cena( img = cena7)
	elem = Elemento (img = elemento, 
                      tit="story",
                      style=dict(left=150, top=60, width=120, hight=200))
	elem.entra(cenaHolmes)
	txtEleme = Texto (cenaHolmes,
    			"He was on the street, when he sees a guy in a hat surrounded by young people who were bothering him.")
	elem.vai = txtEleme.vai
	cenaHolmes.vai()
Historia()