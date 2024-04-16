nomepro = ('Lápis', 1.75,
           'Borracha', 2.00,
           'Caderno', 15.90,
           'Estojo', 25.00,
           'Trasnferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.32,
           'Canetas', 22.30,
           'Livro', 34.90)
print(f'{'LISTAGEM DE PRODUTO':>30}')
print('=-'*30)
for c in range(0, len(nomepro)):
    if c % 2 == 0:
        print(f'{nomepro[c]:.<30}', end='')
    else:
        print(f'R${nomepro[c]:>7.2f}')
print('=-'*30)
