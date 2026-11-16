palavra = input("Por favor, digite uma palavra: ")
caractere = input("Por favor, digite um caractere: ")

for i in range(len(palavra) - 2):
    if palavra[i] == caractere:
        print(palavra[i:i+3])