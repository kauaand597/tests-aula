
from math import sqrt

while True:

    num = int(input("Por favor, digite um número: "))
    if num == 0:
        print("Saindo...")
        break
    if num < 0:
        print("Número inválido")
    else:
        print(sqrt(num))

    