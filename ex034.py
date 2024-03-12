sal = float(input('Qual é o seu salário atual? R$ '))
print(f'O seu salário é de R$ {sal:.2f}')
if sal >= 1250:
    print(f'Com o aumento de 10% o seu novo salário é de R$ {sal+(sal*10/100):.2f}')
else:
    print(f'Com o aumento de 15% o seu novo salário é de R$ {sal+(sal*15/100):.2f}')
