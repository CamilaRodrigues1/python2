print('=+'*15)
print('{:-^30}'.format('BANCO CR'))
print('=+'*15)
valor = int(input('Qunato você quer sacar? R$ '))
tot = valor
ced = 50
totacedula = 0
while True:
    if tot >= ced:
        tot -= ced
        totacedula += 1
    else:
        if totacedula > 0:
            print(f'O total de {totacedula} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totacedula = 0
        if tot == 0:
            break
