"""def leiaint(x):
    valor = str(input(x))
    if valor.isnumeric():
        valor = int(valor)
    else:
        while True:
            print('\033[31mNumero errado tente novamente\033[m')
            valor = str(input(x))
            if valor.isnumeric():
                valor = int(valor)
                break
    return valor


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')"""


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERROR! Numero invalido tente novamente\033[m')
        if ok is True:
            break
    return valor


x = leiaint('Digite um numero: ')
print(f'O numero que você digitou doi {x}')
