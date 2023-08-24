#Faça 4 listas:
#A. Filmes
#B. Jogos
#C. Livros
#D. Esporte
#a. Adicione no mínimo 2 itens em cada lista.
#b. Crie uma lista das 4 listas criadas acima.
#c. Acesse (mostrar) algum item da lista livros.
#d. Remova um item da lista esporte.

filmes = []
filmes.append("corrosII","Aviões")
jogos = []
jogos.append("LOL","Minecraft")
livros = []
livros.append("Lovecraft","Biblia")
esportes = []
esportes.append("Volei","Futebol")
listas = [filmes,jogos,livros,esportes]
print(listas())
esportes.pop(1)
print(esportes)