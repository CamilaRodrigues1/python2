jogador = dict()
partidas = list()
jogador['nome'] = str(input('Qual é o nome do jogador? '))
totalpartidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, totalpartidas):
    partidas.append(int(input(f'Quantos gols fez na partidas {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {totalpartidas} partidas.')
for i, c in enumerate(partidas):
    print(f'=> Na partida {i}, fez {c} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
