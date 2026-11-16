def chessboard(size):
    for i in range(size):
        linha = ''
        for j in range(size):
            linha += str((i + j + 1) % 2)
        print(linha)