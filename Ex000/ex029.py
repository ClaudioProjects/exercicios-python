vel = float(input('Informe em KM qual a velocidade que seu carro tava: '))
if vel >80:
    mul = (vel - 80)
    print(f'Seu carro foi multado por estar {mul}KM acima do limite\nVocê deve pagar uma multa de R${mul*7:.2f}')
else:
    print('Você andou dentro do limite, continue assim!!')
