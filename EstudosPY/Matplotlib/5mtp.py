import matplotlib.pyplot as plt
import numpy as np

# Marcadores 
''' 
você pode usar o argumento palavra-chave marker para enfatizar cada ponto com um marcador especifico:
''' 
# Marque cada ponto com um círculo:

ponto_y = np.array([3,8,1,10])
plt.plot(ponto_y, marker = 'o')


#Marque cada ponto com uma estrela:
plt.plot(ponto_y, marker = '*')
#plt.show()

''' 
Referência do marcador
Você pode escolher qualquer um destes marcadores:

Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
''' 

# Tamanho do Marcador

''' 
Você pode usar o argumento palavra-chave markersize ou versão mais curta ms para definir o tamanho dos marcadores: 
''' 
# Defina o tamanho dos marcadores para 20:

plt.plot(ponto_y, marker= 'o', ms = 20)
#plt.show()


# Cor do Marcador:
''' 
Você pode usar o argumento palavra-chave markeredgecolorou o mais curto mecpara definir a cor da borda dos marcadores:
''' 

# Defina a cor EDGE para vermelho:

plt.plot(ypoints, marker = 'o', ms= 20, mec='r')
#plt.show()

''' 
VocÊ pode usar o argumento palavra-chave markerfacecolot ou o mais curto mfc para definir a cor dentro da borda dos marcadores: 
''' 
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
#plt.show()

''' 
Use os argumentos mece mfcpara colorir todo o marcador:
''' 

# Defina a cor da borda e da face como vermelho:
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
#plt.show()

''' 
Você também pode usar valores de cores hexadecimais: 
''' 

# Marque cada ponto com uma linha cor verde:
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')

''' 
Ou qualquer um dos 140 nomes de cores suportados.
'''

# Marque cada ponto com a cor chamada 'hotpink':
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
