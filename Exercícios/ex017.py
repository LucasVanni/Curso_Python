from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hip = hypot(ca, co)

hi = (co ** 2 + ca ** 2) ** (1/2)# maneira matemática

print('A hipotenusa vai medir {:.2f}'.format(hip))

print('A hipotenusa no método matemático vai medir {:.2f}'.format(hi))
