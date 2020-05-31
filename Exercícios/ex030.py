n = int(input('Me diga um número qualquer: '))
resultado = n % 2
if resultado == 0:
    print('O número {} é PAR'.format(n))
else:
    print('\033[mO número {} é IMPAR'.format(n))
