'''num = [2, 5, 9, 1]
print(num)
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
num.remove(3)
print(num)'''
valor = list()
for cont in range(0, 5):
    valor.append(str(input('Digite um valor: ')))
for c, v in enumerate(valor):
    print(f'Na posição {c} achei o valor {v}')
print('Cheguei ao fim.')