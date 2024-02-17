"""#Listas é uma coleção de objetos armazenadas em um objeto só

lista1 = list() #uma lista vazia
 
lista2 = ["Flamengo",128,True,500.0]
hino = ["Uma vez Flamengo sempre Flamengo!"]

somar_listas = lista2 + hino
print(somar_listas)

#Acessando index dos elementos da lista3
lista3 = ["Amarelo", "Verde", "Roxo",["Laranja", "Preto"]]
print(lista3[0]) #Imprime a cor "Amarelo"
print(lista3[1]) #Imprime a cor "Verde"
print(lista3[2]) #Imprime a cor "Roxo"
print(lista3[3][0]) #Imprime a cor "Laranja"
print(lista3[3][1]) #Imprime a cor "Preto"


#interando uma lista ou pecorrendo uma lista
for mengo in lista2:
    print(mengo)

#Interando listas aninhadas
    for mengao in hino:
        for palavra in mengao:
            print(palavra)

#Slicing em listas
numeros = list(range(1,11))
print(numeros[:3]) #Imprime 1,2,3
print(numeros[3:]) #Imprime 4,5,6,7,8,9,10
print(numeros[4:7]) #Imprime 5,6,7
print(numeros[-1:]) #imprime o ultimo elemento da lista: 10

#Atribuíndo lista em uma outra lista
"""
"""valores = []
dinheiro = list(range(100,1001,100))
for valor in dinheiro:
    valores.append(valor)
    print(valores)"""

#Metodo de adicionar com slicing
valores = [31,55,65,3,22,1]
pipas = valores[:] #COPIANDO A LISTA INTEIRA
print(pipas)

pares = list(range(1,11))
print(pares[1::2]) #IMPRIME 2,4,6,8,10

#INVERTENDO valores slicing LISTA COM SALTOS NEGATIVOS:
print(pipas[-1::-1])