import math
c1 = float(input('Informe a medida do cateto oposto: '))
c2 = float(input('Informe a medida do cateto adjacente: '))
#c3 = math.sqrt(math.pow(c1, 2) + math.pow(c2, 2))
c3 = math.hypot(c1, c2)
print(f'A hipotenusa mede {c3:.2f}')