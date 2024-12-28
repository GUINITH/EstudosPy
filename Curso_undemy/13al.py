# F-strings: Interpolação de Strings

nome = 'Guilherme'
idade = 25
altura = 1.80

print(f'{nome} tem {idade} anos e {altura} de altura')

# formatação de strings com f-strings
print(f'{nome} tem {idade} anos e {altura:.2f} de altura')

# formatando strings com format 
print('{} tem {} anos e {:.2f} de altura'.format(nome, idade, altura))
