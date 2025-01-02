#Operadores in not in

# in: retorna True se o item estiver na lista 
# not in: retorna True se o item nao estiver na lista

lista = [1,2,3,4,5,6,7,8,9,10]
print(4 in lista)
print(20 not in lista)

numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')