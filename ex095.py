jogador = dict()
partidas = list()
dados = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    totalpartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,  totalpartidas):
        partidas.append(int(input(f'Quantos gols na {c}° partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    dados.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!Responda apenas S ou N.')
    if resp in 'N':
        break
print('=='*30)
print('Cód ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*60)
for d, j in enumerate(dados):
    print(f'{d:>3} ', end='')
    for i in j.values():
        print(f'{str(i):<15}', end='')
    print()
print('=='*30)
while True:
    jogadores = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if jogadores >= len(dados):
        print(f'ERRO!Não existir jogador com o código {jogadores}')
    else:
        print(f'==== Lenvantamento do jogador {dados[jogadores]["nome"]} ==== ')
        for c, j in enumerate(dados[jogadores]["gols"]):
            print(f'=> Na partida {c} fez {j} gols.')
    print('=='*30)
    if jogadores == 999:
        break
    print()
print('Volte sempre!')
