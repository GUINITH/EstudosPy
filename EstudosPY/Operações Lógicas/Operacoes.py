
"""
Exemplos de Comparações com operadores lógicos: Maior que: >, Maior ou igaul: >=, Menor que: <, Menor ou Igual: <=, Igual: ==, Diferente: !=.
"""
comparacao1 = 5 > 3
print(comparacao1) 
# Output: True 5 Maior que 3

comparacao2 = 5 < 3
print(comparacao2)
#Output: False 5 é maior que 3

comparacao3 = 10 >= 9
print(comparacao3)
#Output: True 9 menor que 10

comparacao4 = 15 <= 25
print(comparacao4)
#Output: True 15 é menor que 25

comparacao6 = 30 == 30
print(comparacao6)
#Output: True 30 é igual a 30

comparacao7 = 50 != 100
print(comparacao7)
# Output: True 50 é diferente de 100

#Exemplo Negação Lógica

negacao1 = not 2 > 1
print(negacao1)
#Output: False Porquê estamos usando a função not, que determina a negação no código, ou seja se a saída real for True, será convertida para False, e vice-versa.

negacao2 = not 5!= 6
print(negacao2)
#Output: False

#Disjunção lógica:

dia_final = int(input("Digite o dia do mês para encerrar a promoção: "))
dia_atual = int(input("Digite o dia do mês para encerrar a promoção: "))
estoque_produtos = int(input("Digite o dia do mês para encerrar a promoção: "))

acabou = dia_atual > dia_final or estoque_produtos == 0
print(acabou)


