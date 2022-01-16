def fatorial(valor, show=False):
    """
    Calcula o fatorial de <Valor>
    Valor: Recebe um valor.
    Show: Recebe um valor boolean, se for True Mostra a operação.
    """
    print(f'{valor} X ' if show is True else'O seu resultado é ', end='')
    for c in range(valor - 1, 0, -1):
        if show is True:
            print(f'{c} X ' if c > 1 else f'{c} = ', end='')
        valor *= c
    return valor


print(fatorial(5, show=False))
