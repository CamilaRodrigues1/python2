print('=-'*30)
print('{:-^60}'.format('lojas compra mas não leva'))
print('=-'*30)
cont = s = promil = menor = nome = 0
resp = ' '
while True:
    print('=-'*30)
    produto = str(input('NOME DO PRODUTO: ')).strip().upper()
    preco = float(input('VALOR DO PRODUTO:R$  '))
    resp = str(input('QUER CONTINUAR? [S/N] ')).strip().upper()[0]
    s += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        nome = produto
    if preco >= 1000:
        promil += 1
    if resp in 'Nn':
        break
print('=-'*30)
print('{:-^40}'.format('VALOR DA SUAS COMPRAS'))
print('=-'*30)
print(f'''O total das compra é de R$ {s:.2f}
Foram comprados {promil} produtos que custa mais de R$1000.00.
O produto mais barato é o {nome} que custou R$ {menor:.2f}.''')



