cont = list()
while True:
    continua = str
    valor = (int(input('Digite um valor: ')))
    if valor not in cont:
        cont.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não vou adicionar...')
    while continua != 'S' and continua != 'N':
        continua = str(input('Quer continuar: [S/N] ')).strip().upper()
    if continua == 'N':
        break
print(f'Você digitou os valores {sorted(cont)}')
