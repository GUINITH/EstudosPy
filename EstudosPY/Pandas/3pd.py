import pandas as pd

# DataFrames

"""
Os conjuntos de dados no Pandas, são geralmente tabelas multidimensionais, chamadas DataFrames.
Série é como uma coluna, um DataFrame é a tablea inteira.

O que é um DataFrame?

Um Pandas DataFrame é uma estrutura de dados bidimensional, 
como um array bidimensional ou uma tabela com linhas e colunas.

"""

#Crie um Dataframe simpes do Pandas:
locais = {
    'municipios': ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte'],
    'Estados': [ 'RJ', 'SP', 'MG']
}
df = pd.DataFrame(locais)
print(df)
"""
No DataFrame as chaves: 'municipios', 'Estados' viram as colunas e os valores de ambas viram as linhas, que são indexadas.

output do código acima:

index   Municipios       Estados
0       Rio De Janeiro     RJ
1       São Paulo          SP
2       Belo Horizonte     MG 

"""

# Localizar Linha

'''
Como você pode ver no resultados acima, o DataFrame é como uma tabela com linhas e colunas.
Pandas usam o loc atributo para retornar uma ou mais linhas especificadas

'''
#Retorne a primeira linha do seu DataFrame:
print(df.loc[0])
'''
Output do código acima: 
Municipios  Rio de Janeiro
Estados     RJ

Note que ele retorna uma série.
'''

# Retorne a primeira linha e a segunda linha:

print(df.loc[[0,1]])

'''
  
        Municipios       Estados
0       Rio De Janeiro     RJ
1       São Paulo          SP

Note que ao usa [], o resultado é um Pandas Dataframe
'''

# Indices Nomeados:

'''
- Com o index argumento, você pode nomear seus próprios índices. Index
'''
# Adicione uma lista de nomes para dar um nome a cada linha:

alunos = {
    'Nomes': ['Gael', 'Tayssa', 'Renner'],
    'Idades': [ 23, 30, 19] 
}
df_alunos = pd.DataFrame(alunos, index=['aluno1','aluno2', 'aluno3'])
print(df_alunos)

'''
Saída:
         Nomes  Idades      
aluno1    Gael      23      
aluno2  Tayssa      30      
aluno3  Renner      19    

'''

# Localizar Índices Nomeados

'''
Use o índice nomeado no atríbuto para retornar a(s) linha(s) especificada(s). loc
'''
# retorne a terceira linha do seu dataframe:

print(df_alunos.loc['aluno3'])

'''
saída:

Nomes     Renner
Idades        19
Name: aluno3, dtype: object 

Ele retorna uma série
'''
