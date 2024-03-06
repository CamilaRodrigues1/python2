num = int(input('Informe um número: '))
print(f'Analizando o número: {num}')
print(f'''UNIDADE: {num // 1 % 10}
DEZENAS: {num // 10 % 10}
CENTENA: {num // 100 % 10}
MILHAR: {num // 1000 % 10}''')
