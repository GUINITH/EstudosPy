# Tipos de dados Numpy

''' 
Por padrão, O python tem estes tipos de dados:

- strings- usado para representar dados de texto, o texto é colocado entre aspas. por exemplo, "ABCD"

- integer- usado para representar números inteiros. por exemplo, -1, -2, -3
- float- usado para representar números reais. por exemplo, 1,2, 42,42

- boolean- usado para representar Verdadeiro ou Falso.

- complex- usado para representar números complexos. por exemplo, 1,0 + 2,0j, 1,5 + 2,5j

''' 

# Tipos de dados em Numpy:

'''
NumPy tem alguns tipos de dados extras e refere-se a tipos de dados com um caractere, como 'i' números inteiros, 'u' números inteiros sem sinal, etc.

Abaixo está uma lista de todos os tipos de dados em Numpy e os caracteres usados para representá-los:

i- inteiro
b- boleano
u- inteiro sem sinal
f- flutuar
c- flutuação complexa
m- delta do tempo
M- data hora
O- objeto
S- corda
U- sequência Unicode
V- pedaço fixo de memória para outro tipo ( void )

'''

# Verificando tipo de dados de um array:

'''
O objeto array NumPy possui uma propriedade chamada dtype que retorna o tipo de dados do array:
''' 

# Obtenha o tipo de dados de um objeto array:
import numpy as np
arr1 = np.array(list(range(1,5)))
print(arr1.dtype) 
# saída: int32

# Obtenha o tipo de dados de um array contendo strings:
arr2 = np.array(['MARIA', 'JOÃO', 'Pedro'])
print(arr2.dtype)
# Saída: <U5



# Criando arrays com um tipo de dados definido

''' 
Usamos a array() função para criar arrays, esta função pode receber um argumento opcional: dtype que nos permite definir o tipo de dados esperado dos elementos do array:
''' 
# Crie um array com tipo de dados string:

arr3 = np.array([1,2,3,4], dtype='S')
print(arr3)
print(arr3.dtype)
'''
saída: 
[b'1' b'2' b'3' b'4']
|S1 

''' 
# Para i,,, e também podemos definir o tamanho u.fSU

# Crie um array com tipo de dados inteiro de 4 bytes:

arr4 = np.array([1,2,3,4,5], dtype='i4')
print(arr4)
print(arr4.dtype)

''' 
saída:
[1 2 3 4 5]
int32

''' 

# E se um valor não puder convertido?
''' 
Se for fornecido um tipo no qual os elemntos não podem ser convertidos, o NumPy gerará um ValueError.

-> ValueError no Python é gerado quando o tipo de argumento passado para uma função é inesperado/incorreto.
'''
# Uma string não inteira como 'a' não pode ser convertida em inteiro (irá gerar um erro):
'''
arr = np.array(['a', '2', '3'], dtype='i')
'''
# Convertendo tipo de dados em matrizes existentes

''' 
A melhor maneira de alterar o tipo de dados de um array existente é fazer uma cópia do array com o astype() método

A astype() função cria uma cópia do array e permite especificar o tipo de dados como parâmetro.

O tipo de dados pode ser especificado usando uma string, como 'f' para float, 'i' para inteiro etc. ou você pode usar o tipo de dados diretamente como float para float e int para inteiro.

''' 

# Altere o tipo de dados de float para inteiro usando 'i'como valor de parâmetro:

arr5 = np.array([1.1, 2.1,3.1])
newarr = arr5.astype('i')
print(newarr)
print(newarr.dtype)
''' 
saída: 
[1 2 3]
int32
'''
#Altere o tipo de dados de float para inteiro usando intcomo valor de parâmetro:

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

'''
saída:
[1 2 3]
int32 

'''
# Altere o tipo de dados de inteiro para booleano:
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

''' 
saída:
[ True False  True]
bool

''' 

# Exercício:
'''
NumPy usa um caractere para representar cada um dos seguintes tipos de dados, qual?

i = inteiro
b= booleano
u= inteiro sem sinal
f= flutuar
c= flutuação complexa
m= tempodelta
M= datahora
o= objeto
U= sequência
'''