import random
print('=-=-'*15)
print('ESTOU PENSANDO EM UM NÚMERO 0 Á 5...TENTE DESCOBRIR.....')
print('=-=-'*15)
computador = random.randint(0, 5)
jogador = int(input('Qual número que estou pensando? '))
print(f'O número que eu pensei foi \033[36m{computador}\033[m')
if jogador == computador:
    print('\033[34mVocê GANHOU\033[m!')
else:
    print('\033[31mVocê PERDEU!\033[m')
print('Fim de jogo!')
