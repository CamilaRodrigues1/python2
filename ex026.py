frase = str(input('Digite uma frase: ')).strip()
print(f'A letra \033[33mA\033[m apareceu {frase.count('a'[0:])}')
print(f'A primeira letra \033[33mA\033[m apareceu na posição {frase.find('a'[0:])+1}')
print(f'A última letra \033[33mA\033[m apareceu na posiçao {frase.rfind('a'[:])+1}')
