def print_sudoku(sudoku: list):
    for i, linha in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print()
        grupos = []
        for j in range(0, 9, 3):
            grupo = ["_" if v == 0 else str(v) for v in linha[j:j + 3]]
            grupos.append(" ".join(grupo))
        print("  ".join(grupos))


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number