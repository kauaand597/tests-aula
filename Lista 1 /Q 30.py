print("Qual é a previsão do tempo para amanhã?")

temp = int(input("Temperatura: "))
chuva = input("Vai chover (sim/não): ").lower()

if temp <= 5:
    print("Use jeans e uma camiseta")
    print("Eu recomendo um jumper também")
    print("Leva um casaco contigo")
    print("Faça um casaco quente, na verdade")
    print("Acho que as luvas estão em ordem")
    if chuva == "sim":
        print("Não se esqueça do seu guarda-chuva!")


elif temp <= 10:
    print("Use jeans e uma camiseta")
    print("Eu recomendo um jumper também")
    print("Leva um casaco contigo")
    if chuva == "sim":
            print("Não se esqueça do seu guarda-chuva!")



elif temp <= 20:
    print("Use jeans e uma camiseta")
    print("Eu recomendo um jumper também")
    if chuva == "sim":
            print("Não se esqueça do seu guarda-chuva!")


else:
    print("Use jeans e uma camiseta")
    if chuva == "sim":
            print("Não se esqueça do seu guarda-chuva!")
