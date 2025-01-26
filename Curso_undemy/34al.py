"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

lista = [1, 2, 3]
lista.append(4)
print(lista)

lista.insert(0, 'i')
print(lista)

lista.pop()
print(lista)

del lista[0]   
print(lista)

lista.extend([4, 5, 6])
print(lista)

lista2 = [12,33,40]
new_list = lista + lista2
print(new_list)


for i in lista:
    print(i)
