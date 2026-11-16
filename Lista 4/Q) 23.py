while True:
    def  palindromes(x):
        if x == x[::-1]:
            return True
        return False
    x = input("Digite um palíndromo: ")
    if palindromes(x) == True:
        print(f"{x} é um palíndromo!")
        break
    else:
        print("isso não era um palíndromo")