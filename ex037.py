
num = int(input('Digite um número? '))
print('''Escolha uma das opções abaixo 
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
resp = int(input('Sua opção: '))
if resp == 1:
    print(f'{num} convertido para BINÀRIO é igual a {bin(num)[2:]}')
elif resp == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif resp == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente.')
