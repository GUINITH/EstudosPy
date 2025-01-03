#  slicing de string

# Exemplos:
'''
012345678
Ola mundo 
-987654321
Fatiamento [i:f:p] [start:stop:step]
Obs.: a funcao len retorna o comprimento da string, que é a quantidade de caracteres
Ex.: len('Ola mundo') = 10


'''
variavel = 'Ola mundo'
print(variavel[0:4])
print(variavel[0:4:2])
print(variavel[-1:-10:-1])

print(len(variavel))