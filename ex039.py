from datetime import date
print('=-='*30)
print('ALISTAMENTO MILITAR')
print('=-='*30)
anos = date.today().year
ano = int(input('Qual é o ano que voce nasceu? '))
idade = anos - ano
if idade == 18:
    print(f'Você tem {idade} e está na idade de se alistar ')
elif idade < 18:
    falta = 18 - idade
    print(f'Voce tem {idade} anos e ainda falta {falta} anos ')
elif idade > 18:
    falta = idade - 18
    print(f'Você tem {idade} anos e já passou da idade de se alistar,voce deveria ter se alistado á {falta} anos')
