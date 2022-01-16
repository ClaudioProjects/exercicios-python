from utilizaveis.lib.interface import *
from utilizaveis.lib.arquivo import *
from time import sleep

arg = 'cursoemvideo.txt'
if validafile(arg) is True:
    print('Arquivo encontrado com sucesso!')
else:
    criafile(arg)
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        lerfile(arg)
    elif resp == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastro(arg, nome, idade)
    elif resp == 3:
        print('Saindo do sistema, até logo...')
        break
    else:
        print('\033[31mERROR: opção invalida\033[m')
