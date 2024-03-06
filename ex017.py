from math import hypot
op= float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(op,ad):.2f}')