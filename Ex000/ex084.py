lista = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    continua = str
    lista.append(dado[:])
    dado.clear()
    while continua != 'S' and continua != 'N':
        continua = str(input('Quer continuar: [S/N] ')).strip().upper()
    if continua == 'N':
        break
print(f'Ao todo foram {len(lista)} pessoas cadastradas')
print(f'O peso maior foi {maior}. O peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi {menor}. O peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
