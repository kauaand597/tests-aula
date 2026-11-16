pin = 4321
tentativas = 0 

while True:
    input_pin = int(input("PIN: "))
    tentativas += 1
    if input_pin != pin:
        print("Errado")
    else:
        if tentativas == 1:
            print("Correto! Você precisou de apenas uma única tentativa!")
        else:
            print(f"Correto! Você precisou de {tentativas} tentativas")
        break