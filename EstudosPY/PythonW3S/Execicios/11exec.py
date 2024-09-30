# Exercício 1: Criando uma Lista de Números Pares
# Crie uma lista chamada `numeros_pares` que contenha todos os números pares de 1 a 20.
# Imprima a lista resultante.

numeros_pares = list(range(2,21,2))
print(numeros_pares)

minha_lista = list(range(1,11))
print(minha_lista)
# Exercício 2: Soma dos Elementos de uma Lista
# Crie uma função chamada `soma_lista` que receba uma lista de números como parâmetro 
# e retorne a soma de todos os elementos da lista.
# Teste a função com a lista `[1, 2, 3, 4, 5]`.

numeros = [1,2,3,4]
def soma_lista(lista = numeros):
    somar_numeros = sum(lista)
    return somar_numeros
    
printar_Lista = soma_lista()
print(printar_Lista)


# Exercício 3: Dicionário de Frutas
# Crie um dicionário chamado `frutas` que mapeia o nome de uma fruta (como string) para 
# o seu preço por quilo (como float). Adicione pelo menos três frutas ao dicionário.
# Imprima o dicionário resultante.

frutas = {
    'fruta1': 'Maçã', 
    'preço': 14.50,
    'fruta2': 'Uva', 
    'preço': 5.50,
}
frutas.update({'fruta3': 'Pera', 'preço': 43.00})
print(frutas)
# Exercício 4: Filtrando Números Maiores que 10
# Crie uma função chamada `filtrar_maiores` que receba uma lista de números e retorne uma 
# nova lista contendo apenas os números maiores que 10.
# Teste a função com a lista `[5, 15, 3, 12, 7, 25]`.


def filtrar_numeros(numeros):
    return numeros > 10

lista_numeros = [11,22,3,44] 
resultado = list(filter(filtrar_numeros, lista_numeros))
print(resultado)

# Exercício 5: Contagem de Vogais em uma String
# Crie uma função chamada `contar_vogais` que receba uma string e retorne o número de 
# vogais (a, e, i, o, u) na string.
# Teste a função com a string "Python é incrível!".

def contar_vogais(palavra: str):
    vogais = ['aeiou']
    contador = {}
    palavra.lower()
    for vogal in vogais:
        if vogal in palavra:
            contador[vogal] = palavra.count(vogal)
    return len(contador)

minha_palavra = 'aeiou'
print(contar_vogais(minha_palavra))

# Exercício 6: Verificação de Palíndromo
# Crie uma função chamada `e_palindromo` que verifique se uma string é um palíndromo.
# Uma string é considerada um palíndromo se ela ler o mesmo de trás para frente.
# Teste a função com as strings "radar" e "python".

# Exercício 7: Fatorial de um Número
# Crie uma função chamada `fatorial` que calcule o fatorial de um número inteiro.
# Teste a função com o número 5.

# Exercício 8: Números Perfeitos
# Crie uma função chamada `e_numero_perfeito` que verifique se um número é perfeito.
# Um número é considerado perfeito se a soma de seus divisores próprios (excluindo ele mesmo)
# for igual ao próprio número.
# Teste a função com os números 6 e 28.

# Exercício 9: Média de Valores em um Dicionário
# Crie uma função chamada `media_dicionario` que receba um dicionário onde as chaves são 
# strings e os valores são números. A função deve retornar a média dos valores.
# Teste a função com o dicionário `{"a": 10, "b": 20, "c": 30}`.

def media_de_valores(values: dict): 
    total_values = sum(values.values())
    compre_velues = len(values.values())
    media_velues = total_values / compre_velues
    return media_velues

dic_values = {"a": 10, "b": 20, "c": 30}
print('valor é:', media_de_valores(dic_values))

# Exercício 10: Classificação de Idades
# Crie uma função chamada `classificar_idade` que receba uma idade como parâmetro e retorne 
# uma string que classifique a pessoa como "criança" (idade < 12), "adolescente" (12 <= idade < 18), 
# "adulto" (idade >= 18), ou "idoso" (idade >= 65).
# Teste a função com as idades 8, 15, 25, e 70.


def classificar_idade(idade):
    if idade < 12: 
        return 'Você é uma criânça'
    elif 12 <= idade < 18:
        return 'você é um adolecente'
    elif 50 == idade < 65:
        return 'você'
    else:
        return 'Você é muito idoso'
 

minha_idade = classificar_idade(40)
print(minha_idade)