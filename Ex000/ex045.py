from time import sleep
import pygame
from random import randint

pygame.init()
cores = {'limpa': '\033[m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'magenta': '\033[35m',
         'cyan': '\033[36m',
         'grey': '\033[37m'}
print(f'{cores["blue"]}*-{cores["limpa"]}'*18)
print(f'{cores["yellow"]}VAMOS JOGAR PEDRA, PAPEL E TESOURA?{cores["limpa"]}')
print(f'{cores["blue"]}*-{cores["limpa"]}'*18)
# 1 == pedra 2 == papel 3 == tesoura#
print(f'{cores["yellow"]}-*{cores["limpa"]}'*16)
print(' '*10, f'{cores["red"]}COMO JOGAR:{cores["limpa"]}')
print(' '*5, f'{cores["magenta"]}DIGITE 1 PARA PEDRA{cores["limpa"]}')
print(' '*5, f'{cores["magenta"]}DIGITE 2 PARA PAPEL{cores["limpa"]}')
print(' '*5, f'{cores["magenta"]}DIGITE 3 PARA TESOURA{cores["limpa"]}')
print(f'{cores["yellow"]}-*{cores["limpa"]}'*16)
bot = randint(1, 3)
you = int(input(f'{cores["cyan"]}DIGITE O NUMERO REFERENTE AO QUE VOCÊ VAI JOGAR: {cores["limpa"]}'))
print(f'{cores["grey"]}BOT- ESTOU PENSANDO EM NUMERO...{cores["limpa"]}')
sleep(2)
print(f'{cores["grey"]}BOT- PENSEI{cores["limpa"]}')
sleep(0.5)
if bot == 1 and you == 2:
    sit = "VITORIA"
elif bot == 2 and you == 1:
    sit = "DERROTA"
# papel win#
elif bot == 2 and you == 3:
    sit = "VITORIA"
elif bot == 3 and you == 2:
    sit = "DERROTA"
# tesoura win#
elif bot == 1 and you == 3:
    sit = "DERROTA"
elif bot == 3 and you == 1:
    sit = "VITORIA"
# pedra win#
else:
    sit = "EMPATE"
if you == 1:
    you = "PEDRA"
elif you == 2:
    you = "PAPEL"
elif you == 3:
    you = "TESOURA"
if bot == 1:
    bot = "PEDRA"
elif bot == 2:
    bot = "PAPEL"
elif bot == 3:
    bot = "TESOURA"
print(f'{cores["red"]}BOT JOGOU:{cores["limpa"]} {cores["yellow"]}{bot}{cores["limpa"]}')
print(f'{cores["blue"]}VOCÊ JOGOU:{cores["limpa"]} {cores["yellow"]}{you}{cores["limpa"]}')
sleep(1)
if sit == "VITORIA":
    print(f'{cores["magenta"]}O RESULTADO FOI:{cores["limpa"]} {cores["green"]}{sit}!!{cores["limpa"]}')
    pygame.mixer.music.load('ex044vitoria.mp3')
    pygame.mixer.music.play()
    sleep(8.5)
    pygame.mixer.music.stop()
elif sit == "EMPATE":
    print(f'{cores["magenta"]}O RESULTADO FOI:{cores["limpa"]} {cores["grey"]}{sit}{cores["limpa"]}')
    pygame.mixer.music.load('ex044empate.mp3')
    pygame.mixer.music.play()
    sleep(10.5)
    pygame.mixer.music.stop()
else:
    print(f'{cores["magenta"]}O RESULTADO FOI:{cores["limpa"]} {cores["red"]}{sit}{cores["limpa"]}')
    pygame.mixer.music.load('ex044derrota.mp3')
    pygame.mixer.music.play()
    sleep(10)
    pygame.mixer.music.stop()


