'''valor = list()
valor.append(str(input('Digite uma expressão: ')))
if valor[0][0] == '(':
    if valor.count('(') % 2 == 0 and valor.count(')') % 2 == 0:
        print('Sua expressão esta correta!!')
else:
    print('Sua expressão esta errada!')'''
valor = str(input('Digite uma expressão: '))
pilha = list()
for simb in valor:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta correta...')
else:
    print('Sua expressão é invalida...')
