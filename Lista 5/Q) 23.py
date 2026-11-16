def create_tuple(x: int, y: int, z: int):
    menor = min(x, y, z)
    maior = max(x, y, z)
    soma = x + y + z
    return (menor, maior, soma)


print(create_tuple(5, 3, -1))  # Saída: (-1, 5, 7)