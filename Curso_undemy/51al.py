# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def mult(*args):
    multiplicar = 1
    total = 0 
    for num in args:
        multiplicar *= num 
        total = multiplicar
    return total

print(mult(2,33,12))





# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if numero % 2 ==0:
        return 'par'
    else:
        return 'ímpar'

print(par_impar(10)) # par