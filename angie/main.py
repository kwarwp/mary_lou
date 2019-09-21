# Priscilla
from _spy.vittolino.main import Cena, Elemento, Texto
cenabeach = "data:image/jpeg;base64,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"