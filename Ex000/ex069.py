cont18 = homem = mulher = 0
while True:
    print('~' * 19)
    print('CADASTRE UMA PESSOA')
    print('~' * 19)
    idade = int(input('Idade: '))
    sexo = conf = str
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        cont18 += 1
    if sexo in 'M':
        homem += 1
    if sexo in 'F' and idade < 20:
        mulher += 1
    print('~' * 21)
    while conf not in 'SN':
        conf = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if conf == 'N':
        break
print(f'Foram cadastradas {cont18} pessoas maiores de 18 anos')
print(f'Foram cadastrados {homem} homens')
print(f'Foram cadastradas {mulher} mulher com menos de 20 anos')
