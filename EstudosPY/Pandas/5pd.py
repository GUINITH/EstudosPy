import pandas as pd
# Ler JSON

'''
Os conjuntos de big data geralmente são armazenados ou extraídos como JSON.

JSON é texto siomples, mas tem o formato de um objetivo, e é bem conhecido no mundo da programação, incluindo Pandas.

Em nossos exemplos, usaremos um arquivo JSON chamado 'test.json'.

'''
# Exmplo

# Carregue um arquivo JSON em um DataFrame:
'''
df_json = pd.read_json('test.json')
print(df.to_string())
'''
# Dica use para imprimir todo o DataFrame a função: to_string()

"""
Dicionário como JSON

 JSON = Dicionário Python

 Os objetos Json têm o mesmo formato que os dicionários Python

"""


# Digamos que seu código Json não estiver em um arquivo, mas em um dicionário Python, você poderá carregá-lo em um DataFrame diretamente:

# Carregue um dicionário Python em um Dataframe:

times = {
    'Time1': {
    'nome':'Flamengo', 
    'cores': 'Rubro-Negro'
    },
    'Time2': {
    'nome':'Fluminense', 
    'cores': 'Tricolor'
    },
    'Time3': {
    'nome':'Vasco', 
    'cores': 'Alvi-Negro Cruzmaltino'
    },
    'Time4': {
    'nome':'Botafogo', 
    'cores': 'Alvi-Negro'
    },
}

df = pd.DataFrame(times)
print(df)

