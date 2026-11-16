# Escreva sua solução aqui
n1 = int(input("Quantas vezes por semana você come na cafeteria estudantil? "))
n2 = float(input("O preço de um almoço típico de estudante? "))
n3 = float(input("Quanto dinheiro você gasta em mantimentos em uma semana? "))

gasto_semana= n3 + (n2*n1)
gasto_dia= gasto_semana / 7

print()
print("Despesa média alimentar:")
print(f"Diário: {gasto_dia:.1f} euros")
print(f"Semanal: {gasto_semana:.1f} euros")