# Plotando sem linha

'''
Para plotar apenas os marcadores, você pode usar o parâmetro de notação de string de atalho 'o', que significa 'anéis'.
'''

# Exemplo

'''
Desenhe dois pontos no diagrama, um na posição (1,3) e outro na posição (8,10)
'''
import matplotlib.pyplot as plt
import numpy as np

ponto_X = np.array([1,8])
ponto_Y = np.array([3,10])
plt.plot(ponto_X, ponto_Y, 'o')
plt.show()

# Varios Pontos

'''
Você pode plotar quantos pontos quiser, apenas certifique-se de ter o mesmo números de pontos em ambos os eixos.
'''

#Exemplo

'''
Desenhe uma linha em um diagrama da posição (1,3) para (2,8), depois para (6,1) e finamente para posição (8,10):

'''
x = np.array([1,2,6,8])
y = np.array([3,8,1,10])
plt.plot(x,y)
plt.show()

# Pontos x Padrão

'''
Se não especificarmos os pontos no eixo x, eles obterão os valores padrão 0,1,2,3 etc., dependendo do comprimento dos pontos y.

Portanto, se tomarmos o mesmo exemplo acima e deixarmos de fora os pontos x, o diagrama ficará assim:
'''

y = np.array([3,8,1,5,7])
plt.plot(y)
plt.show()

# Os pontos x no exemplo acima são [0,1,2,3,4,5].

# Pratica

# Desenhe um diagrama da posição (1,6) até (5, 9) e deppois (3, 10) até (2,8):
import numpy as np
import matplotlib.pyplot as plt
x_num = [1,5,3,2]
y_num = [6,9,10,8]
x_position = np.array(x_num)
y_position= np.array(y_num)

plt.plot(x_position,x_position)
plt.show()
