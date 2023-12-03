# Determinando o Tipo de Entrada de Dados

Vamos imaginar um programa que informa quantos anos falta para que uma criança atinja a maioridade. Podemos ler a idade da criança pelo teclado (entrada), subtrair a idade do número 18 (processamento) e exibir o resultado da conta na tela (saída). Considere a solução abaixo:

`idade = input('Digite a sua idade: ')
resto = 18 - idade
print('Faltam', resto, 'anos.')`

Se você copiar e executar o programa, ele dará erro na segunda linha. Isso ocorre porque o teclado é uma "máquina de escrever" um pouco mais moderna. Portanto, tudo que entra pelo teclado é considerado pelo Python como texto (ou seja, str). Porém, não podemos "fazer contas" com textos. Fazemos contas com números. Portanto, neste caso, precisamos falar para o Python interpretar a nossa entrada como um número. Um bom tipo de dado para "idade" seria um número inteiro. Fazemos isso colocando o nome do tipo desejado, e entre parênteses colocamos nosso input:

`idade = int(input('Digite a sua idade: '))
resto = 18 - idade
print('Faltam', resto, 'anos.')`

Chamamos essa operação de ``coerção de tipo(type coersion)``. Em materiais em inglês você verá essa operação com o nome casting. Tome cuidado: operações de coerção podem resultar em perdas de dados. Se você converter o número ``float`` 3.9 para ``int``, ele não arredondará para 4, e sim descartará a parte fracionária, resultando em 3.

exemplos na pasta de [Entradas.py](C:\Users\guigu\OneDrive\Documents\GitHub\EstudosPy\EstudosPY\Entradas\Entradas.py)