def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copia = []
    for linha in sudoku:
        copia.append(linha[:])
    copia[row_no][column_no] = number
    return copia