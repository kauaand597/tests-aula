n = int(input("Por favor, digite um número: "))

inicio = 1
fim = n

while inicio <= fim:
    print(inicio)
    if inicio != fim:
        print(fim)
    inicio += 1
    fim -= 1