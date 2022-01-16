from random import randint

tuplas = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram:', end=' ')
for c in tuplas:
    print(c, end=' -> ')
print(f'Fim\nO maior valor sorteado foi {max(tuplas)}\n'
      f'O menor valor sorteado foi {min(tuplas)}')
