def agenda():
    contatos = {}

    while True:
        comando = input("comando (1 buscar, 2 adicionar, 3 sair): ")

        if comando == "1":
            nome = input("nome: ")
            if nome in contatos:
                for numero in contatos[nome]:
                    print(numero)
            else:
                print("nenhum número")

        elif comando == "2":
            nome = input("nome: ")
            numero = input("número: ")
            if nome not in contatos:
                contatos[nome] = []
            contatos[nome].append(numero)
            print("ok!")

        elif comando == "3":
            print("saindo...")
            break

agenda()