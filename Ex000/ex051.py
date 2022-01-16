an = int(input('Peimeiro termo: '))
r = int(input('Razão: '))
decimo = an + (10 - 1) * r
for c in range(an, decimo, r):
    print(c, end=' -> ')
print('Acabou')
