def count_matching_elements(my_matrix: list, element: int) -> int:
    contador = 0
    for linha in my_matrix:
        for valor in linha:
            if valor == element:
                contador += 1
    return contador