def dado(msg):
    valido = False
    while valido is False:
        n = str(input(msg)).strip()
        z = n.replace(',', '.')
        y = z.replace('.', '')
        print(z)
        if y.isnumeric() is True:
            valido = True
            z1 = float(z)
            return z1
        else:
            print(f'\033[31m<{z}> NÂO É UM NÚMERO VALIDO\033[m')
