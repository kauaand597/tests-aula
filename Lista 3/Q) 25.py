while True:
    n= int(input("Por favor, digite um número: "))
    if n <= 0:
        print("Obrigado e até logo!")
        break
    fat =1
    for _ in range(1, n + 1):
        fat *= _
    print(f"O fatorial do número {n} é {fat}") 
