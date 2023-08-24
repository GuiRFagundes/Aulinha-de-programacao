#Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
#mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
#Euros.
a = input("digite seu nome: ")
b = float(input("digite quantidade de dinheiro na carteira: "))
d = b/4.87
print("quantidade em dolar:",d)
e = b/5.27
print("quantidade em euros:",e)
