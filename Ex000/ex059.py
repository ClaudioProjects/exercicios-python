opção = 0
opera = 0
opera1 = 0
numero1 = int(input('\033[33mDigite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
while opção != 5:
    print('\033[34m-' * 13, 'Menu', '-' * 13)
    print('Digite [1] para somar.\n'
          'Digite [2] para multiplicar.\n'
          'Digite [3] para Maior\n'
          'Digite [4] para novos números\n'
          'Digite [5] para sair do programa')
    print('-' * 32)
    opção = float(input('Escolha uma opção: '))
    if 0 < opção < 6:
        if opção == 1:
            opera = 'Soma'
            opera1 = numero1 + numero2
        elif opção == 2:
            opera = 'Multiplicação'
            opera1 = numero1 * numero2
        elif opção == 3:
            opera = 'Maior número'
            if numero1 < numero2:
                opera1 = numero2
            else:
                opera1 = numero1
        elif opção == 4:
            numero1 = int(input('Primeiro valor: '))
            numero2 = int(input('Segundo valor: '))
        elif opção == 5:
            continue
        print(f'\033[32mVocê escolheu {opera} o resultado é: {opera1:.2f}')
    else:
        print('\033[31mOpção invalida tente novamente')
    print('\033[34m-' * 32)
