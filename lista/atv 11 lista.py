#Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
#trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
#ao final mostrar seu nome e salário final calculado.
a = input("Digite o nome do funcionario: ")
b = int(input("Digite o numero de horas do funcionrio: "))
c = int(input("Digite o numero de oras trabalhadas"))
s = float(input("Digite o salario do funcionario"))
d = s-s*0.002
print("Salario fina de:",d)