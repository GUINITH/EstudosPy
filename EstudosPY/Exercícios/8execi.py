# Listas
# Listas é tipo  de variáveis que podem receber diversos valores


#Esse é o exemplo de lista declaração de listas:
lista_exeplo1 = [1,2,3]
#Se quiser utilizar o método list()
lista_exeplo2=list(range(1,4,1))
print(lista_exeplo1, lista_exeplo2)
# lista vazia
lista_vazia = []
# Função list(), serve para converter/criar uma lista com essa função
list()
# Acessando inidices da minha lista
#Crie uma lista e acesse o segundo indice da lista
lista = list(range(2,11,2))
# lista = [ 2,4,6,8,10]
#Acessando o segundo índice de minha lista:
print(lista[2]) # saída: 6
#Pegando o último elemento da lista
print(lista[-1]) # Resultado: 10
#Pegando o penúltimo elemento da lista
print(lista[-2]) #Resultado: 8

# Pegando ídices subjacentes com slice:
lista_slice = [3,4,5,6,7,8,]
# Pega os 3 primeiros índices da lista com slice:
print(lista_slice[:3])
# Pega os 3 últimos índices da lista com slice:
print(lista_slice[3:])
#Pegue os dois índices do meio da lista:
print(lista_slice[2:4])
# Além disso podemos adicionar passos no slice, para pegar uma sequência 2 em 2 por exemplo
lista_mult2 = list(range(11))
# pegue um múltiplo de 2 em uma lista até 10:
# [valor inicial é o índice da sublista a ser gerado, segundo é o valor final, terceiro é o passo, ou seja de 2 em 2 números]
print(lista_mult2[2:11:2]) # Resultado: [2,4,6,8,10]
#pecorrendo lista
for numero in lista_mult2:
    print(numero)
#Testando a existência de valores:
#Declarando uma lista
lista_nomes = [ "Guilherme", "Rafael","Pedro", "Lucas"]
exist_nome = "Rafael" in lista_nomes
print(exist_nome)