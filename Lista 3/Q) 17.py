texto = input("Por favor, digite uma string: ")

tamanho = 1
while tamanho <= len(texto):
    print(texto[:tamanho])
    tamanho += 1