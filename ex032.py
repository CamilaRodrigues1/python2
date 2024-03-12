ano = int(input('Qual ano deseja saber? '))
print(f'O ano de {ano}', end=' ')
if ano % 4 == 0:
    print('ele é BISSEXTO!')
else:
    print('ele não é BISSEXTO!')
