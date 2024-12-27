"""
Variáveis:  Variaveis são containers usados para salvar algo na mémoria do computador.
PEP8: Inicie variáveis com letras minúsculas, pode ser números e underline -.
O sinal de = é o operador de  atribuição. Ele é usado para atribuir um  valor a uma  variável
uso: nome_variavel = expressao
"""
nome_completo = 'Guilherme Felipe Dos Santos'
soma_dois_mais_dois = 2 + 2
print(nome_completo, soma_dois_mais_dois) # Guilherme Felipe Dos Santos , # 4     

nome = 'Felipe'
idade = 25 
maior_de_idade = idade >=18
print(f'Nome: {nome}, idade: {idade} anos')
print(f'E maior de idade: {maior_de_idade}')


def maior_ou_menor(nome: str, idade: int):
    if idade >=18:
        return f'Nome: {nome}, idade: {idade} anos e sou maior de idade'
    else:
        return f'Nome: {nome}, idade: {idade} anos e sou menor de idade'



print(maior_ou_menor('Guilherme', 23))