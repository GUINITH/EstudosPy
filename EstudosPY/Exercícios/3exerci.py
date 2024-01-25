#Espressões aritiméticas
#Soma: +
#Subtração: -
#divisão real: /
#divisão inteira: //
#Resto da Divisão %
#Potência: **

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))

print("Escolha uma interação entre os números: somar, subtrair, multiplicar,dividir, potência")

operacao = input("Qual interação escolhida:  ")

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
divisao_real= numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
resto = numero_1 % numero_2
multiplicao = numero_1 * numero_2
Potencia = numero_1 ** numero_2

if operacao.lower() == "somar":
    print(f" a soma é: {soma}")
elif operacao.lower() == "subtrair":
    print(f" a subtração é: {subtracao}")

elif operacao.lower() == "dividir":
      divisao = input("digite 1-para divisão inteira, 2-para divisão real e 3 para o resto da divisão: ")
      if  divisao == "1":
          print(f"A divisão inteira é: {divisao_inteira}")
      elif  divisao == "2":
          print(f"A divisão real é: {divisao_real}")
      elif  divisao == "3":
          print(f"O resto da divisão é: {resto}")
      else:
          print("Operação indefinida")
elif operacao.lower() == "multiplicar":
    print(f" a multiplicação é: {multiplicao}")
elif operacao.lower() == "potencia":
       print(f" a potência é: {Potencia}")
else:
    print("Digite uma operação correta!")

