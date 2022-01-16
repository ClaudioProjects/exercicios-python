from datetime import date

cores = {'limpa': '\033[m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'magenta': '\033[35m',
         'cyan': '\033[36m',
         'grey': '\033[37m'}
print(f'{cores["green"]}_{cores["limpa"]}'*19)
print(f'{cores["yellow"]}ALISTAMENTO MILITAR{cores["limpa"]}')
print(f'{cores["green"]}_{cores["limpa"]}'*19)
ano = int(input(f'{cores["magenta"]}informe o ano do seu nascimento: {cores["limpa"]}'))
ano1 = date.today().year - ano
if ano1 == 18:
    print(f'{cores["green"]}JA É HORA DE SE ALISTAR!!{cores["limpa"]}')
elif ano1 > 18:
    print(f'{cores["red"]}JA PASSOU DO TEMPO DE SE ALISTAR\n{cores["limpa"]}'
          f'{cores["red"]}VOCÊ DEVIA TER SE ALISTADO A {ano1 - 18} ANO(S){cores["limpa"]}')
else:
    print(f'{cores["cyan"]}VOCÊ AINDA NÃO PODE ALISTAR\n{cores["limpa"]}'
          f'{cores["cyan"]}VOCÊ VAI SE SE ALISTAR DAQUI {18 - ano1} ANOS(S){cores["limpa"]}')
