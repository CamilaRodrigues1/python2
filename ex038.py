num = int(input('Escreva um número: '))
num1 = int(input('Escreva segundo número: '))
maior = num
if num1 < num:
    print('O primerio numero é maior')
    maior = num1
elif num < num1:
    print('O segundo número é maior.')
elif num == num1:
    print('Não existir numero maior ,eles tem mesmo valor')