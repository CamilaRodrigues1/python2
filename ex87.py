matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = s = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor na posição [{l} ,{c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()
print(f'a soma de todos os valores pares são {par}')
for l in range(0, 3):
    s += matriz[l][2]
print(f'A soma de todos os números da terceira coluna são {s}')
for c in range(0, 3):
    if c == matriz[1][c]:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda linha é {maior}')
