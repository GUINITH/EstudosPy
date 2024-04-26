# Limpando Células vazias

# Células Vazias
''' 
Células vazias podem potencialmente fornecer um resultado errado quando você analisa dados.
'''
# Remover linhas
''' 
Uma maneira de lidar com células vazias é remover linhas que contêm células vazias.

Isso geralmente é Ok, já que os conjuntos de dados podem ser muito grandes e 
remover algumas linhas não terá grande impacto no resultado.

''' 
import pandas as pd 
# Criando DataFrame
dados = {
    'nomes': ['Rafael', 'Carlos', 'Rick', 'Taís', 'Marcia' , 'Maria'],
    'idades': [17,16,15,14,18,None],
    'turma': [301,201,101,101,301,None]
}
df_alunos = pd.DataFrame(dados)
print(df_alunos)

''' 
Saída:
  nomes  idades  turma
0  Rafael    17.0  301.0
1  Carlos    16.0  201.0
2    Rick    15.0  101.0
3    Taís    14.0  101.0
4  Marcia    18.0  301.0
5   Maria     NaN    NaN
'''

# Retornar um novo Data frame sem células vazias:
new_df = df_alunos.dropna()
#print(new_df)

''' 
saída:

0  Rafael    17.0  301.0
1  Carlos    16.0  201.0
2    Rick    15.0  101.0
3    Taís    14.0  101.0
4  Marcia    18.0  301.0

''' 
# Note que por padrão, o método retorna um novo DataFrame e não alterá o original:  .dropna()

''' 
Se você quiser alterar o Datraframe Original

Use o argumento: inplace = True
'''
# Adicionando uma coluna e algumas linhas
df_alunos['Cursos Técnicos'] = ['Desenvolvedor', 'Cuidador', 'Pintor', 'Enfermeira','Professora', None]
print(df_alunos)

# Remova todas as linhas com valores Null
#df_alunos.dropna(inplace=True)
#print(df_alunos.to_string())

# Note: Agora, o não retornará um novo DataFrame, mas removerá todas as linhas que contêm valores Null do DataFrame original .dropna(inplace=True)


# Substituir Valores Vazios:

''' 
Outra maneira de lidar com células vazias é inserir um novo valor.

Dessa forma, você não precisa excluir linhas inteiras apenas por causa de algumas cazias Células>.

O método nos permite substituir vazios células com um valor: fillna()


''' 

# Subistitua os valores Null pelo número: 19
#df_alunos.fillna(19, inplace=True)
#print(df_alunos)

''' 
saída:

    nomes  idades  turma Cursos Técnicos
0  Rafael    17.0  301.0   Desenvolvedor
1  Carlos    16.0  201.0        Cuidador
2    Rick    15.0  101.0          Pintor
3    Taís    14.0  101.0      Enfermeira
4  Marcia    18.0  301.0      Professora
5   Maria    19.0   19.0              19

''' 
# Subistituir somente para colunas especificadas:

''' 
O exemplo acima substitui todas as células vazias em todo Data Frame.

Para substituir apenas valores vaios para uma coluna, especifique o nome da coluna para o DataFrame:

'''

# Subistitua os valores Null nas colunas 'idades','turma','Cursos Técnicos':

#df_alunos['idades'].fillna(19, inplace=True)
#df_alunos['turma'].fillna(300, inplace=True)
#df_alunos['Cursos Técnicos'].fillna('Designer', inplace=True)
#print(df_alunos)

''' 
Saída: 

    nomes  idades  turma Cursos Técnicos
0  Rafael    17.0  301.0   Desenvolvedor
1  Carlos    16.0  201.0        Cuidador
2    Rick    15.0  101.0          Pintor
3    Taís    14.0  101.0      Enfermeira
4  Marcia    18.0  301.0      Professora
5   Maria    19.0  300.0        Designer
''' 

# Subistituir usando média, mediana ou moda 

''' 
Uma maneira comum de substituir células vazias, é calcular o valor médio, mediano ou moda da coluna.

Pandas usa os métodos e para Calcular os respectivos valores para uma coluna especificada: mean(), median() e mode()
''' 

# Calcule a média e substitua quaisquer valores vazios por ela:
média = df_alunos['idades'].mean()
df_alunos.fillna(média, inplace=True)
print(df_alunos)
