def block_correct(sudoku: list, row_no: int, column_no: int):
    vistos = []
    for i in range(3):
        for j in range(3):
            valor = sudoku[row_no + i][column_no + j]
            if valor != 0:
                if valor in vistos:
                    return False
                vistos.append(valor)
    return True