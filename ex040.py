n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n2+n1)/2
print(f'Sua média é {media} ')
if media < 5:
    print('REPROVADO')
elif 6.9 > media >= 5:
    print('RECUPERAÇÃO')
elif media > 7:
    print('APROVADO')
