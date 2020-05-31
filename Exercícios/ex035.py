'''print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

L1 = float(input('Primeiro segmento: '))
L2 = float(input('Segundo segmento: '))
L3 = float(input('Terceiro segmento: '))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Esses segmentos podem formam um triângulo.')
else:
    print('Esses segmentos não podem formam um triângulo.')

num = '7'

res = int(num) / 2

print(type(res))

n1 = 5
n2 = 2
res = n1 / n2 // 1
print(res)

from random import randint
num = randint(1, 6)
res = num // 2
print(res)

a = 4
b = 3
c = 2
d = a + b * c
e = d % c + 1
print("{} e {}".format(d, e))

texto = 'Tres Pratos de Trigo para Tigres Tristes'
total = texto.upper().count(texto[0])
print(total)

res = 3 + 2 * 4

print(res)

valor = '153'
parte = "5"
valor += parte
print(valor.isnumeric())'''

from datetime import date
ano = date.today().year

from random import choice
n = [2, 5, 9, 1, 4]
res = choice(n) % n[0]
print(res)

frase = 'Curso em Video de Python'
separado = frase.split()
palavra = separado[2]
letra = palavra[3]
print(letra.upper())

a = 4
b = 3
c = 2
d = a + b * c
e = d % c + 1
print("{} e {}".format(d, e))