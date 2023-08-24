#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
#obtidos os seguintes dados:
#a. Código da cidade; (digitado pelo usuário)
#b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
#c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
#Deseja-se saber:
#b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#c. Qual a média de veículos nas cinco cidades juntas;
#d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
c1 = c2 = c3 = c4 = c5 = []
cs = [c1,c2,c3,c4,c5]
for i in range(len(cs)):
    c = int(input("Digite o codigo da cidade: "))
    cs[i]= c
print(cs)