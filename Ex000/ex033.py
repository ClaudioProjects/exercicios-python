n = int(input('Digite um numero: '))
n1 = int(input('Digite outro numero: '))
n2 = int(input('Digite mais um numero: '))
menor = n
if n1 < n and n1 < n2:
    menor = n1
if n2 < n and n2 < n1:
    menor = n2
maior = n
if n1 > n and n1 > n2:
    maior = n1
if n2 > n and n2 > n1:
    maior = n2
print(f'O menor numero é {menor}!!')
print(f'O maior numero é {maior}!!')
