from random import randint
import pygame
from time import sleep


pygame.init()
cores = {'limpa': '\033[m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'magenta': '\033[35m',
         'cyan': '\033[36m',
         'grey': '\033[37m'}



# 1 == pedra 2 == papel 3 == tesoura#
bot = randint(1, 3)
you = int(input(':'))
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
    sit = "VITORIA"
elif bot == 3 and you == 1:
    sit = "DERROTA"
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
if sit == "VITORIA":
    pygame.mixer.music.load('ex044vitoria.mp3')
    pygame.mixer.music.play()
    sleep(8.5)
    pygame.mixer.music.stop()
elif sit == "EMPATE":
    pygame.mixer.music.load('ex044empate.mp3')
    pygame.mixer.music.play()
    sleep(10.5)
    pygame.mixer.music.stop()
else:
    pygame.mixer.music.load('ex044derrota.mp3')
    pygame.mixer.music.play()
    sleep(10)
    pygame.mixer.music.stop()


