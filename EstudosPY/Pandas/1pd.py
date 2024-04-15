
# Primeiros passos no Pandas

# Instalação: pip install pandas 

#Importação:
import pandas as pd 

primary_dataset = {
    'alunos': ['Gabriel', 'Michelle', 'Rafaele'],
    'Idade': [14,13,12]
}
df1 = pd.DataFrame(primary_dataset)
print(df1)

#Verificando a versão  do Pandas:
print(pd.__version__)

