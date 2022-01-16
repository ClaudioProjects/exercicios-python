'''from random import randint
from time import sleep

cont = 0
palpites = int(input('Quantos jogos você quer ver: '))
for c in range(1, palpites + 1):
    lista = [randint(1, 60), randint(1, 60),randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    cont += 1
    for c in range(0, 6):
        for l in range(0, 6):
            if lista[c] == lista[l] and lista.count(lista[c]) == 2:
                lista[l] = randint(1, 60)
    print('=' * 30)
    print(f'Jogo {cont}: {sorted(lista)}')
    sleep(0.5)'''

from random import randint
from time import sleep

print('-' * 30)
print('JOGA NA MEGA SENA')
print('-' * 30)
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando Jogos', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.3)