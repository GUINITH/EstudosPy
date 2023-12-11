
#### Laços de Repetição
* Em Python, a instrução while é bastante parecida com o if: ela possui uma expressão lógica, e seu conteúdo só será executado se a expressão for verdadeira. Porém, após chegar ao final, ela retorna ao início e testa novamente a condição.

* Se ela for verdadeira, seu conteúdo será executado de novo. Ao final da nova execução, a condição é testada novamente, e assim sucessivamente. A execução só será interrompida quando o teste se tornar falso. Vejamos como resolver o problema da idade utilizando o while:

``idade = int(input('Digite a idade: ')) while idade < 0 or idade > 150: print('Erro! Idade deve estar entre 0 e 150!') idade = int(input('Digite a idade: '))``
``print('Obrigado!')``

Faça alguns testes com o programa acima. Note que se você digitar uma idade válida desde o início, ele nunca chega a mostrar erro: o while é como um if e será ignorado se sua condição for falsa. Porém, caso você digite valores inválidos, a condição será verdadeira e ele irá executar enquanto você estiver digitando valores falsos.