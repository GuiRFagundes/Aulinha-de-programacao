#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
#continue pedindo até que o usuário informe um valor válido.
def main():
    while True:
        try:
            n = float(input("Digite uma nota de 0 a 10"))
            if 0<= n <=10:
                break
            else:
                print("Valor invalida")
        except ValueError:
                print("Porfavor, indera valor valido")
    print("você colocou a nota {}".format(n))

if __name__ == "__main__":
     main()
