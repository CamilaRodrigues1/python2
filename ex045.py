from random import randint
from time import sleep
computador = randint(0, 2)
jogo = ['\033[30mPEDRA\033[m', '\033[32mPAPEL\033[m', '\033[33mTESOURA\033[m']
print('\033[31m=-=\033[m'*30)
print('JOGO DO PEDRA, PAPEL, TESOURA!')
print('\033[31m=-=\033[m'*30)
print('''[0]\033[30mPEDRA\033[m
[1]\033[32mPAPEL\033[m
[2]\033[33mTESOURA\033[m''')
jogador = int(input('Qual é a sua opçao? '))
print('\033[30mPEDRA\033[m')
sleep(1)
print('\033[32mPAPEL\033[m')
sleep(1)
print('\033[33mTESOURA\033[m')
sleep(1)
print('\033[31m=-=\033[m'*30)
print(f'O computador jogou {jogo[computador]}')
print(f'O jogador jogou {jogo[jogador]}')
print('\033[31m=-=\033[m'*30)
if computador == 0:
    if jogador == 0:
        print('\033[34mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[35mJOGADOR GANHOU!\033[m')
    elif jogador == 2:
        print('\033[36mCOMPUTADOR GANHOU!\033[m')
    else:
        print('\033[37mJOGADA INVALIDA!\033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[36mCOMPUTADOR GANHOU!\033[m')
    elif jogador == 1:
        print('\033[34mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[35mJOGADOR GANHOU!\033[m')
    else:
        print('\033[37mJOGADA INVALIDA!\033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[35mJOGADOR GANHOU!\033[m')
    elif jogador == 1:
        print('\033[36mCOMPUTADOR GANHOU!\033[m')
    elif jogador == 2:
        print('\033[34mEMPATE!\033[m')
    else:
        print('\033[37mJOGADA INVALIDA!\033[m')
print('\033[31m=-=\033[m'*30)
print('FIM DO JOGO')
print('\033[31m=-=\033[m'*30)