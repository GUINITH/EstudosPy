# Precedência de Operadores

# Precedência de Operadores

# Os operadores com a mesma precedência são avaliados da esquerda para a direita.
# Os operadores com precedência diferente serão avaliados da esquerda para a direita.

# Exemplos: 

print(10 + 5 * 2) # 20
print((10 + 5) * 2) # 40    
print(10 * 2 + 5) # 25
print(10 * (2 + 5)) # 50

# 1. () 
#2 **
#3 *, /, //, % 
#4 +, -

account = (1+1) ** (5+5)
print(account)