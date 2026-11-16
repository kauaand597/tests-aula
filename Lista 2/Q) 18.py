senha = input("Senha: ")

while True:
    input_senha = input("Repita a senha: ")
    if input_senha != senha:
        print("As senhas não coincidem!")
    else:
        print("Conta de usuário criada!")
        break
