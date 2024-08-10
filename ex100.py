from random import randint
def sorteia(lista):
    for c in range(0, 5):
        numeros = randint(1, 10)
        lista.append(numeros)
        print(f'{numeros}', end=' ')
    print('pronto')


def somarpar(lista):
    s = 0
    for valor in lista:
        if valor % 2 == 0:
            s += valor
    print(f'A soma dos valores pares são {s}')


n = list()
sorteia(n)
somarpar(n)
