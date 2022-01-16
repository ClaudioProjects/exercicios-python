'''print('\033[34m=' * 30)
print(' ' * 9, 'BANCO CEV')
print('=' * 30)
saque = int(input('\033[36mQuanto você quer sacar: R$ '))
nota1 = saque // 50
restante1 = (saque % 50)
nota2 = restante1 // 20
restante2 = (restante1 % 20)
nota3 = restante2 // 10
restante3 = (restante2 % 10)
nota4 = restante3
if nota1 > 0:
    print(f'\033[35mTotal de {nota1} cédulas de R$50.00')
if nota2 > 0:
    print(f'\033[33mTotal de {nota2} cédulas de R$20.00')
if nota3 > 0:
    print(f'\033[31mTotal de {nota3} cédulas de R$10.00')
if nota4 > 0:
    print(f'\033[32mTotal de {nota4} cédulas de R$1.00')
print('\033[34m=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Qual o valor você quer sacar: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'O total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')