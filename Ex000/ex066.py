n = s = cont = 0
while True:
    n = int(input('Digite um numero [Digite 999 para parar]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram digitados {cont} valores e a soma dos valores foi {s}')
