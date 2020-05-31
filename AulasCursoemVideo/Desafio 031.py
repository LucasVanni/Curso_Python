KM = float(input('Qual a distância da viagem e KM? '))

if KM <= 200:
    valorP = 0.5 * KM
else:
    valorP = 0.45 * KM

print('O valor da passagem é R${}'.format(valorP))
