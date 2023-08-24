#Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
#As condições para aposentadoria são:
#• Ter pelo menos 65 anos,
#• Ou ter trabalhado pelo menos 30 anos,
#• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
a = int(input("Digite sua idade: "))
b = float(input("digite seu tempo de serviço: "))
if (a > 64) or (b > 29) or ((a > 59) and (b > 24 )):
    print("pode se aposentar")
else:
    print("não pode aposentar ainda")
    
