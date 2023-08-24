#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
#códigos utilizados são:
# 1 , 2, 3, 4 - Votos para os respectivos candidatos
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#a. O total de votos para cada candidato;
#b. O total de votos nulos;
#c. O total de votos em branco;
#d. A percentagem de votos nulos sobre o total de votos;
#e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
#valor zero
Beninca = []
Rafael = []
Avila = []
Gui = []
Nulo = []

while True:
    a = int(input("digite em quem quer votar: \n 1-Beninca \n 2-Rafael \n 3-Avila \n 4-Gui \n 5-Nulo \n 6-Parar "))
    if (a == 1):
        Beninca.append(1)
    elif (a == 2):
        Rafael.append(1)
    elif (a == 3):
        Avila.append(1)
    elif (a == 4):
        Gui.append(1)
    elif (a == 5):
        Nulo.append(1)
    else:
        break
totalv = sum(Beninca)+sum(Rafael)+sum(Avila)+sum(Gui)+sum(Nulo)
np = ((sum(Nulo)*100)/totalv)
print(f"Total de votos de cada candidato \n Beninca: {sum(Beninca)} \n Rafael: {sum(Rafael)} \n Avila: {sum(Avila)} \n Gui: {sum(Gui)} \n {sum(Nulo)}")
