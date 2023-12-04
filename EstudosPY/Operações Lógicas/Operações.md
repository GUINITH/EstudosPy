# Operações Lógicas

### Operadores Booleanos
* Quando estudamos variáveis, vimos que existem alguns tipos primitivos: str(texto), int(número inteiro), float(número Real), e boolean(lógico).

* Vimos diversas operações aritméticas também, como a soma, adivisão ou potência, cujos resultados são int ou float. Porém,podemos ter também operações cujo resultado é bool: são operações lógicas.

#### 1.1 Comparações
* Algumas das operações lógicas mais conhecidas são comparações:

`comparacao1 = 5 > 3 
print(comparacao1)
comparacao2 = 5 < 3
print(comparacao2)`

Se executarmos o código acima, a saída que teremos na tela será:

`True`,
`False`

Isso ocorre porque o 5 é maior que 3. Portanto, comparacao 1 recebeu uma expressão cujo valor lógico é verdadeiro, portanto seu resultado foi `True`, e o oposto ocorreu para comparacao2. O Pythoin possi 6 operadores de comparação:

Maior que: `>`,
Maior ou igaul: `>=`,
Menor que: `<`,
Menor ou Igual: `<=`,
Igual: `==`,
Diferente: `!`.

Note que o operador para comparar se 2 valores são iguais é ``==``, e não ``=``. Isso ocorre porque o operador ``=`` é o nosso operador de atribuição: ele diz que a variável à sua esquerda deve receber o valor da expressão à direita. O operador de ``== ``irá testar se o valor à sua esquerda é igual ao valor à sua direita e irá responder ``True`` ou `False`, como todos os outros operadores de comparação.


#### 1.2 Negação lógica

Outra operação lógica bastante importante é a negação. Ela inverte o resultado de uma expressão lógica. Caso a expressão resulte em ``True``, a sua negação irá resultar em ``False``, e vice-versa.

A negação em Python é representada pela palavra ``not``. Vamos modificar o exemplo anterior:

`comparacao! = not 5 > 3`
`print(comparacao1)`
`comparacao2 not 5 < 3`
`print(comparacao2)`

O resultado será:
`
`False`
`True`

Podemos resumir o funcionamento do not utilizando uma tabela-verdade. Nela testamos os diferentes valores possíveis para a entrada e anotamos o resultado para cada conjunto de valores:

| A | not A | |-------|-----------| | True | False | | False | True |





