'''lista = [[], [], []]
for c in range(0, 9):
    if c <= 2:
        lista[0].append(int(input(f'Digite um valor para a posição {[0, len(lista[0])]}: ')))
    elif c <= 5:
        lista[1].append(int(input(f'Digite um valor para a posição {1, len(lista[1])}: ')))
    else:
        lista[2].append(int(input(f'Digite um valor para a posição {2, len(lista[2])}: ')))
for p in range(0, 3):
    print(f'[ {lista[0][p]} ]', end=' ')
print()
for p in range(0, 3):
    print(f'[ {lista[1][p]} ]', end=' ')
print()
for p in range(0, 3):
    print(f'[ {lista[2][p]} ]', end=' ')'''

lista = [[], [], []]
for c in range(0, 3):
    for l in range(0, 3):
        lista[c].append(int(input(f'Digite um valor para a posição: [{c, l}] ')))
print('-=' * 30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[ {lista[c][l]:^5} ]', end=' ')
    print()
