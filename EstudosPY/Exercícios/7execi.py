"""Exercício 1: 

Crie uma string chamada frase contendo uma frase de sua escolha. Use slicing para extrair apenas as três últimas palavras da frase e imprima o resultado."""

frases = "EU, ESTOU ADORANDO ESTUDAR PYTHON"
print(frases[10:35])

"""Exercício 2:

Crie uma tupla chamada dados contendo informações de um usuário, como nome, idade e email. Desempacote os elementos da tupla em três variáveis chamadas nome, idade e email e imprima cada uma delas."""

tupla_de_usuario = ("Guilherme", 24, "felipeguilherme@xxxx.com")
nome,idade, email = tupla_de_usuario
print(nome)
print(idade)
print(email)