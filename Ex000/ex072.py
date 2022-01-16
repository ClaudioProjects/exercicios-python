tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
         'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoite', 'Dezenove', 'Vinte')
z = int(input('Digite um valor entre 0 e 20: '))
while z > 20 or z < 0:
    z = int(input('Numero invalido. Tente novamente: '))
print(f'Você digitou o numero {tupla[z]}')
