num = int(input('Digite um numero: '))
tot = 0
for n in range(1, num+1, 1):
    if num % n == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[34m', end=' ')
    print(f'{n}\033[m', end='')
print(f'\nO número {num} foi divisivel {tot} vezes.')
if tot == 2:
    print('Ele é primo')
else:
    print('Ele não é primo.')
