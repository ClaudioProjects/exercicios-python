palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
           'mercado', 'programador', 'futuro')
for c in range(0, len(palavra)):
    print(f'\nNa palavra {palavra[c].upper()} temos', end=' ')
    for z in range(0, len(palavra[c])):
        if palavra[c][z] in 'a' 'e' 'i' 'o' 'u':
            print(palavra[c][z], end=' ')
'''for c in palavra:
    print(f'\nNa palavra {c.upper()} temos', end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')'''
