# Acessar elemenmtos da matriz
import numpy as np
'''
A indexação de array é o mesmo que acessar um elemento de array.

Você pode acessar um elemento de array consultando seu número de índice.

Os índices em arrays Numpy começam com 0, o que significa que o primeiro elemento tem índice 0, e o segundo tem índice 1, etc.

'''

# Obtenha o primeiro elemento do seguinte array:

arr1 = np.array([2,4,6,10])
print(arr1[0])

# Obtenha o segundo elemento da matriz:
print(arr1[1])

# Obtenha o terceiro e quarto elemento da matriz e some-os:
print(arr1[2] + arr1[3])

# Acesse Matrizes 2-D:
''' 
Para acessar elementos de arrays 2-D, podemos usar inteiros separados por vírgula representando a dimensão e o índice do elemento.

Pense nas matrizes 2D como uma tabela com linhas e colunas, onde a dimensão representa a linha e o índice representa a coluna.

'''
# Acesse o elemento na primeira linha, segunda coluna:
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2 elemento da primeira linha: ', arr[0, 1]) # 2

#arr_2D =np.array([[1,2,3,4,5], [6,7,8,9,10]])
#print(arr_2D)

#Acesse o elemento na 2 linha, 5 colna: 

print('5 elememnto da 2 linha:', arr[1,4]) # 10



# Acesando Matrizes 3D

'''
Para acessar elementos de arrays 3D podemos usar inteiros separados por vírgula representando as dimensões e o índice do elemento.

'''
# Acesse o terceiro elemento do segundo array do primeiro array:

arr_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print('resposta é:', arr_3D[0,1,2]) #6

# Explicação:

''' 
arr[0, 1, 2]imprime o valor 6.

E é por isso:

O primeiro número representa a primeira dimensão, que contém duas matrizes:
[[1, 2, 3], [4, 5, 6]]
e:
[[7, 8, 9], [10, 11, 12]]
Desde selecionamos 0, ficamos com o primeiro array:
[[1, 2, 3], [4, 5, 6]]

O segundo número representa a segunda dimensão, que também contém dois arrays:
[1, 2, 3]
e:
[4, 5, 6]
Como selecionamos 1, ficamos com o segundo array:
[4, 5, 6]

O terceiro número representa a terceira dimensão, que contém três valores:
4
5
6
Como selecionamos 2, terminamos com o terceiro valor:
6
'''

# Indexação Negativa

''' 
Use indexação negativa para acessar um array do final.
'''

# Imprima o última elemento do 2 dim:

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])
