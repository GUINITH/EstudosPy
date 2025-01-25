"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

"""

palavra_secreta = 'python' 
dica = ''
tentativas = 0

while True: 
    letra = input('Digite uma letra: ')
    tentativas += 1
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra_secreta:
        dica = f"Acertou, a letra {letra} existe em {palavra_secreta}"
        print(dica)
        break 
    
    else:
        dica += '*'
        continue