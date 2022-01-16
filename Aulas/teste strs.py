frase = input('escreva uma frase').replace(' ', '').upper()

if frase == frase[::-1]:
    print('esta frase é um palíndromo')
else:
    print('esta frase não é um palíndromo')