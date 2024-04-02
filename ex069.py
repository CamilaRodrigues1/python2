cont18 = conthome = contmul = 0
resp = ' '
while True:
    print('=-'*30)
    print('      cadastre uma pessoa     ')
    print('=-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper().split()[0]
    resp = str(input('Quer continuar? [S/N] ')).strip().upper().split()[0]
    if idade > 18:
        cont18 += 1
    if sexo in 'F':
        if idade <= 20:
            contmul += 1
    elif sexo in 'M':
        conthome += 1
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Foram cadastrado {cont18} pessoas com mais de 18 anos.')
print(f'Foram cadastrado {contmul} mulheres com menos de 20 anos.')
print(f'Foi registrado {conthome} homens. ')
