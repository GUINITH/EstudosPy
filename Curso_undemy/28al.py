"""
while: Estrutura de Repetição

while condicao:

break: Parar o loop
continue: Pular para o proximo loop
"""
contador = 1 
while contador <= 5:
    print(contador)
    contador +=1


#break 
contador = 1 
while contador <= 5:
    print(contador)
    if contador == 3:
        print("Parei no 3 porque e maior que 3")
        break
    contador +=1

#continue
"""
while contador <= 5:
    contador +=1
    if contador == 3:
        print("Pulei o 3")
        continue 
    else:
        contador ==4
        break
print(contador)    
    
""" 