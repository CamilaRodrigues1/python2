cont = 0
num = s = 0
while num != 999:
    num = int(input('digite um número [digite 999 para parar]: '))
    if num != 999:
        s += num
        cont += 1
print(f'Voce digitou {cont} e a soma deles é de {s}')