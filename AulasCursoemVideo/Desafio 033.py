n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1 > n2 > n3:
    print('O número maior é {}'.format(n1))
else:
    if n2 > n1 > n3:
        print('O número maior é {}'.format(n2))
    else:
        if n3 > n1 > n1:
            print('O número maior é {}'.format(n3))

if n1 < n2 < n3:
    print('O número menor é {}'.format(n1))
else:
    if n2 < n3 < n1:
        print('O número menor é {}'.format(n2))
    else:
        if n3 < n2 < n1:
            print('O número menor é {}'.format(n3))
