palavra = input("Por favor, digite uma string: ")

if palavra[1] == palavra[-2]:
    print(f"O segundo e o penúltimo caractere são {palavra[1]}")
else:
    print("O segundo e o penúltimo caractere são diferentes")