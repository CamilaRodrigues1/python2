aluno = dict()
aluno['Nome'] = str(input('NOME: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situacâo'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situacâo'] = 'Recuperaçâo'
else:
    aluno['Situacâo'] = 'Aprovado'
print('=-'*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')


