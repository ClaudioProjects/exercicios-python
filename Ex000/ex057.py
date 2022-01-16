sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
