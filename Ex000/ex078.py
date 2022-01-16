posição_menor = list()
posição_maior = list()
valor = list()
for c in range(0, 5):
    valor.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores: {valor}')
for c in range(0, 5):
    if valor[c] == min(valor):
        posição_menor.append(c)
    elif valor[c] == max(valor):
        posição_maior.append(c)
print(f'O menor valor foi {min(valor)} nas posições {posição_menor}')
print(f'O maior valor foi {max(valor)} nas posições {posição_maior}')
