while True:
    u = input("Digite seu nome de usuário: ")
    s = input("Digite sua senha: ")

    if s != u:
        print("Cadastro realizado com sucesso!")
        break
    else:
        print("Erro: a senha não pode ser igual ao nome de usuário. Tente novamente.")