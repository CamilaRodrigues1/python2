passagem = int(input('Quantos km você quer viajar? '))
print(f'Sua viagem é de {passagem}km.')
print('Sua passagem custarà R$', end=' ')
if passagem <= 200:
    print(f'{passagem*0.50:.2f}')
else:
    print(f'{passagem*0.45:.2f}')
print('Boa viagem!!')
