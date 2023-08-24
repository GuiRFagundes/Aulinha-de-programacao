#Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
#para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
#conversão.
a = int(input("Quer passar a temperatura de C para F (1) ou de F para C (2): "))
if (a == 1):
    print("escreva temperatura em celsius")
    t1 = a + 273
    print("coversão deu",t1)
else:
    print("escreva temperatura em fahrenheit")
    t2 = a -273
    print("conversão ficou",t2)
