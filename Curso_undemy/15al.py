# if / else if / else 
# se / se não se / se não

# Condicionais ou desvio de fluxo, são instruções do Python que descide se outras linhas serão ou não executadas. Se a condição for verdadeira, execute essa linha, se não execulte essa outra linha.

entrada = input('Você quer entrar no jogo? (s/n) ')
if entrada == 's':
    print('Vamos la')
elif entrada == 'n':
    print('Volte quando quiser')
else:
    print('Resposta inválida, digite apenas s para sim ou n para não')