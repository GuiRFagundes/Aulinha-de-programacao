#Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
#os itens repetidos. 
a = ["Mari","Bruno","Bruno","Jorge","Yuri"]
print(a.count("Bruno"))
#print(f"O item {a[1]} aparece {a.count("Bruno")} vezes na lista")
print("O item {} aparece {} vezes na lista".format(a[1], a.count("Bruno")))
