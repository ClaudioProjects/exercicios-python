valor = list()
par = list()
impar = list()
while True:
    valor.append(int(input('Digite um valor: ')))
    continua = str
    while continua != 'N' and continua != 'S':
        continua = str(input('Quer continuar: [S/N] ')).strip().upper()
    if continua == 'N':
        break
for i, z in enumerate(valor):
    if z % 2 == 0:
        par.append(z)
    else:
        impar.append(z)
print(f'A lista completa é {sorted(valor)}')
print(f'A lista dos números pares é {sorted(par)}')
print(f'A lista dos números impares é {sorted(impar)}')
