print('—' * 35)
print('Controlador de terrenos')
print('—' * 35)


def area(a, b):
    s = a * b
    print(f'A de um terreno {a} * {b} é de {s}m²')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
