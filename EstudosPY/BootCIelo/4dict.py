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