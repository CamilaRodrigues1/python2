print('=-=-'*15)
re = 'REAJUSTE SALARIO'
print(f'\033[33m{re: >35}\033[m')
print('=-=-'*15)
sal = float(input('Qual é o seu salario?R$ '))
print(f'O seu salario é de R$ {sal:.2f} e com o aumento de 15% seu novo salario é de R$ {sal+(sal*15/100):.2f}')
