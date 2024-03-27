sexo = str(input('Imforme o sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('imformaçao invalida ,Informe o sexo: [F/M] ')).strip().upper()[0]
if sexo in 'Mm':
    print('sexo MASCULINO registrado com sucesso!!!')
if sexo in 'Ff':
    print('sexo FEMENINO registrado com sucesso!!!')
print('acabou')