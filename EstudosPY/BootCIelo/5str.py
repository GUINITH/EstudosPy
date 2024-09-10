#Strings

#Concatenação
frase1,frase2,frase3 = "Guilherme", " ","Felipe"
soma = frase1 + frase2 + frase3
print(soma)

#Operadores LÓGICOS
fruta1,fruta2 = "banana","abacaxi"
comparacao = fruta1 > fruta2
print(f"{fruta1} é maior que {fruta2}: {comparacao}")

# Trasformando uma String em lista

string = "Ola Mundo"
lista = list(string)
print(lista)

#Metodo Join
str_var = "Flamengo"
adicionando_str = "Malvadao".join(str_var)
print(adicionando_str)

#Quebralinha
print("Ola\nMundo")

#tAbulacao
aprovados = ['Mario', 'Peach', 'Luigi']
reprovados = ['Wario', 'Bowser']
 
print('Candidatos aprovados:')
for nome in aprovados:
    print('\t', nome)
 
print('Candidatos reprovados:')
for nome in reprovados:
    print('\t', nome)

#Maiuscula

frases = "vAmos Programar"
maiuscula = frases.upper()
print(maiuscula)

#minuscula
otura_frase = "PYTHON"
minuscual = otura_frase.lower()
print(minuscual)

#Title
estado = 'rio de janeiro'
corrigindo = estado.title()
print(corrigindo)

#capitalize
frase4 = "eU sou Programador"
correcao = frase4.capitalize()
print(correcao)

#Qubrando strings com split()

texto = "Eu amo Programar em Python"
palavras = texto.split()
print(palavras) 


#Subistituindo expressões

texto = "Eu amo Programar em Python"
sustituindo = texto.replace("Python","Javascript")
print(texto,"\n",sustituindo)

#Funcao Format

Nome= input("digite seu nome: ")
idade = int(input("digite sua idade: "))
ano = int(input("digite o ano de formação: "))
mensagem = "Eu me chamo {}, tenho {} anos, sou programador desde {}."
formatando_mensagem = mensagem.format(Nome,idade,ano)
print(formatando_mensagem)