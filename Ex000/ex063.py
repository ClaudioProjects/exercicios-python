print('*' * 22)
print('Sequencia de Fibonacci')
print('*' * 22)
n = int(input('Você quer ver quantos termos: '))
n2 = 0
n3 = 1
c = 0
n1 = 0
if n > 2:
    while c != n - 2:
        n1 = n2
        if c == 0:
            print(f'{n1} -> {n2}', end=' -> ')
        n2 = n3
        n3 = n1 + n2
        c += 1
        print(n3, end=' -> ')
elif n == 2:
    print(f'{n1} -> {n2}', end=' -> ')
elif n == 1:
    print(n1, end=' -> ')
print('FIM')

'''nant = 1
fibonacci = 0
n = int('Você quer ver quantos termos: ')
cont = 0
while n != 0:
    print(f'{fibonacci}', end=' -> ')
    fibonacci += nant
    nant -= fibonacci
    n -= 1
print('FIM')'''
