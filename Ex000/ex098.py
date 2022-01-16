from time import sleep


def contador(a, b, c):
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


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
