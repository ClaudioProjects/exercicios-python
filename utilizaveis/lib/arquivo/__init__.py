from utilizaveis.lib.interface import cabeçalho


def validafile(arg):
    try:
        a = open(arg, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criafile(arg):
    try:
        a = open(arg, 'wt+')
        a.close()
    except Exception as error:
        print(f'<{error}>Houve um erro na criação do programa')
    else:
        print(f'Arquivo {arg} criado com sucesso!')


def lerfile(arg):
    try:
        a = open(arg, 'rt')
    except Exception as error:
        print(f'<{error}> Houve um erro na leitura do programa')
    else:
        cabeçalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>6} anos')
    finally:
        a.close()


def cadastro(arg, nome='Desconhecido', idade=0):
    try:
        a = open(arg, 'at')
    except Exception as error:
        print(f'<{error}> Houve um erro na hora de cadastrar')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except Exception as error:
            print(f'<{error}> houve um erro no arquivo')
        else:
            print(f'Novo registro de {nome}')
