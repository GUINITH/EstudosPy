''''
Exercicio de Calculadora

Pedir ao usuário para digitar dois números e uma operação matemática

Se os dois números e a operação forem digitados, exiba o resultado da operação
Se nada for digitado, exiba: Desculpe, você deixou campos vazios.

'''
while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite masi um número: '))
        operacao = input('Digite uma operação: ')
        if operacao == '+':
            print(num1 + num2)
            break
        elif operacao == '-':
            print(num1 - num2)
            break
        elif operacao == '*':
            print(num1 * num2)
            break
        elif operacao == '/':
            print(num1 / num2)
            break
        else:
            print('Operação inválida')
            break
    except:
        print('Desculpe, vocé deixou campos vazios')
        break
