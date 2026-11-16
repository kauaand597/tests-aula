def invert(dictionary: dict):
    itens = list(dictionary.items())
    dictionary.clear()
    for chave, valor in itens:
        dictionary[valor] = chave