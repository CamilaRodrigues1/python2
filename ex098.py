from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('=*'*20)
    print(f'CONTAGEM DE {inicio} Á {fim} DE {passo} EM {passo}')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('fim!')
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}", end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('=*'*20)
print('AGORA É SUA VEZ')
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
contador(i, f, p)
print('fim do programa')