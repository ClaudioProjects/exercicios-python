cores = {'limpa': '\033[m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'magenta': '\033[35m',
         'cyan': '\033[36m',
         'grey': '\033[37m'}
print(f'{cores["green"]}CALCULADOR DE IMC{cores["limpa"]}')
peso = float(input('Quanto você pesa: '))
altura = float(input('Qual sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    sit = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    sit = 'PESO IDEAL'
elif 25 <= imc < 30:
    sit = 'ACIMA DO PESO'
elif 30 <= imc < 40:
    sit = 'OBESIDADE'
else:
    sit = 'OBESIDADE MÓRBIDA'
print(f'{cores["magenta"]}Seu ÍNDICE DE MASSA CORPORAL é de:{cores["limpa"]} {cores["blue"]}{imc:.2f}{cores["limpa"]}')
print(f'{cores["magenta"]}Seu imc indica que você esta:{cores["limpa"]} {cores["blue"]}{sit}{cores["limpa"]}')

