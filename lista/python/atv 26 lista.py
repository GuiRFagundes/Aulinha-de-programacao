#Faça um programa que leia e valide as seguintes informações:
#a. Nome: maior que 3 caracteres;
#b. Idade: entre 0 e 150;
#c. Salário: maior que zero;
#d. Sexo: 'f' ou 'm';
#e. Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres)
while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("Nome deve ter mais de 3 caracteres. Tente novamente.")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
             break
        else:
            print("Idade deve estar entre 0 e 150. Tente novamente.")
    except ValueError:
        print("Por favor, digite um valor numérico válido para a idade.")
while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break
        else:
            print("Salário deve ser maior que zero. Tente novamente.")
    except ValueError:
        print("Por favor, digite um valor numérico válido para o salário.")

while True:
    sexo = input("Digite seu sexo (f/m): ").lower()
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print("Sexo deve ser 'f' para feminino ou 'm' para masculino. Tente novamente.")

while True:
    estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil deve ser 's' para solteiro, 'c' para casado, 'v' para viúvo ou 'd' para divorciado. Tente novamente.")

    print("Informações válidas:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado_civil}")