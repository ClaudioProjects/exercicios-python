lista = list()
media = 0
while True:
    pessoa = dict()
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    pessoa['Idade'] = int(input('Idade: '))
    media += pessoa['Idade']
    lista.append(pessoa[:])
    del pessoa
    continua = str
    while continua != 'N' and continua != 'S':
        continua = str(input('Quer continuar: [S/N] ')).strip().upper()
    if continua == 'N':
        break
print('-=' * 35)
media = media / len(lista)
print(f'—Foram cadastradas {len(lista)} pessoas.')
print(f'—A media de idade do grupo foi de {media:.1f}.')
print('—As mulheres cadastradas foram:', end=' ')
for i, v in enumerate(lista):
    if v['Sexo'] == 'F':
        print(v['Nome'], end=' ')
print()
print('As pessoas com idade acima da media cadastradas foram:')
for i, v in enumerate(lista):
    if v['Idade'] > media:
        print(v)
print('<<<ENCERRADO>>>')
