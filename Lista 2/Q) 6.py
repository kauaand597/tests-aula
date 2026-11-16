print("Pessoa 1:")
nome1 = input("Nome: ")
idade1 = input("Idade: ")
print("Pessoa 2:")
nome2 = input("Nome: ")
idade2 = input("Idade: ")

if idade2 == idade1:
    print(f"{nome1} e {nome2} têm a mesma idade")

if idade1 > idade2:
    print(f"A pessoa mais velha é {nome1}")
elif idade2 > idade1:
    print(f"A pessoa mais velha é {nome2}")