from random import randint
from time import sleep
lista = list()
jogos = list()
print('=-'*30)
print(f'{'MEGA SENA': ^60}')
print('=-'*30)
num = int(input('Quantos jogos quer sortear? '))
tot = 1
while tot <= num:
    cont = 0
    while True:
        numeros = randint(1, 61)
        if numeros not in lista:
            lista.append(numeros)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-'*30)
print('-=-'*3, f'SORTEANDO {num} JOGOS', '-=-'*3)
for i, c in enumerate(jogos):
    print(f'JOGO{i+1}: {c}')
    sleep(2)
print('=-'*4, '< BOA SORTE >', '=-'*4)
