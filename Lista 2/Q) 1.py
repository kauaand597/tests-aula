# Corrija o programa
number = int(input("Por favor, digite um número: "))
numbernv = number - 100
if number > 100:
    print("O número era maior que cem")
    print("Agora seu valor diminuiu em cem")
    print(f"Seu valor agora é {numbernv}")
    print(f"{numbernv} deve ser meu número da sorte!")
    print("Tenha um bom dia!")
else:
    print(f"{number} deve ser meu número da sorte!")
    print("Tenha um bom dia!")