frase = 'curso em video python'
print(type(frase))
print(frase[-9], frase[9],'Fatiamento')
print(len(frase), 'Len')
print(frase.count('o'), 'Count')
print(frase.count('o',0,13))
print(frase.find('deo'))
print('curso' in frase)
print(frase.replace('python', 'android'))
print(frase.upper())
print(frase.capitalize())
print(frase.title())
frase2 = '   Aprenda python  '
print(frase2.strip())
print(frase2.rstrip())
print(frase.split())
print(''.join(frase))
print(frase.upper().find('VIDEO'))
print('curso' in frase)