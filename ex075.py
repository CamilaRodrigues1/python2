num = (int(input('digite um valor: ')),
       int(input('digite um valor: ')),
       int(input('digite um valor: ')),
       int(input('digite um valor: ')))
print(f'O 9 apareceu {num.count(9)} x.')
print(f'o primerio numero 3 digitado esta na posiçao {num.index(3)+1}')
for n in num:
    if n % 2 == 0:
        print(f'os numeros pares são {n}.')
        