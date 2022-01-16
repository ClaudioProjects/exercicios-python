def leiaint(msg):
    while True:
        try:
            a = int(input(msg))
        except ValueError:
            print('\033[31mValor invalido\033[m')
        except KeyboardInterrupt:
            print('\033[31mO Usuário preferiu não digitar nenhum numero\033[m')
        except Exception as erro:
            print(f'O erro foi {erro.__cause__}')
        else:
            break
    print(f'O valor {a} foi adicionado nja lista')


def leiafloat(msg):
    while True:
        try:
            a = float(input(msg))
        except ValueError:
            print('\033[mValor invalido\033[m')
        except KeyboardInterrupt:
            print('\033[mO Usuário preferiu não digitar nenhum numero\033[m')
        except Exception as erro:
            print(f'O erro foi {erro.__cause__}')
        else:
            break
    print(f'O valor {a} foi adicionado na lista')


leiaint('Digite um numero inteiro: ')
leiafloat('Digite um numero real: ')
