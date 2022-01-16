termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
n = 0
while n < 10:
    print(termo, end=' -> ')
    termo += razao
    n += 1
print('Fim')
