# Escreva sua solução aqui
idade = int(input("Qual é a sua idade? "))

if idade < 0:
    print("Isso deve ser um engano")
elif idade < 5:
    print("Desconfio que você ainda não sabe escrever...")
else:
    print(f"Ok, você tem {idade} anos")