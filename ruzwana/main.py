# Laurenice
from _spy.vitollino.main import Cena, Elemento, Texto
cena11 ="https://i.imgur.com/K1Amaae.png" 
elemento ="https://bit.ly/32y88Mk" 
 
def Historia(): 

	cenaHolmes = Cena( img = cena11)
	elem = Elemento (img = elemento)
                   tit = "story", 
                   stile =dict(left=150, top=60, width=60, highit=200) 
	elem.entra(cenaHolmes)
	txtElem = Texto (cenaHolmes,
    			 "")
	elem.vai = txtElem.vai
	cenaHolmes.vai()
Historia()

