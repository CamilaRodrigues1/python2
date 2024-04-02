print('='*30)
print('           Tabuada')
print('='*30)
while True:
    print('=' * 30)
    num = int(input('qual é o número? '))
    if num <= 0:
        break
    for c in range(1, 11):
        print(f'{num} x {num*c:2} = {num*c}')
print('fim..................')
print('='*30)
