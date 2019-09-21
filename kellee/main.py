# Felipe
from _spy.vittolino.main import Cena, Elemento, Texto 
cenafloresta = "data:image/jpeg;base64,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"
elementoprincipe = "http://www.imagenspng.com.br/wp-content/uploads/2015/04/branca-de-neve-cute-principe-04.png"
