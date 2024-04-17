maior = menor = cont = 0
valores = list()
for c in range(0, 5):
    valores.append(int(input(f'digite um valor na posição {c}°: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        elif valores[c] < menor:
            menor = valores[c]
print(f'Voce digitou os valores {valores}')
print(f'maior numero é {maior} na posição ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}°.', end='..')
print()
print(f'menor numero é {menor} na posição ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}°.', end='...')

