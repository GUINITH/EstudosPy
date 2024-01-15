## Variáveis
"""
Variáveis são pequenos espaços de memória que separamos para armazenar um dado, que em seguida poderá ser acessado através de identificador único em nosso código.s


# 1. Variáveis

my_var = "Sheldom" # Criando uma Variável

# 2. Exiba o Conteúdo da Variável
print(my_var) # Saída: Sheldom, tipo: string

idade = 24 #Saída: 24, tipo int
print(idade)

Peso = 135.5 # Saída: 135.5, tipo float
print(Peso)

Estudando = True
Nao_estudando = False

print(Estudando ) # Saída: True, tipo booleano
print(Nao_estudando ) # Saída: False, tipo booleano

#3 Exiba os tipos das variáveis
print(type(my_var)) #String
print(type(idade)) #Int
print(type(Peso)) #Float
print(type(Estudando)) #Bool
print(type(Nao_estudando)) #Bool
"""
# Obtenha dados do úsuario, crie 3 variáveis, uma para guardar o nome, altura e peso do úsuario e exiba no terminal
""""name_user = str(input("Qual seu nome ?: "))
user_age = int(input("Qual sua idade ?: "))
user_peso = float(input("Qual seu peso ?:  "))

print(f"Bem-vindo {name_user}, você tem {user_age} anos e pesa {user_peso} kg.")
"""

"""idade = int(input("Digite sua idade: "))

while idade < 7:
    print(f"Você é criança, sua idade é {idade} anos")

print("Obrigado!")
"""

idade = int(input('Digite a idade: '))
 
while idade < 0 or idade > 150:
  print('Erro! Idade deve estar entre 0 e 150!')
  idade = int(input('Digite a idade: '))
 
print('Obrigado!')