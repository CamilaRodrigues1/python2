import random
lista = (random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
num = lista
print('A sua lista é ', end='')
for c in num:
    print(f'{c}', end=' ')
print(f'\no maior numero sorteado {max(num)}')
print(f'o menor numero sorteado {min(num)}')
