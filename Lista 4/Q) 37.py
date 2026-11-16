notas = []
pontos = []

while True:
    linha = input("Pontos da prova e exercícios concluídos: ")
    if linha == "":
        break
    partes = linha.split()
    prova = int(partes[0])
    exercicios = int(partes[1])

    pontos_exercicios = exercicios // 10
    total = prova + pontos_exercicios

    if prova < 10:
        nota = 0
    elif total <= 14:
        nota = 0
    elif total <= 17:
        nota = 1
    elif total <= 20:
        nota = 2
    elif total <= 23:
        nota = 3
    elif total <= 27:
        nota = 4
    else:
        nota = 5

    pontos.append(total)
    notas.append(nota)

media = sum(pontos) / len(pontos)
aprovados = len([n for n in notas if n > 0])
percentual = aprovados / len(notas) * 100

print("Estatísticas:")
print(f"Média de pontos: {media:.1f}")
print(f"Percentual de aprovação: {percentual:.1f}")
print("Distribuição de notas:")
for n in range(5, -1, -1):
    print(f"  {n}: " + "*" * notas.count(n))