# Operador Lógicos: and, or, not 
# Operadores lógicos, também conhecidos como conjunção lógica e disjunção lógica, servem para combinar expressões lógicas. Returnando algum dado booleano como True ou False.

# and: verdadeiro apenas se ambas as condições forem verdadeiras
# or: falso apenas se ambas as condições forem falsas
# not: inverte a expressão original

# avaliação de curto circuito
print(True and True) # True
print(True and False) # False
print(True or True) # True
print(True or False) # True
print(not True) # False
print(not False) # True

# and 
idade = int(input('Digite sua idade: '))

if idade >= 18 and idade <= 65:
    print('Você é de Maior! ')
else:
    print('Você é de Menor! ')


#or    
entrada = input('Deseja entrar no jogo? (S/N) ')

if entrada == 'S' or entrada == 's':
    print('Vamos la')
elif entrada == 'N' or entrada == 'n':
    print('Volte quando quiser')
else:
    print('Resposta inválida, digite apenas s para sim ou n para não')


# not
altura = input('Qual sua altura?')
if not altura:
    print('Você não digitou nada')
else:
    print(f'Sua altura é: {altura}')