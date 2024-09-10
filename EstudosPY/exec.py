def arabico_para_romano(digito):
        
    romano = ''
    if digito <= 3:
        romano = 'I' * digito
    elif digito <= 8:
        romano = 'I'*(digito == 4)  + 'V' + 'I'*(digito - 5) 
    else:
        romano = 'I' + 'X'

    digitos = [int(digito) for digito in str(numero)]

    return romano

for i in range(10):
    print(i,'=',arabico_para_romano(i))