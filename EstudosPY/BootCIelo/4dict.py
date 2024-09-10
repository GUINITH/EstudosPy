
jogador ={
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
               "nome4": "Botafogo"}

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
<<<<<<< HEAD
dicio_clubs.get("Corinthians")
    
nomes = [ "Rafael","Pedro","Marcia"]
idades = [43,22,33]

dicio_nomes =dict(zip(nomes, idades))
#Verifica se existe uma chave no dicionário
dicio_Gui = dicio_nomes.get("Guilherme")
print(f'Existe, "Guilherme" no dicionário{dicio_nomes}: {dicio_Gui}')
#SetDefault verifica se tiver um valor, se sim ele retorna chave e valor, se não ele adiciona ao dicionário.
dicio_Gui = dicio_nomes.setdefault("Guilherme",24)
print(f'Existe, "Guilherme" no dicionário{dicio_nomes}')

#Função copy, copia um dicionário, para evitar duas ou mais dicionários referênciar o mesmo dicionário.
dicio_alunos = dicio_nomes.copy()
print(dicio_alunos)

#Update: Serve para upar uma lista na outra;
dicio_familia = {}
dicio_familia.update(dicio_nomes)
print(dicio_familia)

"""print(dicio_familia.items())"""
=======
print(f"Existe Corinthians: {dicio_clubs.get('Corinthians')}")
print(dicio_clubs)

#Setdefault
dicio_alunos = {'nome1': "Pedro", "idade1": 23, 'nome2':"Miguel", "idade2": 43,'nome3':"Pablo", "idade3": 29 }
novo_aluno = dicio_alunos.setdefault("nome4","Guilherme")
novo_aluno = dicio_alunos.setdefault("idade4",24)
print(dicio_alunos)

#Copy

#Se você deseja obter todas as chaves de um dicionário, use o método keys():

computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250bg'}

print(computador.keys())
#A saída é um objeto do tipo dict_keys que equivale a uma lista com todas as chaves:

dict_keys(['CPU', 'RAM', 'SSD'])
#Para obter apenas os valores das chaves em seu dicionário:


notas = {'Mat': 5, 'Por': 7, 'His': 8}

print(notas.values())
#A saída será uma lista com os valores de cada chave:


frutas = {'pera': 10, 'uva': 2, 'maça': 55}

print(frutas.items())

#O método update() tanto pode criar, como atualizar dados:


dicio = {'nome': 'Erick'}

# Atualiza o elemento de chave 'nome'
dicio.update({'nome':'Matheus'})

# Cria os elementos de chave 'idade' e 'tamanho'
dicio.update({'idade':18})
dicio.update(tamanho=1.60)

print(dicio)

#Excluindo elementos no dicionário
#Você pode excluir um elemento do dicionário com a keyword del do Python, especificando sua chave:

pessoa = {'nome': 'Matheus', 'idade': 18, 'tamanho': 1.60}

del pessoa['tamanho']

print(pessoa)
#Resultando na exclusão do dado especificado:

{'nome': 'Matheus', 'idade': 18}
#Excluindo e retornando o elemento excluído
# método pop() remove o item cujo a chave foi especificada:

sacola = {'maça': 2, 'ovos': 6, 'farinha': 2}

ovos = sacola.pop('ovos')

print(ovos)
print(sacola)

#Excluindo último item
#O método popitem() também remove o último elemento do dicionário.

#Contudo, diferente do método pop() que apenas retorna o valor daquele elemento, popitem() retorna o elemento todo, contendo chave e valor.

#Veja usando o mesmo exemplo do método pop():

sacola = {'maça': 2, 'ovos': 6, 'farinha': 2}

farinha = sacola.popitem()

print(farinha)
print(sacola)
#Veja que o retorno foi uma tupla e o último item foi removido:


('farinha', 2)
{'maça': 2, 'ovos': 6}
#Limpando dicionário
#Uma maneira de esvaziar um dicionário é utilizando o método clear(), dessa forma:


dicio = {'nome': 'F9', 'motor': 'v8', 'ano': 2019}
dicio.clear()

print(dicio)
#O retorno é um dicionário vazio: {}.

#Copiando Dicionário
#Em Python, você não pode simplesmente digitar dict1 = dict2 para copiar um dicionário.

#Dessa forma você esta apenas copiando a referência do dict1 ao dict2.

#A maneira correta de criar uma cópia do dicionário é utilizando o método copy(), assim:


dicio = {"operacao": "web scraping", "dados": 250}

copia = dicio.copy()

print(copia)
print(dicio)
#Resultando na cópia exata do dicionário

{'operacao': 'web scraping', 'dados': 250}
{'operacao': 'web scraping', 'dados': 250}
#O método dict.setdefault()
#O método dict.setdefault()  

#retorna o valor da chave especificada, e, caso a chave não exista, a cria com o valor especificado.

#Vamos ao exemplo:

dicio = {'coleta': 'scrapy', 'dados': 200}

set_dados = dicio.setdefault('dados')

print(set_dados)
print(dicio)
#Como a chave dados existe, ela é retornada:

200
{'coleta': 'scrapy', 'dados': 200}
#Agora vamos adicionar apenas a chave sem valor, e outro com chave e valor:


dicio = {'coleta': 'scrapy', 'dados': 200}

set_data = dicio.setdefault('data')
set_teste = dicio.setdefault('teste', 1)

print(set_data)
print(set_teste)
print(dicio)
#A saída resulta em:


{'coleta': 'scrapy', 'dados': 200, 'data': None, 'teste': 1}
#O set_data que teve apenas atribuída uma chave, teve seu valor criado como None, enquanto set_teste teve o valor adicionado.

#Criando Dicionários a partir de lista de valores
#Com o método dict.fromkeys() é possível criar um dicionário a partir de uma lista de chaves e um valor, que será usado em todas as chaves.

#Veja o exemplo:


chaves = ['chave1', 'chave2', 'chave3']
valor = 0

dicio = dict.fromkeys(chaves , valor)


print(dicio)
>>>>>>> 3438cc20c097e81a890876753db24543bd7770ce
