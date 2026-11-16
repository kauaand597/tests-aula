alunos= int(input("Quantos alunos do curso? "))
tamanho_gp_querido= int(input("Tamanho do grupo desejado? "))

numero_de_grupos = alunos // tamanho_gp_querido

if alunos % tamanho_gp_querido != 0:
    numero_de_grupos += 1
print(f"Número de grupos formados: {numero_de_grupos}")