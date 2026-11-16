def column_correct(sudoku: list, column_no: int):
    vistos = []
    for linha in sudoku:
        valor = linha[column_no]
        if valor != 0:
            if valor in vistos:
                return False
            vistos.append(valor)
    return True