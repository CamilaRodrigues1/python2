from datetime import date
anoatual = date.today().year


def voto():

    idade = anoatual - ano
    if idade <= 15:
        print(f'Com {idade} anos:NÃO VOTA')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: O VOTO NÂO È OBRIGATORIO')
    else:
        print(f'Com {idade} anos: O VOTO É OBRIGATORIO')


ano = int(input('Em que ano voce nasceu?'))
voto()


#gustavo guanabara
def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade <= 15:
        return f'Com {idade} anos:NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: O VOTO NÂO È OBRIGATORIO'
    else:
        return f'Com {idade} anos: O VOTO É OBRIGATORIO'


ano = int(input('Em que ano voce nasceu?'))
print(voto(ano))
