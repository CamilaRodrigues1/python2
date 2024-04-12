lista = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
         'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
         'quatorze' 'quinze', 'dezesseis', 'dezessete',
         'dezoito', 'dezenove', 'vinte')
while True:
    cont = int(input('digite um numero de [0 á 20]'))
    print(f'voce digitou o numero {lista[cont]}')
    resp = str(input('quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break

print('fim do programa')
