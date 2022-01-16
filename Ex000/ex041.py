from datetime import date

cores = {'limpa': '\033[m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'magenta': '\033[35m',
         'cyan': '\033[36m',
         'grey': '\033[37m'}
nas = int(input('Em que ano você nasceu: '))
prod = date.today().year - nas
if prod <= 9:
    sit = 'MIRIM'
elif prod <= 14:
    sit = 'INFANTIL'
elif prod <= 19:
    sit = 'JUNIOR'
elif prod <= 20:
    sit = 'SENIOR'
else:
    sit = 'MASTER'
print(f'{cores["yellow"]}Você é um atleta de:{cores["limpa"]} {cores["blue"]}{prod} anos{cores["limpa"]}')
print(f'{cores["yellow"]}Você é considero um atleta:{cores["limpa"]} {cores["blue"]}{sit}{cores["limpa"]}')
