# Desempacotamento de cargos 

lista_nomes = [['Lais', 'Pablo', 'marcia', 'pedro'], ['Flamengo', 'Vasco', 'Fluminense', 'Botafogo']]

# desempacotamento normal 
nome1, nome2= lista_nomes
print(nome1)
print(nome2)

# desempacotamento com for 
for nomes in lista_nomes:
    for nome in nomes:
        print(nome)


# desempacotamento de cargos 
print(*lista_nomes, sep= '\n')