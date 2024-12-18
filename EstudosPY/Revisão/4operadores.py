# Operadores em Python: 
# Aritméticos, 
# atribuição, 
# comparação, 
# lógicos, 
# identidade
# associação

# Aritméticos: 
# + adição,
#  - subtração, 
# * multiplicação, 
# / divisão real, 
# ** potência, 
# // divisão inteira, 
#  % resto de divisão

soma = 1 + 11 
print(soma)

subtracao = 22 - 15 
print(subtracao)

multi = 34 * 18 
print(multi)

div_float = 23 / 13 
print(div_float) 

potencia = 2** 10 
print(potencia)
div_int = 40 // 4 
print(div_int)

resto = 10 % 5 
print(resto)

# Atribuição: 
"""
= operador de atribuição
+= operador de atribui e soma
-= operador de atribui e subtrai 
*= operador que atribui e multiplica 
/= operador que atribui e divide real
**= operador que atribui e potência
/= operador que atribui e divide inteiro
%= operador que atribui e modula o resto da divisão

"""
atribuition = 12
print(atribuition)

atribuition += 10 
print(atribuition)

atribuition -= 11
print(atribuition)

atribuition *= 22 
print(atribuition)

atribuition /= 10 
print(atribuition)

atribuition **= 12 
print(atribuition)

atribuition //= 10 
print(atribuition)

atribuition %= 10 
print(atribuition)



# Comparação

"""
> maior que 
< menor que
>= maior ou igual que
<= menor ou igual que
== igual a 
!= diferente de 
"""
numero_maior = 10 > 5 
print(numero_maior)

numero_menor = 10 < 20 
print(numero_menor)

maior_ou_igual = 15 >= 10 
print(maior_ou_igual)

menor_ou_igual = 12 <= 5
print(menor_ou_igual)

igual = 12 == 19 
print(igual)

diferente = 22 != 30 
print(diferente)


# Lógicos: 
# and: e, ambas condições precisam ser verdadeiras, caso contrário é falso
# or: ou, uma ou as duas condições precisam ser verdadeiras, caso contrário é falso
# negacão: not inverte a condições

num1 = 22 
num2 = 13 

comparacao_and = num1 and num2 > 10
print(comparacao_and)

comparacao_or = num1 or  num2 < 50
print(comparacao_or)

comparacao_not = not num1 > num2 
print(comparacao_not)


# identidade:
# is 
# is not  

nome = 'Fernanda'
alunos = ['Mirela', 'Miguel', 'Pedro', 'Fernanda']

checar_nome = nome is alunos 
print(checar_nome)

num3 = 5 
numeros = list(range(1,5))
checar_num = num3 is not numeros
print(checar_num)


# associação: 
# in, 
# in not

name_user = 'Manoel' 

for nome in ['Pedro', 'Rafael', 'Guilherme']:
    print(True)

alunos = ['Pedro', 'Rafael', 'Guilherme']
if 'Manoel' not in alunos: 
    print('Ele nao e aluno')
else: 
    print('Ele é aluno!')









