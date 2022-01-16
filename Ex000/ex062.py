termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
z = 10
cont = 1
total = 0
while z != 0:
    total += z
    while cont <= total:
        cont += 1
        print(termo, end=' -> ')
        termo += razao
    print('FIM')
    print('-=' * 17)
    z = int(input('Você quer ver mais quantos termos: '))
print(f'A progressão foi finalizada com {cont} termos!')
