"""jogador ={
    "nome": "Zico",
    "idade": 76,
    "Nacionalidade": "Brasileiro",
    "Profissão": "Jogador De Futebol",
    "Clubes": ["Flamengo", "Udinese", "Cachíma Antless"],
    "gols": 376,
    "Número": 10
}

#Acessando valores do dicionario

#nome
print(jogador["nome"])
#idade
print(jogador["idade"])
#Profissão
print(jogador['Profissão'])

#Trasformando tuplas e listas em dicionario

#lista
lista_meninos= [["Rafael", 10], ["Gabriel", 13], ["Pedro", 15]]
dicio_nomes1 = dict(lista_meninos)

#Tuplas 
tuplas_meninas = (("Maria", 11),("Bruna",14),("Winny",12))
dicio_nomes2 = dict(tuplas_meninas)

print(dicio_nomes1, dicio_nomes2)

#Trasformando em dicionario com listas separadas, utilizando o metodo zip(chave, valor)
nomes = ['Carlos',"Vanessa","Miguel"]
idades = [13,23,36]
dicio_pessoas= dict(zip(nomes,idades))

print(dicio_pessoas)

#Atribuindo valores em dicionários

dicio_clubs = {"nome1": "Flamengo", 
               "nome2": "Vasco",
               "nome3": "Fluminense",
               "nome4": "Botafogo",}

# Atribuindo valores com as chaves novas e passando os valores
dicio_clubs["nome5"] =  "Real Madrid"
dicio_clubs ["nome6"]= "Barcelona"
print(dicio_clubs)

#Pecorrendo dicionarios
for club in dicio_clubs:
    print(club)

#verificando existência de uma chave:
if "Palmeiras" in dicio_clubs:
    dicio_clubs["nome8"].append("palmeiras")
else:
    dicio_clubs["nome8"] = ["Palmeiras"]
print(dicio_clubs)

#get
print(f"Existe Corinthians: {dicio_clubs.get('Corinthians')}")
print(dicio_clubs)"""

#Setdefault
dicio_alunos = {'nome1': "Pedro", "idade1": 23, 'nome2':"Miguel", "idade2": 43,'nome3':"Pablo", "idade3": 29 }
novo_aluno = dicio_alunos.setdefault("nome4","Guilherme")
novo_aluno = dicio_alunos.setdefault("idade4",24)
print(dicio_alunos)

#Copy

"""Se você deseja obter todas as chaves de um dicionário, use o método keys():

1
2
3
computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250bg'}

print(computador.keys())
A saída é um objeto do tipo dict_keys que equivale a uma lista com todas as chaves:

dict_keys(['CPU', 'RAM', 'SSD'])
Para obter apenas os valores das chaves em seu dicionário:

1
2
3
notas = {'Mat': 5, 'Por': 7, 'His': 8}

print(notas.values())
A saída será uma lista com os valores de cada chave:


frutas = {'pera': 10, 'uva': 2, 'maça': 55}

print(frutas.items())

O método update() tanto pode criar, como atualizar dados:

1
2
3
4
5
6
7
8
9
10
dicio = {'nome': 'Erick'}

# Atualiza o elemento de chave 'nome'
dicio.update({'nome':'Matheus'})

# Cria os elementos de chave 'idade' e 'tamanho'
dicio.update({'idade':18})
dicio.update(tamanho=1.60)

print(dicio)

Excluindo elementos no dicionário
Você pode excluir um elemento do dicionário com a keyword del do Python, especificando sua chave:

1
2
3
4
5
pessoa = {'nome': 'Matheus', 'idade': 18, 'tamanho': 1.60}

del pessoa['tamanho']

print(pessoa)
Resultando na exclusão do dado especificado:

{'nome': 'Matheus', 'idade': 18}
Excluindo e retornando o elemento excluído
O método pop() remove o item cujo a chave foi especificada:

1
2
3
4
5
6
sacola = {'maça': 2, 'ovos': 6, 'farinha': 2}

ovos = sacola.pop('ovos')

print(ovos)
print(sacola)

"""