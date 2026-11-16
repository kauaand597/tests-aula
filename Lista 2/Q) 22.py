print("Por favor, digite números inteiros. Digite 0 para terminar.")
contador = 0
lista_numeros = []
while True:
    numero = int(input("Número: "))
    contador += 1
    lista_numeros.append(numero)
    if numero == 0:
        

        positive_numbers = len([num for num in lista_numeros if num > 0])
        negative_numbers = len([num for num in lista_numeros if num < 0])
        print(f"Números digitados {contador - 1}")
        print(f"A soma dos números é {sum(lista_numeros)}")
        print(f"A média dos números é {sum(lista_numeros) / (contador - 1)}")
        print(f"Números positivos {positive_numbers}")
        print(f"Números negativos {negative_numbers}")

        break
