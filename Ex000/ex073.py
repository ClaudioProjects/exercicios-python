times = ('Atlético-MG', 'Flamengo', 'Fortaleza', 'Palmeiras', 'Bragantino', 'Corinthians', 'Internacional',
         'Fluminense', 'Cuiabá', 'Atlético-PR', 'Atlético-GO', 'São Paulo', 'América-MG', 'Ceará SC', 'Santos',
         'Bahia', 'Juventude', 'Sport Recife', 'Grêmio', 'Chapecoense')
print(f'Os cinco primeiros times do brasileirão: ', end='')
for c in range(0, 5):
    print(times[c], end=' -> ')
print('Fim')
print('Os quatro últimos times do brasileirão: ', end='')
for c in range(16, 20):
    print(times[c], end=' -> ')
print('Fim')
print(sorted(times))
print(f'Chapecoense esta na {times.index("Chapecoense")}° posição')
