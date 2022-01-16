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
