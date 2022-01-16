from random import randint

print('*' * 24)
print('VAMOS JOGAR PAR OU IMPAR')
print('*' * 24)
sit = str
v = 0
while True:
    print('=-' * 15)
    pc = randint(0, 10)
    n = int(input('Digite um valor: '))
    escolha = ' '
    soma = pc + n
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador jogou {pc}. TotaL foi de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!!')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU!!')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'Game over você venceu {v} vezes!')
