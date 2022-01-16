from time import sleep

cores = {'limpa': '\033[m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'magenta': '\033[35m',
         'cyan': '\033[36m',
         'grey': '\033[37m'}
print(f'{cores["magenta"]}={cores["limpa"]}' * 21)
print(f'{cores["yellow"]}COMPARADOR DE NÚMEROS{cores["limpa"]}')
print(f'{cores["magenta"]}={cores["limpa"]}' * 21)
n1 = int(input(f'{cores["red"]}Digite o primeiro valor: {cores["limpa"]}'))
n2 = int(input(f'{cores["red"]}Digite o segundo valor: {cores["limpa"]}'))
print(f'{cores["yellow"]}COMPARANDO...{cores["limpa"]}')
sleep(1)
if n1 > n2:
    print(
        F'{cores["cyan"]}{n1}{cores["limpa"]} {cores["yellow"]}É MAIOR QUE{cores["limpa"]} {cores["cyan"]}{n2}{cores["limpa"]}\n' 
        f'{cores["yellow"]}O PRIMEIRO VALOR É MAIOR!!.{cores["limpa"]}')
elif n1 == n2:
    print(
        f'{cores["cyan"]}{n1}{cores["limpa"]}{cores["yellow"]} E {cores["limpa"]}{cores["cyan"]}{n2}{cores["limpa"]} {cores["yellow"]}SÃO IGUAIS!!.{cores["limpa"]}')
else:
    print(
        f'{cores["cyan"]}{n2}{cores["limpa"]} {cores["yellow"]}É MAIOR QUE{cores["limpa"]} {cores["cyan"]}{n1}{cores["limpa"]}{cores["yellow"]}.{cores["limpa"]}\n'
        f'{cores["yellow"]}O SEGUNDO VALOR É MAIOR!!.{cores["limpa"]}')
print(f'{cores["magenta"]}TENHA UM BOM DIA!!{cores["limpa"]}')
