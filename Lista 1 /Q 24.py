nome = input("Por favor, diga-me o seu nome: ")

if nome != "Jerry":
    porcoes = int(input("Quantas porções de sopa? "))

    custo_tota = 5.90 * porcoes

    print (f"O custo total é de {custo_tota}")
    print("Próximo por favor!") 
else:
    print("Próximo por favor!")