""# Operações básicas de tuplas tuple()

tupla1 = tuple() # tupla vazia
tupla2 = () # tupla vazia
 
linguagens = ('PHP',"JAVA","PYTHON")
#Uma tupla com 3 elementos

elementos = 3.15, 1000, False,"Laranja"
#Tupla declarada sem parênteses

#tuplas dentro de uma tupla
tupla_in_tuplas =(("la","li"),(11,22),(True, False))

print(linguagens[0]) #Result: "PHP"
print(linguagens[-1::-1]) #Result: '"PYTHON","JAVA","PHP"
print(elementos[2]) #Result: False
print(tupla_in_tuplas[2][0]) #Result: True

"""
Todas as outras operações que revisamos hoje em listas podem ser realizadas com tuplas:
iteração através de um loop do tipo for
slicing passando índice inicial, final e salto
concatenação
"""

# convertendo lista para tupla:
numeros = [23,45,67,89,100,19]
tupla_de_numeros = tuple(numeros)
print(tupla_de_numeros)

# Podemos converter tuplas em listas
lista_num = list(tupla_de_numeros)
print(lista_num) 

#Imutabilidade:  Quando utilizamos tuplas, estamos dizendo que aqueles dados não poodem sofrer alterações
#Mutabilidade: Diferente de tuplas as listas podem ser alteradas, segue os exemplos abaixo

lista_ex = list(range(1,6)) # criando uma lista de 1 até 5
tupla_ex = tuple(range(1,6)) # criando uma tupla de 1 até 5
print(lista_ex, tupla_ex) # printando a lista e a tupla

lista_ex.append(6) # Como lista é mutavel, podemos adicionar e remover valores dentro de uma lista
print(lista_ex[:]) # [1,2,3,4,5,6]

"""tupla_ex[0] = 6 #Como tupla é imutavel, não podemos alterar elas do mesma forma que utilizamos com a lista
print(tupla_ex[0]) # Erro"""

#Desempacotamento de tuplas com variáveis para cada elemento na tupla
a,b,c,d= ("Flamengo", "Vasco","Fluminense","Botafogo")
print(a)
print(b)
print(c)
print(d)

#Desempacotamento de tuplas de múltiplos elementos

c,*t = ("Flamengo", "Vasco","Fluminense","Botafogo")
print(c)
print(t)

#operação de tuplas inplicitas
"""
Explicação:
O Python oferece alguns truques que permitem escrever códigos mais enxutos do que em outras linguagens, e parte desses truques utiliza sintaxe de tupla. Por exemplo, para criar duas variáveis e atribuir valores simultaneamente a elas, podemos utilizar vírgulas:

"""
x,y = (20,21)
print(x,y)
x,y=y,x
print(x,y)

"""
Esse tipo de operação é considerado açúcar sintático, ou seja, não acrescenta funcionalidades novas, apenas cria formas mais simples e legíveis de realizar operações que já éramos capazes de realizar anteriormente.

Internamente, o Python está usando lógica de criar e desempacotar tuplas para realizar esse tipo de operação.
"""
#Enumerate  
"""Existe uma ferramenta em Python que pode nos ajudar a escrever de maneira mais pythonica, sem precisar acessar lista por índice: o enumerate. Primeiro, vamos entender o que ele faz e, em seguida, veremos como deixar o código mais limpo:     """ 
tupla_de_frutas = ('abacate', 'banana', 'carambola', 'damasco', 'embaúba', 'framboesa', 'goiaba')
for frutas in enumerate(tupla_de_frutas):
    print(frutas)

#zip

alunos = ["FABIO","CARLOS","LUIZ",'PEDRO']
notas = [5, 9,0,23]
boletim = () 

for aluno,nota in zip(alunos,notas):
    boletim = aluno,nota
    print(boletim)

""" Assim como no enumerate, o zip montou tuplas. Cada tupla representa 1 posição das listas originais, e cada posição dentro da tupla representa o dado de uma das listas. Ou seja, cada elemento do zip contém 1 elemento de cada lista original, na ordem que eles apareceram nas listas originais. Logo, ele permite percorrer 2 listas simultaneamente.
"""