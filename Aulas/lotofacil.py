from random import randint
import pygame
from time import sleep

lista = []
lista2 = []
maximo = [0]
lotofacil = [2, 3, 5, 10, 11,
             12, 15, 16, 17, 19,
             20, 21, 22, 23, 25]
acertos = tentativas = t12 = t13 = t14 = t15 = 0
while max(maximo) != 15:
    for c in range(0, 15):
        n = randint(1, 25)
        while True:
            if n in lista:
                n = randint(1, 25)
            else:
                lista.append(n)
                break
    sorted(lista)
    lista2 = sorted(lista)
    for c in range(0, 15):
        if lotofacil[c] in lista2:
            acertos += 1
    maximo.append(acertos)
    if acertos == 12:
        t12 += 1
    elif acertos == 13:
        t13 += 1
    elif acertos == 14:
        t14 += 1
    elif acertos == 15:
        t15 += 1
    acertos = 0
    lista.clear()
    lista2.clear()
    tentativas += 1
print(f"Foram {tentativas} jogos")
print(f"Dos quais {t12} tiveram 12 acertos")
print(f"Dos quais {t13} tiveram 13 acertos")
print(f"Dos quais {t14} tiveram 14 acertos")
print(f"Dos quais {t15} tiveram 15 acertos")
pygame.mixer.music.load('ex044vitoria.mp3')
pygame.mixer.music.play()
sleep(8.5)
pygame.mixer.music.stop()