import numpy as np

vetor = np.array([1,2,3,4])
print(vetor)

# Ver tipo de um ndarray
# <class 'numpy.ndarray'
print(type(vetor))

# Podemos criar uma tabela com duas dimenssões
tabela = np.array([[2,3], [4,5]])
print(tabela)

#Matemáticamente como temos um objeto de 3 ou mais dimensões nós chamamos de tensor
#dimenssões: [1,2], [3,3]
matriz = np.array([[43,35], [29, 4], [81, 3]])
print(matriz)

# Tensor nada mais é que duas tabelas:
tensor = np.array([[2,3], [5,7], [0,3], [9,4]])
print(tensor)

# Utilizando método copy para não alterar o valor das dimensões da array
#O método copy() copia todos os valores do array para um novo endereço de memória.

a = np.array([[5,2, 3,1]])
b = a.copy
print(a, b)
variavel =+1
print(variavel)