from math import radians,cos, tan, sin
num = int(input('Digite o valor do ângulo que deseja:  '))
a = radians(num)
print(f'''O ângulo de {num} tem o SENO de {sin(a):.2f}
O ângulo  de {num} tem o COSSENO de {cos(a):.2f}
O ângulo de {num} tem a TANGENTE  de {tan(a):.2f}''')
