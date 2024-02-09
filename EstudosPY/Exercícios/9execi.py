#Funções
def minha_primeira_funcao():
    print("Olá Mundo!")
minha_primeira_funcao()

#função comparâmetros
def soma(a, b):
    resultado = a + b
    print(resultado)
soma(23,56)

def cálculo(numero1,numero2):
    somar = numero1 + numero2
    subtrair = numero1 - numero2
    divisao_inteira = numero1 // numero2
    divisao_real = numero1 / numero2
    divisao_resto = numero1 % numero2
    multiplicacao = numero1 * numero2
    potencia = numero1 ** numero2
    print("Escolha a operação díposnivel: somar,subtrair,multiplicar,dividir ou potência")
    print("Para sair digite sair.")
    while True:
        opcao_do_usuario = input("Qual operação você deseja: ")
        if opcao_do_usuario.lower() == "somar":
            print(somar)
            decisao = input("Para continuar digite(continuar) e para sair digite(sair): ")
            if decisao.lower() == "sair":
                print("Encerrando programa")
                break
            elif decisao.lower() == "continuar":
                continue
        elif opcao_do_usuario.lower() == "subtrair":
            print(subtrair)
            decisao = input("Para continuar digite(continuar) e para sair digite(sair): ")
            if decisao.lower() == "sair":
                print("Encerrando programa")
                break
            elif decisao.lower() == "continuar":
                continue
        elif opcao_do_usuario.lower() == "dividir":
            print("Para divisão inteira digite 1.")
            print("Para divisão real digite 2.")
            print("Para resto de divisão digite 3.")
            opcao_de_divisao = int(input("Qual tipo de divisâo você deseja: "))
            if opcao_de_divisao == 1:
                print(divisao_inteira)
            elif opcao_de_divisao == 2:
                print(divisao_real)
            elif opcao_de_divisao == 3:
                print(divisao_resto)
            else:
                print("divisão incorridas")
                continue
        elif opcao_do_usuario.lower() == "multiplicar":
            print(multiplicacao)
        elif opcao_do_usuario.lower() == "potência":
            print(potencia)
        elif opcao_do_usuario.lower() == "sair":
            print("Obrigado, fim do programa")
            break
        else:
            print("Operação incorreta!")

primeiro_número = int(input("Digige um número: "))
segundo_numero = int(input("Digige um número: "))
 
cálculo(primeiro_número, segundo_numero)
       



