# Prática

#nome = str(input('Qual é o seu nome? '))
#print('Prazer em te conhecer {:20}!'.format(nome))
#print('Prazer em te conhecer {:>20}!'.format(nome))
#print('Prazer em te conhecer {:<20}!'.format(nome))
#print('Prazer em te conhecer {:^20}!'.format(nome))
#print('Prazer em te conhecer {:=^20}!'.format(nome))

#print('Prazer em te conhecer {:-^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

print('A soma vale {}'.format(n1+n2))
print('A multiplicação vale {}'.format(n1*n2))
print('A divisão vale {}'.format(n1/n2))
print('A divisão inteira vale {}'.format(n1//n2))
print('A exponenciação vale {}'.format(n1**n2))

print('')
print('')

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o \n produto é {}, e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('divisão inteira é {} e potência {}'.format(di, e))



# Teoria

# + -> adição
# - -> subtração
# * -> multiplicação
# / -> divisão
# ** -> potência
# // -> divisão inteira
# % -> Resto da divisão

# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print(5 ** 2)
# print(5 // 2)
# print(5 % 2)

# Ordem de precedência
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -

# print('')

# print(5 + 3 * 2)

# print('')

# print(3 * 5 + 4 ** 2)

# print('')

#print(3 * (5 + 4) ** 2)
