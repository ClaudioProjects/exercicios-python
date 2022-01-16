nome = input('Digite o seu nome: ')
#nome1 = nome.upper()
#nome2 = 'SILVA' in nome1
#print(f'Seu nome tem Silva? {nome2}')
nome1 = nome.upper().split()
print(f'Seu nome tem Silva: {"SILVA" in nome1}')