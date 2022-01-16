from datetime import date

s = 0
y = date.today().year
for c in range(1, 8):
    x = int(input(f'Ano de nascimento da {c}° pessoa: '))
    if y - x >= 21:
        soma = 1
        s += soma
menor = c - s
print(f'Das 7 pessoas informados {s} delas ja atingiram a maioridade e {menor} ainda não atingiram a maioridade')
