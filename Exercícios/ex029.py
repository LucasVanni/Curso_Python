velAt = float(input('Qual a velocidade atual do carro? '))

if velAt > 80:
    multa = (velAt - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80 KM/H')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')
