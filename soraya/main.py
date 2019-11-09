# Jacqueline
from _spy.vitollino.main import Cena, Elemento, Texto
cena11 = "https://i.imgur.com/8vImpkP.png"
elemento = "encurtador.com.br/aegw0"

def Historia():
	cenaHolmes = Cena( img = cena11)
	elem = Elemento( img = elemento,
                     tit="Story",
                     style=dict(left=150, top=60, width=60, hight=200))
	cenaHolmes.vai()
Historia()