a = str(input('Digite algo: '))
print(f'Qual é seu tipo primitivo desse valor {type(a)}')
print(f'Só tem espaço ?{a.isspace()}')
print(f'È um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'È alfanúmerico? {a.isalnum()}')
print(f'Está em maiúsculo? {a.isupper()}')
print(f'Está em minúsculo? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')



