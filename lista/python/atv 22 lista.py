#Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
#digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
#Desconsiderando o valor 1000 da parada.
def main():
    numeros=[]
    while True:
        numero = int(input("digite um numero (1000 para parar): "))
        if numero == 1000:
            break
        numeros.append(numero)
    qn = len(numeros)
    sm = sum(numeros)
    print("Foram digitados {} numeros".format(qn))
    print(f"A soma dos numeros é: {sm}")
if __name__=="__main__":
    main()