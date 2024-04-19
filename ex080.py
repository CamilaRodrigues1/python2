num = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Adicinado no final da lista....')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Acdicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'os valores da lista é {num}')
