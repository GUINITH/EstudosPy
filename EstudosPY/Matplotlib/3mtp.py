# Plotagem de pontos x e y:
"""
A função é usada para desenhar pontos (marcadores) em um diagrama. plot()

Por padrão, a função desenha uma linha de ponto a ponto. plot()

A função usa parâmetros para especificar pontos no diagrama.

O parâmetro 1 é uma matriz que contém os pontos no eixo x.

O parâmetro 2 é uma matriz que contém os pontos no eixo y.

Se precisa traçar uma linha de (1,3) a (8, 10), temos que pasar duas matrizes [1,8] e [ 3, 10] para função de plotagem.

"""

# Desenhe uma linha em um diagrama da posição (1,3) á posição (8,10):
import matplotlib.pyplot as plt 
import numpy as np

# O eixo x os pontos é (1,3)
# O eixo y os pontos é (3,10)
x = np.array([1,8])
y = np.array([3,10])

plt.plot(x,y)
plt.show()

# desenhe uma linha em um  diagrama da posição (3,6) á posição (8,10)
x = np.array([3, 8])
y = np.array([6, 10])
plt.plot(x,y)
plt.show()

"""
O eixo x é o eixo horizontal.
O eixo y é o eixo vertical.
"""

