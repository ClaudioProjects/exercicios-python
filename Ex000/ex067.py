while True:
    n = int(input('Você quer ver a tabuada de qual valor: '))
    print('~' * 38)
    c = 0
    if n <= 0:
        break
    while c != 10:
        c += 1
        print(f'{n} X {c:2} = {n * c}')
    print('~' * 38)
print('Tabuada encerrada. Volte sempre')
