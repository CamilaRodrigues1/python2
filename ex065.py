cont = soma = maior = menor = media = 0
resp = 'Ss'
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
media = soma / cont
print(f'''voce digitou {cont} números 
a soma de todos ele é {soma}
e a media é de {media:2}
e o numero maior é {maior} e o numero menor é {menor}''')

