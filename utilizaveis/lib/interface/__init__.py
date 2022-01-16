def linha(tam=42):
    return '\033[34m—\033[m' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('\033[32mMenu Principal\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    option = leiaint('\033[32mSua opção: \033[m')
    cabeçalho(f'Opção {option}')
    return option


def leiaint(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: valor invalido\033[m')
            continue
        except Exception as erro:
            print(f'O erro foi {erro.__cause__}')
            continue
        except KeyboardInterrupt:
            print('\033[31mERROR: usuário preferiu não digitar nenhum numero\033[m')
            return 0
        else:
            return a