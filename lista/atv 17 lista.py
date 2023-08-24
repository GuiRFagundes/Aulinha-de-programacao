#Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
#utilizando as seguintes formulas (onde h corresponde à altura):
#• Homens: (72.7 ∗ h) − 58
#• Mulheres: (62, 1 ∗ h) − 44, 7
a = float(input("Digite sua altura: "))
b = input("Digite seu sexo M(masculino) ou F (feminino): ")
if (b == "M"):
    pm = (72.7 * a) - 58
    print("Seu peso ideal é",pm)
else:
    pf = (62.1 * a) - 44.7
    print("Seu peso ideal", pf)