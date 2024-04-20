dados = list()
dados1 = list()
cont = maior = menor = 0
print('=-'*30)
print(f'{'CADASTRO DE PESSOAS': ^60}')
print('=-'*30)
while True:
    dados.append(str(input('NOME: ')))
    dados.append(int(input('PESO: ')))
    cont += 1
    if len(dados1) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    dados1.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Foram cadastradas {cont} pessoas.')
print(f'Maior peso foi {maior}kg peso de  ', end=' ')
for p in dados1:
    if p[1] == maior:
        print(f'[{p[0]}].', end=' ')
print(f'\nMenor peso foi {menor}kg peso de ', end=' ')
for p in dados1:
    if p[1] == menor:
        print(f'[{p[0]}].', end=' ')
print('=-'*30)
