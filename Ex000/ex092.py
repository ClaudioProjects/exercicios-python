import datetime

ano = datetime.date.today().year
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
pessoa['Idade'] = (int(input('Ano de nascimento: ')) - ano) * -1
pessoa['CTPS'] = int(input('Carteira de Trabalho: (0 não tem) '))
if pessoa['CTPS'] > 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salario'] = float(int(input('Salario: ')))
    idade = pessoa['Idade'] + (35 - (ano - pessoa['Contratação']))
    pessoa['Aposentadoria'] = idade
for k, v in pessoa.items():
    print(f'—{k} tem o valor de {v}')
