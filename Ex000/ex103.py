def ficha():
    jogador = str(input('Nome: ')).strip()
    if len(jogador) < 1:
        jogador = '<desconhecido>'
    gols = input('Número de gols: ').strip()
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {jogador} fez {gols} gols no campeonato')


ficha()
