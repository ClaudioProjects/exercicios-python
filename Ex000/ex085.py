lista = [[], []]
for c in range(1, 8):
    dado = int(input(f'Digite {c}° valor: '))
    if dado % 2 == 0:
        lista[0].append(dado)
    else:
        lista[1].append(dado)
print(f'Os valores pares foram: {sorted(lista[0])}')
print(f'Os valores impares foram: {sorted(lista[1])}')
