salario = float(input('Qual o seu salario: '))
if salario > 1250:
    print(f'Seu salario com 10% de aumento vai para R${salario * 110/100:.2f}')
else:
    print(f'Seu salario depois do aumento de 15% vai para R${salario * 115/100:.2f}')
