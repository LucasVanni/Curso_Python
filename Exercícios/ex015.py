dias = int(input('Informe a quantia de dias que o carro foi alugado: '))

kmR = float(input('Informe quantos Kilometros foram percorridos pelo carro: '))

pago = (dias * 60) + (kmR * 0.15)

print('O total a pagar é de R$ {:.2f}'.format(pago))
