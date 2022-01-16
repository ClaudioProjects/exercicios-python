num = int(input('Digite um numero: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[32m{c}', end=' ')
        total = total + 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[33mO numero {num} foi divisível {total} vezes')
if total == 2:
    print('Por isso ele é PRIMO')
else:
    print('Por isso ele não é Primo')
