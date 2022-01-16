def linha(msg):
    print('—' * 35)
    print(f'{msg:^35}')
    print('—' * 35)


# valida o arquivo
try:
    with open('lista.txt', 'r') as arquivo:
        arquivo.read()
except FileNotFoundError:
    with open('lista.txt', 'w') as arquivo:
        arquivo.write('')
# Menu
while True:
    '''linha(f'{"MENU PRINCIPAL":^35}')
    linha('\033[32m1\033[m - \033[31mVer pessoas cadastradas\n'
          '\033[32m2\033[m - \033[31mCadastrar nova pessoa\n'
          '\033[32m3\033[m - \033[31mSair do sistema\033[m')'''
    option = 0
    while not 0 < option < 4:
        try:
            option = int(input('\033[33mSua opção: \033[m'))
        except ValueError:
            print('\033[31mValor inserido invalido, Tente novamente\033[m')
# escolhas
    if option == 1:
        with open('lista.txt', 'r') as arquivo:
            texto = arquivo.readline()
        print(texto)
    elif option == 2:
        while True:
            try:
                nome = str(input('Nome: '))
            except ValueError:
                print('\033[31mValor inserido invalido, Tente novamente\033[m')
            else:
                break
        while True:
            try:
                idade = int(input('Idade: '))
            except ValueError:
                print('\033[31mValor inserido invalido, Tente novamente\033[m')
            else:
                break
        with open('lista.txt', 'a') as arquivo:
            arquivo.write(f'{nome}')
            arquivo.write(str(f'{idade}'))
    elif option == 3:
        break
