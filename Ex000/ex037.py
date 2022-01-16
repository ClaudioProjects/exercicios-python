numero = int(input('DIGITE UM NÚMERO INTEIRO: '))
print('''CONVERSOR DE NÚMEROS
[1] APERTE PARA BINÁRIO
[2] APERTE PARA OCTAL
[3] APERTE PARA HEXADECIMAL''')
option = int(input('ESCOLHA UMA OPÇÃO: '))
if option == 1:
    print(f'{numero} CONVERTIDO PARA BINÁRIO É {bin(numero)[2:]}')
elif option == 2:
    print(f'{numero} CONVERTIDO PARA OCTAL É {oct(numero)[2:]}')
elif option == 3:
    print(f'{numero}CONVERTIDO PARA HEXADECIMAL È {hex(numero)[2:]}')
else:
    print('ERROR')