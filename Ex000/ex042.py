cores = {'l': '\033[m',
         'r': '\033[31m',
         'g': '\033[32m',
         'y': '\033[33m',
         'b': '\033[34m',
         'm': '\033[35m',
         'c': '\033[36m',
         'grey': '\033[37m'}
print(f'{cores["magenta"]}ANALISADOR DE TRIANGULOS{cores["limpa"]}')
seg1 = float(input('Digite o valor do primeiro segmento: '))
seg2 = float(input('Digite o valor do segundo segmento: '))
seg3 = float(input('Digite o valor do terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    pord = 1
    sit1 = 'VOCÊ PODE'
else:
    pord = 0
    sit1 = 'VOCÊ NÃO PODE'
print(f'{cores["cyan"]}{sit1} FORMAR UM TRIANGULO COM ESSES SEGMENTOS{cores["limpa"]}')
if seg1 == seg2 and seg2 == seg3 and pord == 1:
    sit = 'EQUILÁTERO'
elif seg1 == seg2 or seg2 == seg3 and pord == 1:
    sit = 'ISÓSCELES'
else:
    sit = 'ESCALENO'
if pord == 1:
    print(f'{cores["blue"]}O SEU TRIANGULO É {sit}{cores["limpa"]}')
else:
    print('TENTE NOVAMENTE')
