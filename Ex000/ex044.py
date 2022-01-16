cores = {'limpa': '\033[m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'magenta': '\033[35m',
         'cyan': '\033[36m',
         'grey': '\033[37m'}
print(f'{cores["cyan"]}SERVIÇO DE PAGAMENTO{cores["limpa"]}')
preço = float(input(f'{cores["yellow"]}Qual o valor do produto: R${cores["limpa"]}'))
print(f'{cores["yellow"]}Formas de pagamento:\n{cores["limpa"]}'
      f'{cores["yellow"]}A VISTA DINHEIRO/CHEQUE DIGITE COM 10% DE DESCONTO: 0\n{cores["yellow"]}'
      f'{cores["yellow"]}A VISTA CARTÃO DIGITE COM 5% DE DESCONTO: 1\n{cores["limpa"]}'
      f'{cores["yellow"]}PARCELADO 2X NO CARTÃO SEM JUROS DIGITE: 2\n{cores["limpa"]}'
      f'{cores["yellow"]}PARCELADO 3X OU MAIS NO CARTÃO COM 20% DE JEROS DIGITE: 3{cores["limpa"]}')
pag = int(input(f'{cores["cyan"]}Qual vai ser a forma de pagamento: {cores["limpa"]}'))
if pag == 3:
    parcela = int(input('VOCÊ QUER PARCELAR DE QUANTAS VEZES: '))
    k = (preço * 120 / 100) / parcela
    l = 'VOCÊ ESCOLHEU PARCELAR DE 3X NO CARTÃO COM 20% DE JUROS'
elif pag == 0:
    k = preço - (preço * 10 / 100)
    l = 'VOCÊ ESCOLHEU A VISTA DINHEIRO/CHEQUE COM 10% DE DESCONTO'
elif pag == 1:
    k = preço - (preço * 10 / 100)
    l = 'VOCÊ ESCOLHEU A VISTA CARTÃO COM 5% DE DESCONTO'
elif pag == 2:
    k = preço
    l = 'VOCÊ ESCOLHEU PARCELAR DE 2X NO CARTÃO SEM JUROS'
else:
    k = 'ERROR'
    l = 'ERROR'
print(f'{cores["green"]}{l}{cores["limpa"]}')
print(f'{cores["green"]}O PREÇO TOTAL VAI FICAR EM{cores["limpa"]} {cores["blue"]}R${k:.2f}{cores["limpa"]}')
