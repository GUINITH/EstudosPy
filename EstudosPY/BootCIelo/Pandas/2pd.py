# Exercícios de Pandas

import pandas as pd
'''
df_clientes = pd.DataFrame({'ID_cliente': [1, 2, 3, 4], 'Nome': ['Ana', 'João', 'Maria', 'Pedro'], 'Idade': [25, 30, 35, 40]})
df_compras = pd.DataFrame({'ID_cliente': [1, 2, 3, 4], 'Produto': ['Celular', 'Notebook', 'Tablet', 'Smartwatch'], 'Preço': [1000, 1500, 800, 300]})
df_localizacao = pd.DataFrame({'ID_cliente': [1, 2, 3, 5], 'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília'], 'País': ['Brasil', 'Brasil', 'Brasil', 'Brasil']})


df_merge1 = pd.merge(df_clientes, df_compras, on='ID_cliente')
print(df_merge1)

df_merge2 = pd.merge(df_clientes,df_localizacao, on='ID_cliente')
print(df_merge2)


data = {
    'Produto': ['Celular', 'Notebook', 'Tablet', 'Celular', 'Notebook'],
    'Vendedor': ['Ana', 'João', 'Maria', 'Ana', 'João'],
    'Quantidade': [2, 1, 3, 2, 2],
    'Preço_Unitário': [1000, 1500, 800, 1000, 1200]
}

df_vendas = pd.DataFrame(data)

#Agrupando nome dos vendedores e somando a quantidade de vendas
df_nome = df_vendas.groupby('Vendedor')['Quantidade'].agg(func='sum')
#Agrupando nome dos produtos e a média do preço_unitário
df_calcular_media_produtos = df_vendas.groupby('Produto')['Preço_Unitário'].agg(func='mean')

'''

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'C': [10, 11, 12]})
df3 = pd.DataFrame({'B': [13, 14, 15], 'C': [16, 17, 18]})

df4 = pd.concat([df1,df2], ignore_index=True)
print(df4)
df5 = pd.concat([df1,df2,df3], axis=1)
print(df5)