texto = input("Por favor, digite uma string: ")
sub = input("Por favor, digite uma substring: ")

primeira = texto.find(sub)

if primeira == -1:
    print("A substring não ocorre duas vezes na string.")
else:
    segunda = texto.find(sub, primeira + len(sub))
    if segunda == -1:
        print("A substring não ocorre duas vezes na string.")
    else:
        print(f"A segunda ocorrência da substring está no índice {segunda}.")