valor = list()
resp = ''
while True:
    num = int(input('Digite um valor: '))
    if num not in valor:
        valor.append(num)
        print('valor adicionado com sucesso...')
    else:
        print('o numero ja adicionado, nao vou adicionar')

    resp = str(input('quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
valor.sort()
print(f'os valores digitados foi {valor}')
