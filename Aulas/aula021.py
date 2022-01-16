from time import sleep


def contador(a, b, c):
    """
    Faz uma contagem e mostra na tela
    Começa no 'A'
    termina no 'B'
    Tem o intervalo de 'c'
    """
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print('-=' * 25)
    print('Analisando os valores')
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont += c
        print('Fim')
    else:
        cont = a
        while cont >= b:
            print(cont, end=' ')
            sleep(0.2)
            cont -= c
        print('Fim')

help(contador)


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = soma(7, 2)
r2 = soma(1)
print(f' As somas valem {r1} e {r2}')
#Escopo de variavel


def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
função()
print(f'N1 fora vale {n1}')