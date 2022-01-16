from time import sleep

pessoa = dict()
lista = list()
tot = 0
pessoa['Nome'] = str(input('Nome: '))
partidas = int(input(f'Quantos jogos o {pessoa["Nome"]} jogou: '))
for c in range(0, partidas):
    lista.append(int(input(f'Quantos gols na partida {c}: ')))
pessoa['Gols'] = lista[:]
pessoa['Total'] = sum(lista)
print('-=' * 35)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}.')
sleep(1)
print('-=' * 35)
print(f'O jogador {pessoa["Nome"]} tem {partidas} partidas')
for i, v in enumerate(pessoa["Gols"]):
    print(f'>> Na partida {i}, fez {pessoa["Gols"][v]} gols')
    sleep(0.5)
print(f'Foi um total de {pessoa["Total"]} gols')
print('-=' * 35)
