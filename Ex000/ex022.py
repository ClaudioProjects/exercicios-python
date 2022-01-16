nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculo:', nome.upper())
print('Seu nome em minúsculo:', nome.lower())
espaço = nome.count(' ')
tudo = (len(nome))
letras = tudo - espaço
print(f'Seu nome tem {letras} letras')
nome1 = (nome.split())
print(f'Seu primeiro nome tem {len(nome1[0])} letras')
