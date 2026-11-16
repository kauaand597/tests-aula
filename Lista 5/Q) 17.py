def agenda():
    contatos = {}

    while True:
        comando = input("comando (1 buscar, 2 adicionar, 3 sair): ")

        if comando == "1":
            nome = input("nome: ")
            if nome in contatos:
                print(contatos[nome])
            else:
                print("nenhum número")

        elif comando == "2":
            nome = input("nome: ")
            numero = input("número: ")
            contatos[nome] = numero
            print("ok!")

        elif comando == "3":
            print("saindo...")
            break

agenda()