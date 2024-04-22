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

