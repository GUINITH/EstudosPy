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
