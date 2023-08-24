#) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
#obtidos os seguintes dados:
##a. Código da cidade; (digitado pelo usuário)
#b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
##c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
#Deseja-se saber:
#b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#c. Qual a média de veículos nas cinco cidades juntas;
#d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio
def main():
    num_cidades = 5
    maior_indice = float('-inf')
    menor_indice = float('inf')
    total_veiculos = 0
    total_acidentes_menos_2000 = 0

    for i in range(num_cidades):
        print(f"Cidade {i + 1}")
        
        codigo_cidade = int(input("Código da cidade: "))
        veiculos_passeio = int(input("Número de veículos de passeio em 1999: "))
        acidentes_vitimas = int(input("Número de acidentes de trânsito com vítimas em 1999: "))
        
        indice_acidentes = acidentes_vitimas / veiculos_passeio
        
        if indice_acidentes > maior_indice:
            maior_indice = indice_acidentes
            cidade_maior_indice = codigo_cidade
        
        if indice_acidentes < menor_indice:
            menor_indice = indice_acidentes
            cidade_menor_indice = codigo_cidade
        
        total_veiculos += veiculos_passeio
        
        if veiculos_passeio < 2000:
            total_acidentes_menos_2000 += acidentes_vitimas
    
    media_veiculos = total_veiculos / num_cidades
    media_acidentes_menos_2000 = total_acidentes_menos_2000 / num_cidades
    
    print(f"Maior índice de acidentes: {maior_indice:.2f}, Cidade: {cidade_maior_indice}")
    print(f"Menor índice de acidentes: {menor_indice:.2f}, Cidade: {cidade_menor_indice}")
    print(f"Média de veículos nas cidades: {media_veiculos:.2f}")
    print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_menos_2000:.2f}")

if __name__ == "__main__":
    main()