soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont = cont + 1
print(f' A SOMA DE TODOS OS {cont} VALORES MÚLTIPLOS DE 1 a 500 DE 3 É {soma}')
