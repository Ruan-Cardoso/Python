# TUPLE e uma sequencia de dados imutaveis 

tupla = (1, 2, 3, 4, 5, 6)
type(tupla)
tupla.append("Sábado2")

# existe uma função tuple para criar um tuple de uma lista

palavras = []
palavras.append("banana")
palavras.append("abacaxi")

nova = tuple(palavras)
# isso e importante pois depois que nao quiser que a lista seja auterada é só trans formala em um tuple
