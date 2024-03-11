num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'\033[33mO NÚMERO {num} È PAR!\033[m')
else:
    print(f'\033[34mO NÚMERO {num} É ÍMPAR!\033[m')
print('FIM DO PROGRAMA!')
