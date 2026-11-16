frase = input('Por favor, digite uma frase: ')

palavras = frase.split()

for palavra in palavras:
    print(palavra[0])