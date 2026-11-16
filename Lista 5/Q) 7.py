def row_correct(sudoku: list, row_no: int) -> bool:
    numeros = [v for v in sudoku[row_no] if v != 0]
    return len(numeros) == len(set(numeros))


def column_correct(sudoku: list, column_no: int) -> bool:
    numeros = [linha[column_no] for linha in sudoku if linha[column_no] != 0]
    return len(numeros) == len(set(numeros))


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


def sudoku_grid_correct(sudoku: list) -> bool:
    for i in range(9):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False

    for linha in range(0, 9, 3):
        for coluna in range(0, 9, 3):
            if not block_correct(sudoku, linha, coluna):
                return False

    return True