import random
cont = 0
while True:
    num = int(input('digite um número: '))
    computador = random.randint(1, 13)
    s = computador + num
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('IMPAR OU PAR? [I/P] ')).strip().upper()[0]
    print(f'o computador colocou {computador}')
    print(f'A soma de {computador} + {num} = {s}')
    print('\033[333deu PAR'if s % 2 == 0 else 'deu IMPAR\033[m')
    if jogador == 'P':
        if s % 2 == 0:
            print('\033[32mvenceu\033[m')
            cont += 1
        else:
            print('\033[34mperdeu\033[m')
            break
    elif jogador == 'I':
        if s % 2 == 1:
            print('\033[32mvenceu\033[m ')
            cont += 1
        else:
            print('\033[34mperdeu\033[m')
            break
    print('\033[31mVamos novamente .....\033[m')
print(f'\033[36mVocê ganhou {cont} vezes\033[m')
