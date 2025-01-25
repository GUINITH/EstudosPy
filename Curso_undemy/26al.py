"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

numero_do_usuario =  input('Digite um número inteiro:')
try:
    numero_do_usuario.isdigit()
    converte_numero = int(numero_do_usuario)
    if converte_numero % 2 == 0:
        print(f'{converte_numero} é par')
    else:
        print(f'{converte_numero} é impar')
except:
    print('Não é um número inteiro')

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.


hora_do_dia = input('Digite a hora do dia:')
try:
    if int(hora_do_dia) >= 0 and int(hora_do_dia) <= 11:
        print('Bom dia')
    elif int(hora_do_dia) >= 12 and int(hora_do_dia) <= 17:
        print('Boa tarde')
    else:
         print('Boa noite')
except:
    print('Hora inválida')

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

nome_do_usuario = input('Digite seu nome: ')
verificacao_1 = len(nome_do_usuario) <= 4
verificacao_2 = (len(nome_do_usuario) == 6) and len(nome_do_usuario) == 5

try:
    if nome_do_usuario.isalpha():
        if verificacao_1:
            print('Seu nome é curto')
        elif verificacao_2:
            print('Seu nome é normal')
        else:
            print('Seu nome é muito grande')
except:
    print('Não aceitamos números e caracteres especiais. Só letras!')

"""