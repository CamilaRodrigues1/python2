soma = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'a soma de todos os {cont} numero são {soma}')
