cont_quadrados = [num**2 for num in range(1,11)]
print(cont_quadrados)

#Divisiveis por 2, no intervalo de entre 1 à 20:
#Condicionais de Compreensão:
divisiveis_por2 = [num for num in range(1,21) if num % 2 == 0]
print(divisiveis_por2)