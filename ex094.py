pessoa = dict()
galera = list()
s = midade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in "FfMm":
            break
        print('ERRO! Por favor digite apenas M ou F:')
    pessoa['idade'] = int(input('Idade: '))
    s += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N:')
    if resp == 'N':
        break
print('=-'*30)
print(f'A) Ao todo foram cadastrados {len(galera)} pessoas.')
midade = s / len(galera)
print(f'B) A média de idade é de {midade:5.2f} anos.')
print(f'C) As mulheres cadastrada foram ', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('D) A lista das pessoa que estão acima da média.', end= '')
for p in galera:
    if p['idade'] >= midade:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v} :', end='')
        print()
print('PROGRAMA ENCERRADO')
