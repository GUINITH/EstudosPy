import numpy as np 

# Primeira objeto em numpy
primary_arr = np.array([2,4,6,8])
print(primary_arr)

# verificando versão
print(np.__version__)

# Criando um objeto Numpy ndarray

"""
NumPy é usado para trabalhar com arrays. O objeto array em NumPy é chamado ndarray.

Podemos criar um ndarrayobjeto NumPy usando a array()função.

"""
#Verificando o tipo de dados
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# type(): esta função interna do Python nos informa o tipo do objeto passado para ela. Como no código acima, mostra que arré numpy.ndarraydo tipo.


"""
Para criar um ndarray, podemos passar uma lista, tupla ou qualquer objeto semelhante a um array para o array() método, e ele será convertido em um ndarray:

"""
# array de tupla
arr_tuple = np.array((21,31,44,55,89))
print(arr_tuple)

#Array de dicionário:
arr_dict = np.array({'num1': 1, "num2": 2, "num3": 3, "num4": 4})
print(arr_dict)