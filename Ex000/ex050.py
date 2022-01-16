s = 0
cont = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c} valor: '))
    if numero % 2 == 0:
        s += numero
        cont = cont + 1
print(f'A soma somente dos {cont} valores pares é {s}')
