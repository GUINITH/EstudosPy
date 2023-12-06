nota1= float(input("Digite sua nota1: "))
nota2 = float(input("Digite sua nota2: "))

media_notas = (nota1 + nota2)/2

if media_notas == 10.0 or media_notas >= 6.0:
    print("Aluno Aprovado")

elif media_notas < 6.0: 
    print("Aluno Reprovado")

print("Sua média é: ", media_notas)