termo = int(input('Primeiro termo: '))
razao = int(input('Razâo: '))
decimo = termo
c = 1
while c <= 10:
    print(f'{decimo} ->', end='')
    decimo += razao
    c += 1
print('acabou....')