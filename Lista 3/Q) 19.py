text = input('Por favor, digite uma string: ').replace(' ', '').lower()

vogais = {'a': 0, 'e': 0, 'o': 0}

for letra in text:
    if letra in vogais:
        vogais[letra] += 1

achou_alguma = False

for vogal, quantidade in vogais.items():
    if quantidade > 0:
        print(f"{vogal} encontrada")
    if quantidade == 0:
        print(f"{vogal} não encontrada")
        achou_alguma = True


