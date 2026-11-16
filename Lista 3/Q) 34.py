def squared(text, size):
    for i in range(size):
        linha = ''
        for j in range(size):
            linha += text[(i * size + j) % len(text)]
        print(linha)