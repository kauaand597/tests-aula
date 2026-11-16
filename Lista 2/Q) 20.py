ano = int(input("Ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    proximo = ano + 1
    while not ((proximo % 4 == 0 and proximo % 100 != 0) or (proximo % 400 == 0)):
        proximo += 1
    print(f"O próximo ano bissexto após {ano} é {proximo}")
else:
    proximo = ano + 1
    while not ((proximo % 4 == 0 and proximo % 100 != 0) or (proximo % 400 == 0)):
        proximo += 1
    print(f"O próximo ano bissexto após {ano} é {proximo}")