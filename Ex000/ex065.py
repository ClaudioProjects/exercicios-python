resposta = str
media = somamedia = maior = menor = 0
while resposta != 'N':
    num = int(input('\033[34mDigite um valor: '))
    media += 1
    somamedia += num
    if media == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    resposta = str(input('\033[37mQuer continuar? \033[33m[S/N] ')).upper()
print(f'\033[35mForam digitados {media} valores, a media entre eles foi: {somamedia / media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
