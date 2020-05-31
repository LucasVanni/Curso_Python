reais = float(input('Quantos dinheiro você tem na carteira? R$'))

dolar = reais / 3.783

euro = reais / 4.415

print('Com R${:.2f} você pode comprar U${:.2f} e {:.2f} Euros'.format(reais, dolar, euro))
