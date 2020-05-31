print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

L1 = float(input('Primeiro segmento: '))
L2 = float(input('Segundo segmento: '))
L3 = float(input('Terceiro segmento: '))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Esses segmentos podem formam um triângulo.')
else:
    print('Esses segmentos não podem formam um triângulo.')
