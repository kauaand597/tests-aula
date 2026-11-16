n1 = float(input("Salário por hora: "))
h1 = int(input("Horas trabalhadas: "))

Dia_da_sem= input("Dia da semana: ")

if Dia_da_sem == "Domingo":
    sal= 2*n1*h1
    print(f"Salários diários: {sal} euros")
else:
    sal = n1*h1
    print(f"Salários diários: {sal} euros")

