lista = ('aprender', 'camila', 'caderno', 'televisão', 'monitor', 'teclado', 'mouse',
         'lâmpada', 'mesa', 'cadeira')
for c in lista:
    print(f'\nNa palavra {c} temos ', end='')
    for p in c:
        if p.lower() in 'aeiou':
            print(p, end=' ')
