import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hip = math.hypot(co, ca)

print('O valor da hipotenusa é {}'.format(hip))
