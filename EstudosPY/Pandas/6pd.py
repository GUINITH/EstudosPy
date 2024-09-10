# Pandas - Analisando DataFrames

import pandas as pd
'''
 Exibindo os dados:

 Um dos métodos mais usados para obter uma visão geral do DataFrame, é o método.head()

 O método retorna os cabeçalhos e um número especificado de linhas, começando pela parte superior.head()

'''

# Imprima o seu dataframe da linha 0 até 7:

alunos_dict = {
    'nomes': ['Rafael', 'Miguel', 'Maria', 'Janine', 'Suellem', 'Mário', 'Roberto', 'Carlos','Stella', 'Pâmela'],
    'idades': [23,27,18,20,21,24,18,19,22,25]
}

df_alunos = pd.DataFrame(alunos_dict)
print(df_alunos.head(8))

# Se o número de linhas não for especificados, o método retornará as 5 primeiras linhas. head()

# Imprima as 5 primeiras linhas
print(df_alunos.head())
'''
 Há também o método para imprimir as 5 últimas linhas do DataFrame. tail()
 
 O método retorna os cabeçalhos e um número especificado de linhas, começando pela parte inferior. tail()

'''
# imprima as últimas 5 linhas do Dataframe:
print(df_alunos.tail())

''' 
Informações sobre os dados

O objeto Dataframes tem um método chamado, que dá-lhe mais informações sobre o conjunto de dados. info()

'''
# Imprima informações sobre os dados:
print(df_alunos.info())

"""
- Abaixo temos o tipo de dados e como sabemos o comando que utilizamos para ver o tipo é type()
<class 'pandas.core.frame.DataFrame'>

- O resultado nos diz que são 10 linhas de 0 a 9 e duas colunas.
RangeIndex: 10 entries, 0 to 9
Data columns (total 2 columns):


- E o nome de cada coluna, com o tipo de dados
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   nomes   10 non-null     object
 1   idades  10 non-null     int64
dtypes: int64(1), object(1)
memory usage: 292.0+ bytes
None

"""

# Valores Nulos

# O método também apresenta quantos valores não-nulos estão presentes em cada coluna, e em nosso conjunto de dados parece que há 10 valores  não-nulos em cada coluna.

# Valores vazios, ou valores nulos, podem ser inválidos ao analisar dados, e você deve considerar a remoção de linhas com valores vazios. Este é um passo em direção ao que é chamado de limpeza de dados.