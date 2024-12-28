# Exercicio de IMC

# Crie um programa que leia o peso e a altura de uma pessoa, calcule e mostre o seu IMC 

nome = 'Guilherme'
altura = 1.82 
peso = 166

calculo_imc = peso / (altura ** 2)

print(f'{nome}, tem {altura} de altura, \npesa {peso}kg e seu IMC e: \n{calculo_imc:.2f}')