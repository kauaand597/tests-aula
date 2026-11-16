def transpose(matrix: list):
    size = len(matrix)
    for row in range(size):
        for column in range(row + 1, size):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
  