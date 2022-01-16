from datetime import date
ano = int(input('Digite um ano? Ou digite 0 para saber do ano atual? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!!')
else:
    print(f'{ano} Não é um ano bissexto!!')