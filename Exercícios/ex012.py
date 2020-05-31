preço = float(input('Qual o preço do produto? R$ '))

# avista = preço - (preço * 10/100)

# parcelado = preço + (preço * 8/100)

novo = preço - (preço * 5/100)

print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(preço, novo))

# print('O valor da compra é de R$ {:.2f}, avista recebe desconto de 10% e fica {:.2f} parcelado com aumento de 8% fica R$ {:.2f}.'.format(preço, avista, parcelado))
