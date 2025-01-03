'''
Interpolação básica  de strings, bem simples basta  cria strings e passar os dados para elas serem preenchidas  com sinal de porcentagem % e o nome da variavel que deseja preencher.
s - string 
d e i - int 
f - float 
x e X Hexadecimal (ABCDEEF0123456789)

'''
nome = 'Guilherme'
preco = 1000.9090099
str_vazia = '%s, o preco e: R$%.2f' % (nome, preco)
print(str_vazia)
print('O hexadecimal de %d e: %04x' % (1500, 1500))

'''
Formatação básica com F-strings 

s - string 
d e i - int 
f - float 
x e X Hexadecimal (ABCDEEF0123456789)
.<numéro de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centralizado
- Quantidade de espaços
sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a

'''
variavel = 'Guilherme'
print(f'Eu sou {variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{100.8987930293023:+,.1f}')
print(f'O hexadecimal de 2000 é: {2000:08x}')
print(f'{variavel!r}')