def main():
    ns = []
    while True:
        try:
            n = int(input("Digite um número inteiro: "))
            ns.append(n)
        except ValueError:
            print("digite um número inteiro válido.")
        
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break
    
    if ns:
        media = sum(ns) / len(ns)
        maior = max(ns)
        menor = min(ns)
        
        print(f"Média: {media}")
        print(f"Maior valor: {maior}")
        print(f"Menor valor: {menor}")
    else:
        print("Nenhum número foi digitado.")

if __name__ == "__main__":
    main()
