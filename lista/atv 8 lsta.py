#Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
#quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
a = float(input("Digite a largura da parede: "))
b = float(input("digite a altura da parede : "))
ar = a*b
t = ar/2
print("Quantidade de baldes necessarios é de",t)