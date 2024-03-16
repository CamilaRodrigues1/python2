peso = float(input('QUAL È O SEU PESO?kg '))
altura = float(input('QUAL È A SUA ALTURA? '))
imc = peso / (altura**2)
print(f'O seu imc é de {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc <= 30:
    print('Sobrepeso.')
elif imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbita')