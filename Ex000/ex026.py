frase = str(input('Digite qualquer frase: ')).upper()
print(f'A letra A aparece {frase.count("A")} vezes')
print(f'A primeira posição que a letra A aparece é na {frase.find("A")+1}')
print(f'A ultima vez que a letra A aparece é na posição {frase.rfind("A")+1}')


