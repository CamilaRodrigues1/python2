import random
tot = 0
computador = random.randint(0, 11)
print('JOGO DA ADIVINHAÇAO')
print('ESTOU PENSANDO EM UM NÚMERO DE 0 Á 10 .')
acertou = False
while not acertou:
    resp = int(input('qual o numero que estou pensando?: '))
    tot += 1
    if resp == computador:
        acertou = True
    else:
        if resp < computador:
            print('Mais...tente novamente')
        elif resp > computador:
            print('menos... tente novamente')
print(f'O computador pensou {computador}')
print(f'acertou com {tot} tentativas')
