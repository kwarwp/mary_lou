# Felipe
from _spy.vittolino.main import Cena, Elemento, Texto 
cena11 =  "https://i.imgur.com/vaTwNBR.png "
elemento =  "https: //bit.ly/32y88Mk"

def Historia  ():
	cenaHolmes = Cena(img = cena11)
	elem = Elemento( img = elemento, 
                     tit= "Story" ,
                     style=dict(left=150, top=60,width=60, hight=200))
	elem.entra(cenaHolmes)
	txtElem = Texto (cenaHolmes,
				"I'm Sherlock Holmes. I'm a detective who likes to follow clues and solve mysteries")
	elem.vai = txtElem.vai
	cenaHolmes.vai ()
Historia ()