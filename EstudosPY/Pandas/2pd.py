#Série Pandas

"""
O que é uma Série?

Uma série é como uma coluna de uma tabela.

é Uma matriz unidimensional que contém dados de qualquer tipo.
"""

# crie uma série Pandas a partir de uma lista:
import pandas as pd 

num = list(range(1,5))
mySerie = pd.Series(num)
print(mySerie)

"""
Labels ou Etiquetas

Se nada mais for especificado, os valores serão rotulados com seu número de índice. O primeiro valor tem o índice 0, o segundo valor tem indice 1 etc.

Este rótulo pode ser usado para acessar um valor especificado.

"""
# Retorne o primeiro valor da Série que você criou anteriormente:
print(mySerie[0])

# Retorne o Segundo valor da Serie:
print(mySerie[1])

"""
Criar Etiquetas
Com o index argumento, você pode nomear seus próprios rótulos.

"""

# Trocando o index de números para letras. Inicialmente era: 0,1,2,3 e agora são: a,b,c,d
a = [1,2,3,4]
mySerie1 = pd.Series(a, index=['a','b','c','d'])
print(mySerie1)

# Acessando o conteúdo pelo novo index rotulado:
print(mySerie1['d'])

"""
Objetos chave/valor como série:

você tabmém pode usar um objeto chave/valor, como dicionário, ao criar uma série.

"""
# Crie uma série Pandas simples a partir de um dicionário:

cidades = {'city1': 'Rio de Janeiro', 'City2': "São Paulo", 'City3': 'Minas Gerais'}
city_serie = pd.Series(cidades)
print(city_serie)

"""
 As chaves dos dicionários se tornam os rótulos, por exemplo:

city1    Rio de Janeiro
City2         São Paulo
City3      Minas Gerais

"""
# Acessando o conteúdo pelo novo index rotulado:
print(city_serie['city1'])

"""
Para selecionar apenas alguns itens do dicionário,
use o index argumento e especifique apenas o intes que deseja incluir na Série

"""

# Creie uma série usando apenas dados de "city1" e "city2"
cidades = {'city1': 'Rio de Janeiro', 'city2': "São Paulo", 'city3': 'Minas Gerais'}
city_serie = pd.Series(cidades, index=['city1', 'city2'])
print(city_serie)


