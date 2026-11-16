temp= int(input("Por favor, digite uma temperatura (F): "))

c = (temp - 32) / 1.8

if c > 0:
    print(f"{temp} graus Fahrenheit é igual a {c} graus Celsius")
else:
    print(f"{temp} graus Fahrenheit é igual a {c} graus Celsius")
    print(f"Brr! Está frio aqui!")