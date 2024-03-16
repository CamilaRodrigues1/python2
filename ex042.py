print('=-='*20)
print('==================ANALIZADOR DE TRIÂNGULO===================')
print('=-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('O segmentos acima podem FORMAR UM TRIÂNGULO.')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('O segmentos acima não FORMAM.')
