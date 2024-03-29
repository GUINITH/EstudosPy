# -*- coding: utf-8 -*-
"""tuplas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t0vmbWNzD6NLkGdbiRlMJz6Eky-AfsJy
"""

#Definindo uma tupla
tupla_vz1 = () # Tupla vazia
tupla_vz2 = tuple() # Outra tupla vazia

#Tuplas com valores
tupla_num1 = (2,3,4,56,796,22,33)
tupla_num2 = (333,42,56,90,112)

print(tupla_vz1,tupla_vz2,tupla_num1,tupla_num2)

tupla_vz1[0] = 12 # Erro, tuplas são imutáveis, ou seja, não podemos alterar seu valor assim como listas.

#Desempacotamento

n1,n2,*n3 = tupla_num1
print(n1)
print(n2)
print(n3)

#OPERAÇÕES COM TUPLAS IMPLICITAS

x,y,*z =tupla_num2
print(x)
print(y)
print(z)

# Açucar sintático, o Python está usando a lógica de criar e desempacotar tuplas para realizar esse tipo de operação
x,y,z = y,z,x
print(x,y,z)

