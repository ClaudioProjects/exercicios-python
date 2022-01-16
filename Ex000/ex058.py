from random import randint
palpite = 0
pc = randint(0, 10)
you = int
valor = str
while pc != you:
    you = int(input('\033[35mAdivinhe o numero que eu pensei: '))
    palpite += 1
    if you < pc:
        valor = 'Mais'
    elif you > pc:
        valor = 'Menos'
    if you != pc:
        print(f'\033[31m{valor}... Você errou tente novamente')
print('\033[32mVocê ganhou!!!\n'
      f'Você precisou de {palpite} tentativas')

'''from random import randint
computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            valor = 'Menos'
        elif jogador < computador:
            valor = 'Maior'
        print(f'{valor}... Tente novamente')
print(f'Você acertou parabens!!!')
print(f'Foram necessários {palpite} palpites ')'''