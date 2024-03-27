from datetime import date
ano = date.today().year
totmaior = totmenor = 0
for c in range(1, 8):
    pessoas = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    nasc = ano - pessoas
    if nasc >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'{totmaior} pessoas atingiram a maior idade.')
print(f'{totmenor} pessoas são menores de idade')