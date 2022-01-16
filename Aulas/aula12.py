nome = str(input('Qual é o seu nome: '))
nome1 = nome.upper()
if nome1 == 'CLAUDIO':
    print('Que nome lindo')
elif nome1 == 'GABRIEL' or nome1 == 'PEDRO' or nome1 == 'JOÃO':
    print('Seu nome é popular no Brasil')
elif nome1 in 'ANA JULIA PAULA FERNANDA LETICIA':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print(f"Tenha um bom dia\033[36m {nome}\033[m")