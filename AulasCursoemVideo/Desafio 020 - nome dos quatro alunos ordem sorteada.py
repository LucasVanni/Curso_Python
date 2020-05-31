import random

n1 = str(input('Digite o nome do primeiro aluno a ser sorteado: '))
n2 = str(input('Digite o nome do segundo aluno a ser sorteado: '))
n3 = str(input('Digite o nome do terceiro aluno a ser sorteado: '))
n4 = str(input('Digite o nome do quarto aluno a ser sorteado: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print('A ordem da lista de apresentação será: ')
print(lista)
