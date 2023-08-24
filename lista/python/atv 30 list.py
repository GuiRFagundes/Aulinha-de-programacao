#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de
#conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá
#receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser
#informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e
#perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta
#operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser
#conforme o exemplo abaixo:
#a. Lojas Tabajara
#b. Produto 1: R$ 2.20
#c. Produto 2: R$ 5.80
#d. Produto 3: R$ 0
#e. Total: R$ 9.00
#f. Dinheiro: R$ 20.00
#g. Troco: R$ 11.00
#h. ...
while True:
        print("Lojas Tabajara - Caixa Registradora")
        
        total = 0.0
        produtos = []
        
        while True:
            try:
                preco = float(input("Digite o preço do produto (ou 0 para finalizar): "))
                if preco == 0:
                    break
                else:
                    produtos.append(preco)
                    total += preco
            except ValueError:
                print("Por favor, digite um valor numérico válido.")
        
        print("Produtos:")
        for i, preco in enumerate(produtos, start=1):
            print(f"Produto {i}: R$ {preco:.2f}")
        
        print(f"Total: R$ {total:.2f}")
        
        while True:
            try:
                dinheiro = float(input("Digite o valor em dinheiro fornecido pelo cliente: "))
                if dinheiro < total:
                    print("O valor em dinheiro fornecido é insuficiente.")
                else:
                    break
            except ValueError:
                print("Por favor, digite um valor numérico válido.")
        
        troco = dinheiro - total
        print(f"Dinheiro: R$ {dinheiro:.2f}")
        print(f"Troco: R$ {troco:.2f}")
        
        reiniciar = input("Deseja registrar outra compra? (s/n): ")
        if reiniciar.lower() != 's':
            break