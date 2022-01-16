from time import sleep
import pygame

print('CONTAGEM REGRESSIVA!! ')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('EVACUAR IMEDIATAMENTE!!')
pygame.init()
pygame.mixer.music.load('ex046.mp3')
pygame.mixer.music.play()
sleep(8)
pygame.mixer.music.stop()