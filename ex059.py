num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
resp = 0
while resp != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    resp = int(input('Qual é a sua opção? '))
    if resp == 1:
        print('=-' * 30)
        print(f'O resultado de {num1} + {num2} = {num1+num2}')
        print('=-'*30)
    elif resp == 2:
        print('=-' * 30)
        print(f'O resultado de {num1} * {num2} = {num1*num2}')
        print('=-'*30)
    elif resp == 3:
        maior = num1
        if num1 > num2:
            maior = num1
        if num1 < num2:
            maior = num2
        print('=-' * 30)
        print(f'O numero {maior} é maior')
        print('=-' * 30)
    elif resp == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    else:
        print('=-' * 30)
        print('opção invalida..')
        print('=-' * 30)
print('fim do programa')
