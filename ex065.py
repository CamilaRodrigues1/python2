num = int(input('quantos termos voce quer mostrar?  '))
f1 = 0
f2 = 1
print('='*30)
print(f'{f1}->{f2}', end='')
cont = 3
while cont <= num:
    f3 = f1 + f2
    print(f'{f3}->', end='')
    cont += 1
print(' acabou......')
