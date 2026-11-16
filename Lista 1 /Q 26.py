n1= int(input("Número 1: "))

n2= int(input("Número 2: "))

opcao = input("Operação: ")


if  opcao == "adicionar":

    r1 = n1+n2
    print (f"{n1} + {n2} = {r1}")
elif opcao == "multiplicar":
    r2 = n1*n2
    print(f"{n1} * {n2} = {r2}")

elif opcao == "subtrair":
    r3 = n1 - n2
    print(f"{n1} - {n2} = {r3}")
else:
    print()