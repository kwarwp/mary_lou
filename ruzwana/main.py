# Laurenice
from _spy.vitollino.main import Cena, Elemento, Texto
cena11 ="https://i.imgur.com/K1Amaae.png" 
elemento = "https://bit.ly/32y88Mk" 
 
def Historia(): 
	cenaHolmes = Cena( img = cena11)
	elem = Elemento( img = elemento,
                      tit="story", 
                      style =dict(left=150, top=60, width=120, hight=200)) 
	elem.entra(cenaHolmes)
	txtElem = Texto (cenaHolmes,
    			 "Mr. Watson, best friend and companion in the adventures of Sherlok Homes.")
	elem.vai = txtElem.vai
	cenaHolmes.vai()
Historia()

