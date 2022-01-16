def moeda(val):
    x = (str(f'R${val:.2f}'))
    z = x.replace('.', ',')
    return z


def metade(val, sit=False):
    result = val / 2
    if sit:
        result = moeda(result)
    return result


def dobro(val, sit=False):
    result = val * 2
    if sit:
        result = moeda(result)
    return result


def aumentar(val, p, sit=False):
    result = (val * (p + 100)) / 100
    if sit:
        result = moeda(result)
    return result


def reduzir(val, p, sit=False):
    result = (val * (100 - p)) / 100
    if sit:
        result = moeda(result)
    return result


def resumo(val, a, d):
    lista = {'Preço Analisado: ': moeda(val),
             'Dobro do Preço: ': dobro(val, sit=True),
             'Metade do Preço: ': metade(val, sit=True),
             f'Aumento de {a}%: ': aumentar(val, a, sit=True),
             f'Redução de {d}%: ': reduzir(val, d, sit=True)}
    print('—' * 35)
    print(f'{"RESUMO DE VALORES":^35}')
    print('—' * 35)
    for p, v in lista.items():
        print(f'{p:<20}{v:<20}')
    print('—' * 35)