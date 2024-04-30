# Pandas - Limpeza de Dados de Formato Incorreto:

# Dados de Formato errado

''' 
Células com dados de formato errado podem dificultar, ou mesmo impossibilitar, a análise de daddos.

Parra corrgi-lo, você tem duas opções: remover as linhas ou converter todas as células no colunas no mesmo formato. 


''' 

# Converter em um formato correto
''' 
Em nosso Data Frame, temos duas células com o formato errado. Confira a linha 22 e 26, a coluna 'Data' deve ser uma cadeia de caracteres que representa um data:
''' 

dados = {
'Duração':[60,60,60,60,60,60,60,450,30],
'Data':['01/12/2020','02/12/2020', '03/12/2020', '2020/12/04','05/12/2020','2020/12/06','2020/12/07', '2020/12/08', None ], 
'Pulso': [110,117,103,109,117,102,110,104,109,98], 
'Pulso Max': [130,145,135,175,148,127,136,134,133],
'Calorias':[409.1,479.0,340.0,282.4,None,323.0,243.0,364.2,None]}

import pandas as pd
df1= pd.DataFrame(dados)
print(df1)