# Listas 

"""
Listas são coleções de dados que aceita varios tipos de dados. 
Elas são mútaveis e indexadas.
Podemos fazer diversas operações como, adicionar item, fatiar, apagar item, selecionar pelo index.
"""


minha_lista = ['a', 1, True, 1.5]
print(minha_lista)

# adicionar item 

minha_lista.append('Novo dado')
print(minha_lista)

# selecionar item 
print(minha_lista[0])

# checar um index 
print(minha_lista.index(1.5))

# fatia lista 

print(minha_lista[0:2])

# Apagar item 

print(minha_lista.pop(4))
