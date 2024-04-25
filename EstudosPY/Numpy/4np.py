# Fatiamento de Matrizes 
''' 
Fatiar em ppython significa levar elemntos de um dado índice para outro dado índice.

Passamos fatiar em vez de índice assim: .[start:end]

Também podemos definir o passo, assim: .[start:end:step]

Se não passarmos comece o seu conderado o

Se não passarmos o fim do seu comprimento de matriz considerado nessa dimensão

Se não passarmos de passo é considerado 1


'''

# Fatie elementos do indice 1 para o indice 5 da seguinte matriz:

import numpy as np 

lista = list(range(1,8))
arr = np.array(lista)
print(arr[1:5]) #2,3,4,5

# Note que o resultado inclui o índice inicial, mas exclui o indice final

# Segmente elementos do índice 4 até o final da matriz:

print(arr[4:])

# Elementos de fatia do inicio ao indice 4 (não incluídos):
print(arr[:4])


# Fatiamento Negativo

'''
Use o operador de subtração para fazer referência a um índice do final:
'''

# Fatia do indice 3 do final para o índice 1 do final:

print(arr[-3:-1])

# Passo

'''
Use o valor para determinar a etapa da fatia: step

'''

# Retorne todos os outros elementos do indice 1 para o índice 5:
print(arr[1:5:2])

# Retorne todos os outros elementos de toda a matriz:
print(arr[::2])

# Fatiamento Matrizes 2D

''' 
A ppartir do segundo elemento, fatie elementos do índice 1 para o índice 4(não incluído):
'''
arr1 = np.array([[list(range(1,6))], [list(range(6,11))]])
print(arr1[1, 1:4])

# Lembre-se que o segundo elemento tem índice 1.

# De ambos os elementos, índice de retorno 2:
print(arr1[0:2, 1:2])

# De ambos os elementos, índice de fatia 1 para índice 4(não incluído), isso retornará uma matriz 2d:
print(arr1[0:2, 1:4])

# Exercícios

''' 
Insira a sintaxe de slicing correta para imprimir a seguinte seleção da matriz:

Tudo, desde (incluindo) o segundo item até (não incluíndo) o quinto item.
'''
lista = list(range(10,41,5))
arr = np.array(lista)
print(arr[1:5]) #15,20,25,30