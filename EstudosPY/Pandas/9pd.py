# Pandas - Limpeza de Dados de Formato Incorreto:
import pandas as pd

# Dados de Formato errado

''' 
Células com dados de formato errado podem dificultar, ou mesmo impossibilitar, a análise de daddos.

Parra corrgi-lo, você tem duas opções: remover as linhas ou converter todas as células no colunas no mesmo formato. 


''' 

# Converter em um formato correto
''' 
Em nosso Data Frame, temos duas células com o formato errado. Confira a linha 22 e 26, a coluna 'Data' deve ser uma cadeia de caracteres que representa um data:

Vamos tentar converter todas as células na coluna 'Data' em datas.

Pandas tem um método para isso: to_datetime()

import pandas as pd

data = {
    'Duration': [60, 60, 60, 45, 45, 60, 60, 450, 30, 60, 60, 60, 60, 60, 60, 60, 60, 60, 45, 60, 45, 60, 45, 60, 60, 60, 60, 60, 60, 60, 60, 60],
    'Date': ['2020/12/01', '2020/12/02', '2020/12/03', '2020/12/04', '2020/12/05', '2020/12/06', '2020/12/07', '2020/12/08', '2020/12/09', '2020/12/10', '2020/12/11', '2020/12/12', '2020/12/12', '2020/12/13', '2020/12/14', '2020/12/15', '2020/12/16', '2020/12/17', '2020/12/18', '2020/12/19', '2020/12/20', '2020/12/21', None, '2020/12/23', '2020/12/24', '2020/12/25', '2020/12/26', '2020/12/27', '2020/12/28', '2020/12/29', '2020/12/30', '2020/12/31'],
    'Pulse': [110, 117, 103, 109, 117, 102, 110, 104, 109, 98, 103, 100, 100, 106, 104, 98, 98, 100, 90, 103, 97, 108, 100, 130, 105, 102, 100, 92, 103, 100, 102, 92],
    'Maxpulse': [130, 145, 135, 175, 148, 127, 136, 134, 133, 124, 147, 120, 120, 128, 132, 123, 120, 120, 112, 123, 125, 131, 119, 101, 132, 126, 120, 118, 132, 129, 115],
    'Calories': [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3, 195.1, 269.0, 329.3, 250.7, 250.7, 345.3, 379.3, 275.0, 215.2, 300.0, None, 323.0, 243.0, 364.2, 282.0, 300.0, 246.0, 334.5, 250.0, 241.0, None, 280.0, 380.3, 243.0]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
print()

# Converte a coluna 'Date' para

- Como você pode ver o resultado, a data na linha 26 foi corrigida, mas a data vazia na linha 22 obteve um valor NAT(NOT A TIME), EM OUTRAS PALAVRAS UM VALOR VAZIO. uma maneira de lidar com valores vazios é simplesmente remover a linha inteira


'''

# Removendo linhas

# O resultado da conversão no exemplo acima nos deu um Valor NaT, que pode ser manippulado como um valor Null, e podemos remover a linha usando o método .dropna(inplace = True)
import pandas as pd
df = pd.read_csv('.\Pandas\dados.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df)