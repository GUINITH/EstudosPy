'''
Exercicio 
Peça ao usuário para digitar seu nome 
Peça ao usuário para digitar a sua idade 

Se nome e idade  forem digitados:
    Exiba:
    seu nome é {nome}
    seu nome invertidop é {nome invertido}
    seu nome  contém ou não espaços
    seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome é {letra}
    Se nada for didigitado, exiba:
    Exiba: Desculpe, você deixou campos vazios.

'''

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ") 

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome nao contém espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, vocé deixou campos vazios.")