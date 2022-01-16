from random import randint
from time import sleep


def sorteia(lst):
    for c in range(0, 5):
        lst.append(randint(0, 10))
    print(f'Sorteando 5 valores: ', end='')
    for c in lst:
        print(c, end=' ')
        sleep(0.25)
    print()


def somapar(lst):
    par = 0
    print(f'A soma dos valores pares da lista ', end='')
    for c in lst:
        print(c, end=' ')
        if c % 2 == 0:
            par += c
    print(f': É igual a {par}')


numeros = list()
sorteia(numeros)
somapar(numeros)
