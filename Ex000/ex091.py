from random import randint
from time import sleep
from operator import itemgetter

jogador = dict()
cont = 0
for c in range(0, 4):
    cont += 1
    jogador[f'Jogador {cont}'] = int(randint(1, 6))
print('Sorteando Valores')
ranking = list()
for k, v in jogador.items():
    print(f'{k} tirou {v}')
    sleep(0.3)
print('-=' * 5, 'Ranking', '-=' * 5)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}° Lugar: {v[0]} com {v[1]}')
    sleep(0.2)

