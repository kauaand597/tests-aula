doacao = int(input("Valor da doação: "))
imposto = 0
if doacao <5000:
    print("Sem imposto!")
elif doacao >= 5000 and doacao < 25000:
    imposto = 100 + ((doacao - 5000) * 0.08)
    print(f"Valor do imposto: {imposto} euros")
elif doacao >= 25000 and doacao < 55000:
    imposto = 1700 + ((doacao - 25000) * 0.10)
    print(f"Valor do imposto: {imposto} euros")
elif doacao >= 55000 and doacao < 200000:
    imposto = 4700 + ((doacao - 55000) * 0.12)
    print(f"Valor do imposto: {imposto} euros")
elif doacao >= 200000 and doacao < 1000000:
    imposto = 22100 + ((doacao - 200000) * 0.15)
    print(f"Valor do imposto: {imposto} euros")
else:
    imposto = 142100 + ((doacao - 1000000) * 0.17)
    print(f"Valor do imposto: {imposto} euros")
    