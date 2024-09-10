# Pyplot

# A marioria dos utilitários Matplotlib encontra-se sob o submódulo, e geralmente são importados sob o pseudônimo: pyplot plt
import matplotlib.pyplot as plt 

# Agora o pacote Pyplote pode ser referido como .plt

#Exmplo: Desenhe uma linha em um diagrama da posição (0,0) á posição (6,250):
import numpy as np

x = np.array([0, 6])
y = np.array([0, 250])
plt.plot(x,y)
plt.show()



