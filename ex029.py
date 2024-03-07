print('=-'*30)
print(f'                      RADAR DE VELOCIDADE')
print('=-'*30)
vel = int(input('Qual era a velocidade do carro? '))
print(f'A velocidade do carro é de {vel}KM.')
if vel > 80:
    nv = (vel-80)*7
    print(f'''Você ultrapassou a velocidade permitida! 
Você pagará uma multa de R${nv:.2f}''')
else:
    print('''Você está na velocidade permitida!
    TENHA UMA BOA VIAGEM!''')
    