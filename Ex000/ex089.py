lista = []
dados = list()
cont = 0
while True:
    lista.append([])
    lista[cont].append(str(input('Nome: ')))
    dados.append(float(input('Primeira nota: ')))
    dados.append(float(input('Segunda nota: ')))
    lista[cont].append(dados[:])
    dados.clear()
    cont += 1
    continua = str
    while continua != 'N' and continua != 'S':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break
print('-=' * 25)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for c, i in enumerate(lista):
    media = 0
    print(f'{c:<4}{lista[c][0]:<10}', end='')
    for z in range(0, 2):
        media += (lista[c][1][z]) / 2
    print(f'{media:>8.1f}')
print('-' * 26)
while True:
    z = int(input('Mostrar nota de qual alunos? [999 INTERROMPE] '))
    print(f'Notas de {lista[z][0]} são {lista[z][1]}')
    print('~' * 27)
    if z == 999:
        break
