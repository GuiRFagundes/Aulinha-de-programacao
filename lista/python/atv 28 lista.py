#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
#cada eleitor votar e ao final mostrar o número de votos de cada candidato
num_eleitores = int(input("Digite o número total de eleitores: "))
candidatos = {"candidato1": 0, "candidato2": 0, "candidato3": 0}

for i in range(num_eleitores):
    print(f"Eleitor {i+1}:")
    print("Opções de voto:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")

    voto = int(input("Digite o número correspondente ao candidato escolhido: "))
        
    if voto == 1:
        candidatos["candidato1"] += 1
    elif voto == 2:
        candidatos["candidato2"] += 1
    elif voto == 3:
        candidatos["candidato3"] += 1
    else:
        print("Voto inválido. Por favor, vote novamente.")

    print("Resultado da eleição:")
    for candidato, votos in candidatos.items():
        print(f"{candidato}: {votos} votos")