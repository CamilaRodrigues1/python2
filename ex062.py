primeiro = int(input('Primeiro termo: '))
razao = int(input('Razâo: '))
termo = primeiro
c = 1
tot = 0
resp = 10
while resp != 0:
    tot = tot + resp
    while c <= tot:
        print(f'{termo} ->', end='')
        termo += razao
        c += 1
    print('pausa')
    resp = int(input('quanto termos que ver?'))
print(f'Pograma finalizado com {tot} termos mostrados')
