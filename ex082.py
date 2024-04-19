lista = []
pares = list()
impares = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = str(input('Quer continuar?[N/S] '))
    if resp in 'Nn':
        break
for v, c in enumerate(lista):
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
lista.sort()
print(f'os números da lista é {lista} ')
print(f'os números impares são {impares}')
print(f'Os número pares são {pares}')
