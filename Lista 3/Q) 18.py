texto = input("Por favor, digite uma string: ")

inicio = len(texto) - 1
while inicio >= 0:
    print(texto[inicio:])
    inicio -= 1