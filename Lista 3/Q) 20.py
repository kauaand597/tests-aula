texto = input('Por favor, digite uma palavra: ')
caractere = input('Por favor, digite um caractere: ')

for i in range(len(texto) - 2):
    if texto[i] == caractere:
        print(texto[i:i+3])
        break
