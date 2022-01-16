valor = list()
cont = 0
while True:
    valor.append(int(input('Digite um valor: ')))
    continua = str
    cont += 1
    while continua != 'S' and continua != 'N':
        continua = str(input('Quer continuar: [S/N] ')).strip().upper()
    if continua == 'N':
        break
valor.sort(reverse=True)
print('-=' * 20)
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decrescente são {valor}')
if 5 in valor:
    print('O numero 5 foi encontrado na lista!!')
else:
    print('O numero 5 não foi encontrado na lista.')
