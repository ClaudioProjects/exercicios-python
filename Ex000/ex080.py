'''valor = list()
valor1 = list()
valor2 = list()
for c in range(0, 5):
    valor.append(int(input('Digite um valor: ')))
    if valor[c] == max(valor):
        print('Valor adicionado ao fim da lista')
        valor1.insert(-1, valor[c])
    elif valor[c] == min(valor):
        valor1.insert(0, valor[c])
        print(f'Valor adicionado na posição 0')
    else:
        for i, z in enumerate(valor1):
            if valor[c] < z:
                valor2.append(valor1.index(z))
        valor1.insert(min(valor2), valor[c])
        print(f'Valor adicionador na posição {valor1.index(valor[c])}')
        del valor2[0:]
print(valor1)'''
lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado no fim da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem são {lista}')
