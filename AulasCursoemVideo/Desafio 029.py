velocidade = int(input('Qual a velocidade do carro? '))

valorVelo = velocidade - 80

if velocidade > 80:
    valor = valorVelo * 7

if velocidade > 80:
    print('O motorista foi multado e o valor da multa é de R${}'.format(valor))