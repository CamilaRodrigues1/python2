from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6), 'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
ranking = []
print('=-'*30)
print(f'{"VALORES SORTEADOS":^50}')
print('=-'*30)
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-'*30)
print(f'{"ranking dos jogadores":^50}')
print('=-'*30)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
print('=-'*30)
