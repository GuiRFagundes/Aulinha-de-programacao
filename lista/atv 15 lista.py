#Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
#tela dizendo se está “quente”, “frio” ou “agradável”.
a = int(input("Diigte a temperatura: "))
if (a < 20):
    print("Frio")
elif a < 24:
    print("agradavel")
else:
    print("quente")