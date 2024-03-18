pago = float(input('QUAL É O VALOR DAS COMPRAS ?R$ '))
print('''COMO VAI SER O PAGAMENTO
[1]Á VISTA DINHEIRO / PIX
[2]Á VISTA NO CARTÃO
[3]EM ATE 2X NO CARTÃO
[4]3X OU MAIS NO CARTÃO''')
resp = int(input('Qual é a opção de pagamento? '))
print(f'A SUA COMPRA FOI DE R${pago:.2f}')
if resp == 1:
    preco = pago - (pago*10/100)
    print(f'À vista no dinheiro/pix você terá 10% de desconto,e pagará R${preco:.2f} ')
elif resp == 2:
    preco = pago - (pago*5/100)
    print(f'À vista no cartão você terá 5% de desconto e pagará no valor final R${preco:.2f}')
elif resp == 3:
    print(f'Você pagará o valor normal parcelado de  2x R${pago/2:.2f}')
elif resp == 4:
    pa = int(input('Quantas parcelas?'))
    preco = pago+(pago*20/100)
    parcela = preco / pa
    print(f'Você pagará 20% de juros a suas compras ficara R${preco:.2f} e parcelado de {pa}x cada parcela vai ser de R${parcela:.2f}')
else:
    print('Opção inválida ,tente novamente.')
