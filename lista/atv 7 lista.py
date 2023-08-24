#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
#de aumento
a = float(input("digite o preço do produto"))
d1 = a-(a*0.05)
print("desconto de 5%",d1)
d2 = a *1.15
print("aumento de 15%",d2)