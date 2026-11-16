n1 = int(input("Por favor, digite o primeiro número: "))
n2 = int(input("Por favor, digite outro número: "))

if n1 > n2:
    print(f"O maior número era: {n1}")

elif n2 > n1:
    print(f"O maior número era: {n2}")

else:
    print("Os números são iguais!")