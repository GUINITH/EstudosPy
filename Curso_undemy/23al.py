# Tratamento de Exeções: try, except
numero_str = input("Digite um número: ")
try:
    numero_float = float(numero_str)
    print(f"O número digitado foi: {numero_float}")
    print(f'O dobro de {numero_float} é: {numero_float * 2}')
except:
    print("Isso nao é um número valido")
    

