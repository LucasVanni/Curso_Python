viagem = float(input('Qual a distância da sua viagem? '))
if viagem <= 200:
    valor = viagem * 0.5
else:
    valor = viagem * 0.45

valor = viagem * 0.5 if viagem <= 200 else viagem * 0.45

print('Você está prestes a começar uma viagem de {}KM.'.format(viagem))
print('E o preço da sua passagem será de R${:.2f}'.format(valor))
