def row_correct(sudoku: list, row_no: int):
    vistos = []
    for valor in sudoku[row_no]:
        if valor != 0:
            if valor in vistos:
                return False
            vistos.append(valor)
    return True