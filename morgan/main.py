# Jane
from _spy.vitollino.main import Cena,Elemento,Texto
cena3 = "https://i.imgur.com/mgp4E0g.png"
elemento ="encurtador.com.br/aegw0"

def Historia():
	cenaHolmes = Cena( img = cena3)
	elen = Elemento  (img = elemento,
                       tit="Story",
                       style=dict(left=150, top=60, width=60, hight=200))
	cenaHolmes.vai()
Historia()