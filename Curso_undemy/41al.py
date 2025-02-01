# Listas sobre listas 
# Podemos ter listas dentro de listas 
# Acessar valores dentro delas. 
lista_numeros = [[1,2,3 ],[4,5,6],[7,8,9]]
print(lista_numeros[0][2]) # 3

for numero in lista_numeros:
    print(numero)
    for num in numero:
        print(num)