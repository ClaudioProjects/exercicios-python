'''n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o ultimo valor: '))
tupla = (n1, n2, n3, n4)
cont = tres = 0
for c in range(0, 4):
    if tupla[c] == 9:
        cont += 1
    elif tupla[c] == 3:
        tres = 1
print(f'O numero 9 apareceu {cont} vezes')
print(f'O numero 3 apareceu na {tupla.index(3) + 1}ª posição' if tres == 1
      else 'O valor 3 não foi ditado em nenhuma posição')
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        print(f'Os valores pares digitados foram: {tupla[c]}', end=' ')'''
n = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite outro valor: ')))
# n = tuple(int(input('Digite um valor: '))((for c in range(1, 5))
print(f'Você digitou os valores {n}')
print(f'O numero 9 foi digitado {n.count(9)} vezes')
print(f'O numero 3 apareceu na {n.index(3) + 1}º posição' if 3 in n else f'O numero 3 não foi digitado')
for c in n:
    if c % 2 == 0:
        print(f'Os numeros pares são: {c}', end=' ')
