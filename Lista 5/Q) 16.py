def histogram(s):
    contagem = {}
    for letra in s:
        contagem[letra] = contagem.get(letra, 0) + 1

    for letra, qtd in contagem.items():
        print(letra, "*" * qtd)