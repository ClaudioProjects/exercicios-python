'''def mensagem(msg):
    print('—' * 20)
    print(msg)
    print('—' * 20)


mensagem(f'{"Sistema de alunos":^20}')'''

'''def soma(a, b):
    print(f'A soma {a} + {b} é igual', end=' = ')
    s = a + b
    print(s)


soma(8, 8)
soma(9, 7)
soma(2, 4)'''

'''def contador(* num):
    tam = len(num)
    print('—' * 35)
    print(f'Recebi os valores {num} e ao todo eles são {tam} números ')
    print('—' * 35)


contador(1, 5, 7, 8)
contador(9, 2, 3)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5, 6]
dobra(valores)
print(valores)'''

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos {valores} é {s}')


soma(1, 5, 7, 31)
soma(1, 7, 3, 1)