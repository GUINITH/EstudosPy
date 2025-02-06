"""
args - Argumentos não nomeados 

*arg* (empacotamento e desempacotamento)


"""

def numeros(*args):
    soma = 0 
    for num in args:
        soma += num
    return  soma

print(numeros(1,2,3,4,5,6)) # 21 