num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
maior, menor = 0,0
if num1 > num2:
    maior, menor = num1, num2
    print(f"maior número é: {maior} e o menor é: {menor}")
elif num1 < num2:
    maior,menor = num2, num1
    print(f"maior número é: {maior} e o menor é: {menor}")
else:
    print(f"{num1} é igual à: {num2}")