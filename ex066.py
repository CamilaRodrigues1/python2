cont = s = 0
while True:
     num = int(input('Digite um número: para parar digite [999]'))
     if num == 999:
        break
     cont += 1
     s += num
print(f'a soma de todos os {cont} valores é {s}.')
