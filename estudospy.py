# -*- coding: utf-8 -*-
"""EstudosPy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h6_0j4OICO87C0GnpCZxuUY8Gr9EycXg
"""

def minha_primeira_funcao(a,b):
    somar = a + b
    return somar
print(minha_primeira_funcao(24,66))

minha_primeira_funcao(1000,500)

def calculando_valores(num1,num2):
  somar = num1 + num2
  mult = num1 * num2
  subtrair = num1 - num2
  dividir = num1 // num2
  potencia = num1 ** num2

  print(f"A soma dos números: {num1}, {num2} é {somar}")
  print(f"A subtração dos números: {num1}, {num2} é {subtrair}")
  print(f"A multiplicação dos números: {num1}, {num2} é {mult}")
  print(f"A divisão dos números: {num1}, {num2} é {dividir}")

  return somar, mult,subtrair,dividir,potencia

calculando_valores(2,76)

#Recursividade
def calculo(nb1,nb2):
    somar = nb1 + nb2
    return somar
def calcular_media(a,b):
    calk = calculo(a,b)
    media = 2/calk
    return media


t = calcular_media(34,45)
print(t)