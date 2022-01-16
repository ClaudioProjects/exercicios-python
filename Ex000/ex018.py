from math import radians, cos, sin, tan
n = int(input('Digite o angulo que você deseja: '))
e1 = cos(radians(n))
e2 = sin(radians(n))
e3 = tan(radians(n))
print(f'Cos de {n}: {e1:.2f}\nSen de {n}: {e2:.2f}\nTan de {n}: {e3:.2f}')