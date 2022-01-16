from random import randint
from time import sleep
print('-*-' * 10)
print('Vou pensar em um numero entre 0 e 5')
print('-*-' * 10)
n = int(input('Digite um numero entre 0 e 5: '))
n1 = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if n == n1:
    print('Acerto viado véi!!')
else:
    print('Erro mula manca!!')
print('FIM.')
