from time import sleep
def maior(* num):
    cont = maior = 0
    print('='*30)
    print("Analizando os valores passados...")
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados {cont} valores ao todo.')
    print(f'o maior valor informado foi {maior}')


maior(9, 5, 1, 3, 6)
maior(5, 8, 1, 4)
maior(2, 3)
