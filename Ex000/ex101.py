def voto(x):
    from datetime import date

    ano = date.today().year
    data = ano - x
    if data < 18:
        s = [data, 'NEGADO']
        return s
    elif data < 65:
        s = [data, 'OBRIGATÓRIO']
        return s
    else:
        s = [data, 'OPCIONAL']
        return s


z = int(input('Em que ano você nasceu: '))
c = voto(z)
print(f'Com {c[0]} anos o voto é {c[1]}')
