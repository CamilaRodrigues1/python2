termo = int(input('Primeiro termo: '))
razao = int(input('Razâo: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo, razao):
    print(c, end=' -> ')
print('acabou')
