#) Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
#Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
#a. Soma de 2 n´umeros.
#b. Diferença entre 2 números (maior pelo menor).
#c.Produto entre 2 números.
#d. Divisão entre 2 números (o denominador não pode ser zero).
a = input("escolha uma das opções \n a. Soma de 2 numeros. \n b. Diferença entre 2 números (maior pelo menor). \n c. Produto entre 2 números. \n d. divisão entre 2 números (o denominador não pode ser zero). ")
if (a == "a"):
    a1 = input("digite 1° numero: ")
    a2 = input("digite 2° numero: ")
    sa = a1 + a2
    print("a soma deu",sa)
elif (a == "b"):
    b1 = input("digite 1° numero: ")
    b2 = input("digite 2° numero: ")
    sb = b1 - b2
elif (a == "c"):
    c1 = input("digite 1° numero: ")
    c2 = input("digite 2° numero: ")
    sc = c1 * c2
elif (a == "d"):
    d1 = input("digite 1° numero (não pode ser 0): ")
    d2 = input("digite 2° numero (não poder ser 0): ")
    sd = d1/d2
    if ((d1 == 0) or (d2 == 0)):
        print("ERROR")
else:
    print("ERROR")