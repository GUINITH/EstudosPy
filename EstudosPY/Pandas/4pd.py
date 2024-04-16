import pandas as pd

# Carregando arquivos em um DataFrame
'''
- Nesse tópico vamos aprender a carregar arquivos em um DataFrame

- Imagine se seus conjuntos de dados estiverem armazenados em um arquivo, o Pandas poderá carregá-los em um DataFrame.

A maneira mais comum de carregar arquivos em um DF é:

df = pd.read_csv('test.csv')
print(df)

'''

# Ler Arquivos CSV

'''
Um maneira simples de armazenar conjuntos de big data é usar arquivos CSV (separados por vírgulas arquivos).

Arquivos CSV contém texto simples e é um formato bem conhecido que pode ser lido por todos, incluindo Pandas.

Em nossos exemplos, usaremos um arquivo CSV chamado 'test.csv'

'''
# Carregue o CSV em um Dataframe:

df_test = pd.read_csv('test.csv')
print(df_test.to_string())

# Dica: Uso para imprimir o todo DataFra,e.to_string()

# Se você tiver um  DataFrame grade com muiitas linhas, o Pandas retornará apenas as primeiras 5 linhas e as últimas 5 linhas:


# Imprima o DataFrame sem o método: to_string()
print(df_test)



'''
Max_rows

- O número de linhas retornadas é definido nas configurações da opção Pandas.
- Você pode verificar as linhas máximas do seu sistema com a instrução.pd.options.display.max_rows

'''

# Verifique o número máximo de linhas retornadas: 
print(pd.options.display.max_rows)

'''
No meu sistema contém 60 linhas o que significa que se o DataFrame contiver mais de 60 linhaas, a instrução retornará apenas os cabeçalhos e a primeira e as útimas 5 linhas.

Você pode alterar o número máximo de linhas com a mesma instrução.
'''

# Aumente o número máximo de linhas para exibir o DataFrame inteiro:
pd.options.display.max_rows= 1000
print(df_test)
