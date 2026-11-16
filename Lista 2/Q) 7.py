text1 = input("Por favor, digite a 1ª palavra: ").lower()
text2 = input("Por favor, digite a 2ª palavra: ").lower()

if text1 == text2:
    print("Você digitou a mesma palavra duas vezes.")
elif text1 < text2:
    print(f"{text2} vem por último em ordem alfabética.")
else:
    print(f"{text1} vem por último em ordem alfabética.")