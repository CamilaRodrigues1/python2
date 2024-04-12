soma = cont = 0

for c in range(1, 7):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f'A soma de todos {cont} números pares são {soma}')
