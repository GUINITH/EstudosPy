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