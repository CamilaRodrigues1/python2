homenidade = mulheridade = somaidade = nomevelho = 0
for p in range(1, 5):
    nome = str(input(F'NOME DA {p}° PESSOA: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO M/F: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        homenidade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homenidade:
        homenidade = idade
        nomevelho = nome
    if idade > 20 and sexo in 'Ff':
        mulheridade += 1
media = somaidade / 4
print(f'A média de idade do grupo é {media} anos.')
print(f'Tem {mulheridade} mulheres menor de 20 anos.')
print(f'O nome do homem mais velho é {nomevelho} e tem {homenidade} anos.')
