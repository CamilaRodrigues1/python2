casa = int(input('Qual é o valor da casa? '))
sal = int(input('Qual é o seu salário? '))
an = int(input('Quer pagar em quantos anos? '))
meses = an * 12
parcela = casa / meses
min = sal * 30/100
print(f'O valor da casa é de R${casa}, parcelada em {meses} meses no valor de R${parcela:.2f} por parcela.')
if parcela <= min:
    print('Financiamento aprovado')
else:
    print('Financiamento reprovado')
