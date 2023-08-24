#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o
#cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o
#cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos
#itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que
#monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#a. Lojas Quase Dois - Tabela de preços
#b. 1 - R$ 1.99
#c. 2 - R$ 3.98
#d. ...
#e. 50 - R$ 99.50
print("tabela de preços")

for q in range(1,51):
    p = q * 1.99
    print(f"{q:2} - R$ {p:.2f}")
