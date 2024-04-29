from datetime import date
ano = date.today().year
pessoa = dict()
pessoa['Nome'] = str(input('NOME: '))
anodenasc = int(input('ANO DE NASCIMENTO: '))
pessoa['Idade'] = ano - anodenasc
pessoa['CTPS'] = int(input('CARTEIRA DE TRABALHO: (0 nâo tem)'))
if pessoa['CTPS'] != 0:
    pessoa['Ano de contrataçâo'] = int(input('ANO DE CONTRATAÇÂO: '))
    pessoa['Salario'] = float(input('SALARIO:R$ '))
    ida = pessoa['Ano de contrataçâo'] - anodenasc
    pessoa['Aponsetadoria '] = 35 + ida
print('=-'*30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
