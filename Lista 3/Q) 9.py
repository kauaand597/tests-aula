# Escreva sua solução aqui
frase1 = input("Por favor, digite a string 1: ")
frase2 = input("Por favor, digite a string 2: ")

if len(frase1) == len(frase2):
    print("As strings têm o mesmo comprimento")
elif len(frase1) > len(frase2):
    print(f"{frase1} é mais longa")
else:
    print(f"{frase2} é mais longa")