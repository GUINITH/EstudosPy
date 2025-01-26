"""
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de
inserir, apagar e listar valores
de uma lista. Não permita que o programa
quebre com erros de indexes inexistente
na lista.

"""
produto_envidado_pelo_usuario = ''
apagar_produto = ''
listar_produtos = ''
produtos = []

while True:
    apresentacao = """

    Escolha uma opção:
    [1] Inserir produto
    [2] Apagar produto
    [3] Listar produtos
    [4] Sair

    """
    print(apresentacao)

    opçao = int(input('Digite a opção desejada: '))

    if opçao == 1:
        produto_envidado_pelo_usuario = input('Digite o produto: ')
        produtos.append(produto_envidado_pelo_usuario)
        continue

    elif opçao == 2:
        apagar_produto = input('Digite o nome do produto ou seu index que deseja apagar: ')
        if apagar_produto.isdigit():
            produtos.pop(int(apagar_produto))
        elif apagar_produto in produtos:
            produtos.remove(apagar_produto)
        else:
            print('Produto inexistente')
        continue

    elif opçao == 3:
        listar_produtos = produtos
        for index, produto in enumerate(listar_produtos):
            print(index, produto)
        continue

    elif opçao == 4:
        print('Programa encerrado')
        break

    else:
        print('Opção inválida')