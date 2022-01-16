cores = {'limpa': '\033[m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'magenta': '\033[35m',
         'cyan': '\033[36m',
         'grey': '\033[37m'}
print(f'{cores["blue"]}CALCULADOR DE MEDIAS{cores["limpa"]}')
nota  = float(input('Nota da primeira prova: '))
nota1 = float(input('Nota da segunda prova: '))
nota2 = (nota + nota1) / 2
if 10 >= nota2 >= 7:
    sit = 'APROVADO'
elif nota2 < 5:
    sit = 'REPROVADO'
elif nota2 > 10:
    sit = 'ERROR'
    nota2 = 'ERROR'
else:
    sit = 'RECUPERAÇÃO'
print(f'{cores["yellow"]}Sua media foi {nota2:.1f} {cores["limpa"]}')
print(f'{cores["blue"]}Seu estado: {sit}{cores["limpa"]}')
