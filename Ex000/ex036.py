from time import sleep
print('\033[32m=\033[m'*48)
print(" "*12, '\033[31m EMPRÉSTIMO BANCÁRIO\n '
      'PARA FAZER A SUA CONSULTA INFORME OS SEUS DADOS\033[m')
print('\033[32m=\033[m'*48)
nome = str(input('Informe o seu nome: '))
casa = float(input('Qual o valor da casa que você quer comprar: R$'))
salario = float(input('Qual o seu salario: '))
tempo = float(input('Você quer pagar essa casa em quantos anos: '))*12
print('AVALIANDO SEU PERFIL...')
sleep(2)
if casa/tempo <= salario * 30/100:
    print(f'\033[36mParabens \033[33m{nome}\033[36m seu empréstimo foi aprovado!!\033[m')
    print(f'\033[35mVocê vai pagar\033[33m R${casa/tempo:.2f}\033[35m mensais, durante \033[33m{tempo/12:.0f} \033[35manos\033[m')
else:
    print(f'\033[33m{nome}\033[31m Seu empréstimo foi negado.\033[m')
print('\033[36mTenha um bom dia!!\033[m')



