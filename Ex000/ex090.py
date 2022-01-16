aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de aluno {aluno["Nome"]}: '))
if aluno['Media'] < 7:
    aluno['Situação'] = str('Reprovado')
else:
    aluno['Situação'] = str('Aprovado')
print('-=' * 35)
for k, v in aluno.items():
    print(f'O {k} é igual a {v}')
