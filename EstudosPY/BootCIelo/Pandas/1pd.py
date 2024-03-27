#Pandas

# Importanod a biblioteca pandas
import pandas as pd
import numpy as np

#Verificando versão
print(pd.__version__)

# criando uma Serie pd.Series()
lista = [1,2,3,4,5,6]
my_serie = pd.Series(lista)
print(my_serie)

# Acessando minha Serie pelo index
print(my_serie[0])

#Definindo uma array com numpy
num = [23,5,67,8]
arr = np.array(num)
print(arr)

#Serie
serie = pd.Series(num)
print(serie)

# Outra forma de acessando os valores
print(serie.values)