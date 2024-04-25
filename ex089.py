lista = []
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1+nota2)/2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'{"Nº":<4}{"NOME":<20}{"MEDIA":>8}')
print('-='*30)
for p, n in enumerate(lista):
    print(f'{p:<4}{n[0]:<20}{n[2]:>8.1f}')
while True:
    print('=-'*30)
    aluno = int(input('Qual aluno quer ver a nota? [999 interrompe]:'))
    if aluno == 999:
        break
    if aluno <= len(lista)-1:
        print(f'O aluno {lista[aluno][0]} tem as notas {lista[aluno][1]}')
    else:
        print('opção invalia')
print('=-'*30)
print('FIM DO PROGRAMA')
print('-='*30)
