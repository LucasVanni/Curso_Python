n = int(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raizQ = n ** (1/2)

print('O dobro de {} é {}.'.format(n, dobro))
print('O triplo de {} é {}.\nA raiz quadrada de {} é {:.2f}.'.format(n, triplo, n, raizQ))

print('\n')

print('O dobro de {} é {}.'.format(n, (n * 2)))
print('O triplo de {} é {}.\nA raiz quadrada de {} é {:.2f}.'.format(n, (n * 3), n, (n ** (1/2))))

print('\n')

print('O dobro de {} é {}.'.format(n, (n * 2)))
print('O triplo de {} é {}.\nA raiz quadrada de {} é {:.2f}.'.format(n, (n * 3), n, pow(n, 1/2)))
