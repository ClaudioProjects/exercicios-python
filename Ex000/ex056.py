media = 0
homem = 0
maior = 0
menor = 0
cont = 0
for p in range(1, 5):
    print('\033[31m-' * 5, f'{p}° Pessoa', '-' * 5)
    pessoa = str(input('\033[36mNome: '))
    sexo = str(input('Sexo [M/F]: ')).stirp().upper()
    idade = int(input('Idade: \033[m'))
    media += idade / 4
    if sexo == 'M':
        if idade >= maior:
            maior = idade
            homem = pessoa
            cont += 1
    elif sexo == 'F':
        if idade <= 20:
            menor += 1
print(f'\033[34mA medida de idade do grupo é {media:.2f} anos.')
if cont == 1:
    print(f'O homem mais velho se chama {homem} e tem {maior} anos.')
elif cont > 1:
    print(f'O grupo tem {cont} homens com {maior} anos.')
else:
    print('Não tem nenhum homem no grupo.')
if menor == 1:
    print(f'Ao todo tem {menor} mulher com menos de 20 anos.')
elif menor > 1:
    print(f'Ao todo são {menor} mulheres com menos de 20 anos.')
else:
    print('Não tem mulheres com menos de 20 anos no grupo')
