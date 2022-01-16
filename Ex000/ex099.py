from time import sleep


def maior(*valores):
    print('-=' * 25)
    print('Analisando os valores processados...')
    for c in valores:
        print(c, end=' ')
        sleep(0.3)
    print(f'Foram informados ao todo {len(valores)} valores')
    print(f'O maior valor informado foi {max(valores)}' if len(valores) > 0 else'O maior valor informado foi 0')


maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
