import random
a1 = str(input('Nome do aluno: '))
a2 = str(input('Nome do aluno: '))
a3 = str(input('Nome do aluno: '))
a4 = str(input('Nome do aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'o escolhido para apagar a lousa é o aluno {escolhido}')