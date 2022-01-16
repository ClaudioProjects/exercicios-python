print('Detector de POLÍNDROMOS')
nome = input('escreva uma frase: ').replace(' ', '').upper()
if nome == nome:
    fim = 'É'
else:
    fim = 'Não é'
print(f'A frase: {nome}. \n'
      f'{fim} um POLÍNDROMO')
