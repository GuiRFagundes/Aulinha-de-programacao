#Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
#perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo.
import random

def main():
    vitorias_consecutivas = 0
    
    print("Jogo de Par ou Ímpar")
    
    while True:
        jogador = input("Escolha par (p) ou ímpar (i): ").lower()
        if jogador not in ['p', 'i']:
            print("Opção inválida. Escolha 'p' para par ou 'i' para ímpar.")
            continue
        
        numero_jogador = int(input("Digite um número entre 0 e 10: "))
        if numero_jogador < 0 or numero_jogador > 10:
            print("Número fora do intervalo válido.")
            continue
        
        numero_computador = random.randint(0, 10)
        print(f"Número escolhido pelo computador: {numero_computador}")
        
        soma = numero_jogador + numero_computador
        resultado = "par" if soma % 2 == 0 else "ímpar"
        
        print(f"A soma é {soma}, o resultado é {resultado}.")
        
        if resultado == jogador:
            print("Você venceu!")
            vitorias_consecutivas += 1
        else:
            print("Você perdeu.")
            break
    
    print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")

if __name__ == "__main__":
    main()