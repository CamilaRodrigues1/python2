lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
lista.sort(reverse=True)
print(f'Os valores da lista em ordem decrescente são {lista}.')
print(f'Foram adicionado {cont} números.')
if 5 in lista:
    print('o valor 5 foi adicionado na lista.')
else:
    print('o valor 5 não foi adicionado na lista')
