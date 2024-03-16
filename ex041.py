from datetime import date
ano = date.today().year
anos = int(input('QUAl È O ANO DO NASCIMENTO DO ATlETA? '))
idade = ano - anos
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÙNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
