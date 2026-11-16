# Copie aqui a sua função line do exercício anterior:
def line(number, character):
    print(character * number)

# Escreva sua solução aqui
def box_of_hashes(height):
    for _ in range(height):
        line(10, "#")