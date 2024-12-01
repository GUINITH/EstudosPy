# Tipo de dados: strings, inteiros, floates, booleanos e complexos


# Tipos de dados primitivos
# Strings  - textos
# Integer - inteiros
# Floats  - reais
# Boolean - Verdadeiro ou Falso

meu_txt = 'Olá, mundo!'
print(type(meu_txt))

meu_int= 10
print(type(meu_int))

meu_float = 10.5
print(type(meu_float))

meu_bool = True
print(type(meu_bool))

# Tipos de dados complexos
# Listas
# Tuplas
# Dicionários
# Conjuntos

minha_lista = [1,2,3]
print(type(minha_lista)) 

minh_tupla = (1,2,3)
print(type(minh_tupla))

meu_dict = {'chave1': 'valor1', 'chave2': 'valor2'}
print(type(meu_dict))

meu_set = {1,2,3}
print(type(meu_set))


# conversão de dados 

convert_str = str(10)
print(convert_str)

convert_int = int('10')
print(convert_int)

convert_float = float(10)
print(convert_float)

convert_bool = bool(10)
print(convert_bool)

convert_list = list('Ola Mundo')
print(convert_list)

convert_tuple = tuple('Ola Mundo')
print(convert_tuple)

convert_dict = dict(enumerate('Ola Mundo'))
print(convert_dict)

convert_set = set('Ola Mundo')
print(convert_set)
