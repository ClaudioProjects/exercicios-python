try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a / b
except ZeroDivisionError:
    print('A divisão por 0 não existe')
except ValueError:
    print('O valor digitado não é valido')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar')
except Exception as erro:
    print(f'O erro doi {erro.__cause__}')
else:
    print(f'O resultado é {c}')
finally:
    print('Tenha um bom dia!!')