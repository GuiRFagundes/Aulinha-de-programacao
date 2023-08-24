#Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
#peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
#aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos
a = float(input("digite sua 1° nota (max 5): "))
b = float(input("Digite sua 2° nota (max 5): "))
c = float(input("Digite sua 3° nota : "))
m = (a+b+c)/2
if (m >= 6):
    print("Você foi aprovado")
    print(m)
else:
    print("Reprovado")
    print(m)