"""
Constante = 'Variáveis que não podem ser alteradas'
Muitas condições no mesmo if (ruim)
 <- Contagem de complexidade (ruim)

"""

velocidade = 61 # velocidade atual do carro 
local_carro = 101 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade do radar 1
LOCAL_1 = 100 # local do radar 1
RADAR_RANGE =  1 # A distancia onde o radar pega

vel_Carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_Carro_pass_radar_1 


if vel_Carro_pass_radar_1:
    print('O carro passou da velocidade permitida no radar 1')

if carro_passou_radar_1:
    print('O carro passou do radar 1')

if carro_multado_radar_1:
    print('O carro multado no radar 1')