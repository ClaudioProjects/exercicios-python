lista = [[], [], []]
result = soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l].append(int(input(f'Digite um valor para a posição [{l, c}]: ')))
        if lista[l][c] % 2 == 0:
            result += lista[l][c]
        if c == 2:
            soma += lista[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {lista[l][c]:^5} ]', end=' ')
    print()
print(f'A soma dos valores pares é {result}')
print(f'A soma dos valores da terceira coluna foi: {soma}')
print(f'O maior valor da terceira linha foi {max(lista[1])}')
