# For 


for i in range(11):
    print(i)


texto = "Python"

for i in range(len(texto)):
    print(texto[i])


#for letra in texto:

interador = iter(texto)

while True:
    try:
        letra = next(interador)
        print(letra)
    except StopIteration:
        break