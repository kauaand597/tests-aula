n = int(input("Camadas: "))

lado = 2 * n - 1
centro = n - 1

for i in range(lado):
    linha = ""
    for j in range(lado):
        distancia = max(abs(i - centro), abs(j - centro))
        linha += chr(ord("A") + distancia)
    print(linha)