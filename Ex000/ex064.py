c = cont = num = valor = 0
while c != 999:
    valor += 1
    c = int(input(f'Digite o {valor}° valor: '))
    if valor == 2:
        print('\033[31mPara finalizar digite: [999]\033[m')
    if c != 999:
        cont += 1
        num += c
print(f'Você digitou {cont} valores')
print(f'A soma dos valores é {num}')
