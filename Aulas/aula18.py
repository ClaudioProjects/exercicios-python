'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos!!')'''

galera = list()
dado = list()
contmenor = contmaior = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade ')
        contmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        contmenor += 1
print(f'Temos {contmaior} pessoas maior de idade\n'
      f'Temos {contmenor} pessoas menor de idade')