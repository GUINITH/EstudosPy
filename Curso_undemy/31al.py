frase = 'O python é uma linguagem de programação multiparadigma. \nPython foi criado por Guido van Rossum'



i = 0
letra_mais_vezes = 0
qtd_apareceu_mais_vezes = 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_atual = frase.count(letra_atual)

    if quantas_vezes_atual > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = quantas_vezes_atual
        letra_mais_vezes = letra_atual

    i += 1

print(f"A letra que apareceu mais vezes foi {letra_mais_vezes} que apareceu {qtd_apareceu_mais_vezes} vezes")