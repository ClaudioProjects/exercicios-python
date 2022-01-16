print('=' * 30)
print(' ' * 5, 'LOJA SUPER BARATÃO')
print('=' * 30)
cont = total = cont2 = menor = 0
barato = str
while True:
    conf = str
    nome = str(input('Nome: '))
    valor = float(input('Preço: R$ '))
    total += valor
    if valor > 1000:
        cont += 1
    if cont2 == 0 or valor < menor:
        menor = valor
        barato = nome
    cont2 += 1
    while conf != 'S' and conf != 'N':
        conf = str(input('Quer continuar: [S/N] ')).strip().upper()
    if conf == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
