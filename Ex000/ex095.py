lista = list()
while True:
    pessoa = dict()
    gols = list()
    total = 0
    pessoa['Nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {pessoa["Nome"]} jogou: '))
    for c in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {c}: ')))
        total += gols[c]
    pessoa['Gols'] = gols
    pessoa['Total'] = total
    lista.append(pessoa.copy())
    del pessoa, gols
    continua = str
    while continua != 'S' and continua != 'N':
        continua = str(input('Quer continuar: [S/N] ')).strip().upper()
    if continua == 'N':
        break
print('-=' * 35)
print(f'{"Cod":<4}{"Nome":<20}{"Gols":<21}{"Total"}')
for i, v in enumerate(lista):
    print(f'{i:<4}{v["Nome"]:<20}{v["Gols"]!s:<21}{v["Total"]}')
x = 0
while x != 999:
    print('—' * 30)
    x = int(input('Mostra dados de qual jogador: '))
    if len(lista) - 1 >= x >= 0:
        print(f'--Levantamento do Jogador {lista[x]["Nome"]}--')
        for c in range(0, len(lista[x]['Gols'])):
            print(f'— Na partida {c}, Fez {lista[x]["Gols"][c]} gols.')
        print(f'Foi total de {lista[x]["Total"]} gols')
    else:
        print('Numero invalido!!. Tente novamente')
