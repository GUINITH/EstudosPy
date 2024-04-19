import numpy as np

#cRIANDO Matrizes



# Dimensões em matrizes 

"""
- Uma dimensão em arrays é um nível de profundidade de array (matrizes aninhadas).

- array aninhado: são arrays que possuem arrays como seus elementos.

"""

# Matrizes 0-D

# Matrizes 0-D, ou escalares, são os elementos de uma matriz. Cada valor em uma matriz é uma matriz 0-D.

arr1 = np.array(42)
print(arr1)

num = 44
arr2 = np.array(num)
print(arr2)



# Matrizes 1-D

"""
Uma matriz que possui matrizes 0-D como seus elementos é chamada de matriz unidimensional ou 1-D.

Estas são as matrizes mais comuns e básicas.
"""

# Crie uma matriz 1-D contendo os valores 1,2,3,4,5:

arr_exemple1 = np.array([1,2,3,4,5])
print(arr_exemple1)

num = list(range(1,6))
arr_exemple2 = np.array(num)
print(arr_exemple2)

# Matrizes 2-D

"""
Uma matriz que possui matrizes 1-D como elementos é chamada de matriz 2-D.

Eles são frequentemente usados ​​para representar matrizes ou tensores de 2ª ordem.

NumPy tem um submódulo inteiro dedicado a operações matriciais chamado numpy.mat
"""
# Crie um array 2-D contendo dois arrays com os valores 1,2,3 e 4,5,6:

num_listas = [[1,2,3], [4,5,6]]
arr_2D = np.array(num_listas)
print(arr_2D)

arr_2D = np.array([[1,2,3], [4,5,6]])
print(arr_2D)

# Matrizes 3-D

"""
Uma matriz que possui matrizes 2-D (matrizes) como seus elementos é chamada de matriz 3-D.

Estes são frequentemente usados ​​para representar um tensor de 3ª ordem.

"""

# Crie uma matriz 3D com duas matrizes 2D, ambas contendo duas matrizes com os valores 1,2,3 e 4,5,6:


listas = [[1,2,3], [4,5,6], [7,8,9]]
arr_3D = np.array(listas)
print(arr_3D)

# Verofoque o número de dimensões?

'''
Numpy Arrays fornece o ndim atribute que retorna um número inteiro que nos informa quantas dimensões o array póssui.
'''

# Verfique quantas dimensões os arrays póssuem:

a = np.array(30) # dimensão 0
b = np.array([1,2,3,4,5,6]) # dimensão 1
c = np.array([[1,2,3],[4,5,6]]) # duas dimensões
d = np.array([[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]]) # três dimensões

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Matrizes Dimensionais Superiores

'''
Uma matriz pode ter qualquer número de dimensões.

Quando a matriz é criada, você pode definir o número de dimensões usando o ndmin argumento.

'''

# Criando um Array de 5 dimensões e verifique se ele possui 5 dimensões:

arr = np.array([2,4,6,8], ndmin = 5)

print(arr)
print(f'Número de dimensões é:  {arr.ndim}')

''' 

Neste array a dimensão mais interna (5ª dim) possui 4 elementos, a 4ª dim possui 1 elemento que é o vetor, a 3ª dim possui 1 elemento que é a matriz com o vetor, a 2ª dim possui 1 elemento que é o array 3D e O primeiro dim possui 1 elemento que é um array 4D.


''' 