from time import sleep


def lista(x,msg):
    print(x * 35)
    print(msg)
    print(x * 35)


while True:
    lista('\033[97:43m~', 'Sistema de ajuda PyHelp')
    func = input('\033[mFunção ou Biblioteca > ')
    lista('\033[97:44m~', f'Acessando o manual do comando <{func}>')
    sleep(1)
    print('\033[30:107m')
    help(func)
    if func == 'fim':
        break
