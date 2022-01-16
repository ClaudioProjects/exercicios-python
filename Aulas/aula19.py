'''dicionario = {'filme': 'Star wars', 'ano': 1977, 'diretor': 'George Lucas'}
dicionario['filme'] = 'Titanic'
for k, v in dicionario.items():
    print(k, v)'''

'''estado = {'uf': 'RIO DE JANEIRO', 'sigla': 'RJ'}
estado1 = {'uf': 'SÂO PAULO', 'sigla': 'SP'}
brasil = list()
brasil.append(estado)
brasil.append(estado1)'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()