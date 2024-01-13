
"""
1) Uma empresa decidiu dar um bônus de 5% ao funcionário se o seu ano de serviço for  superior a 5 anos.

Peça ao usuário seu salário e ano de serviço e imprima o valor líquido do bônus.
"""
#Solicitei o salario do úsuario
salario = float(input("Digite seu salário:"))

#Solicitei o ano de serviço de meu usuario
ano_serviço = int(input("Digite o ano que você entrou na empresa: "))

#Uma variável que está recebendo o salário digitado por meu úsuario e multiplicando pelos 5%
bonus = salario * 0.05

# Bonus total que está recebendo a soma do salário com bonus
bonus_total = salario + bonus

#Condicional que verifica o tempo de casa e se esse tempo é maior que 5 para liberar o bônus do úsuario
if 2024 - ano_serviço > 5: 
    print(f"Você tem direito ao bônus valor liquido do bônus: {bonus_total}")
else:
    print("Você não tem direito ao bônus")


