r1 = float(input('Diga o tamanho da primeira reta: '))
r2 = float(input('Diga o tamanho da segunda reta: '))
r3 = float(input('Diga o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os tres segmentos podem formar um triangulo')
else:
    print('Os tres segmentos não podem formar um triangulo')