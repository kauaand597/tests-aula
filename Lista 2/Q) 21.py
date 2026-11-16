text = []

while True:
    palavra = input("Por favor, digite uma palavra: ")
    
    if text and text[-1] == palavra:
        break

    text.append(palavra)

    if palavra == "fim":
        text.pop()  # remove "fim" da lista
        break

print(" ".join(text))