km = float(input('Digite quantos KM de distancia tem a sua viagem: '))
'''if km <=200:
    print(f'Sua viagem é curta, vai custar R${km * 0.5:.2f}')
else:
    print(f'Sua viagem é longa, vai custar R${km * 0.45:.2f}')'''
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print(f'Sua viagem vai custar R${preço:.2f}')