from ex108pkg import moeda

p = float(input('Digite um preço: R$ '))
print(f'A medade de {moeda.moeda(p)} é {moeda.metade(p, sit=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, sit=False)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, sit=True)}')
print(f'Ao diminuir 13% temos {moeda.reduzir(p, 13, sit=False)}')
