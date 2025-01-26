"""
Tuplas - uma lista imutável
"""

numeros = (1, 2, 3, 4, 5)
print(numeros)
print(type(numeros))

# enumerate: retorna uma tupla com a contagem e o elemento
for i, num in enumerate(numeros):
    print(i, num)