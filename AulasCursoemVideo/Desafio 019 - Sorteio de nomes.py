import random

n1 = str(input('Digite o nome do primeiro aluno a ser sorteado: '))
n2 = str(input('Digite o nome do segundo aluno a ser sorteado: '))
n3 = str(input('Digite o nome do terceiro aluno a ser sorteado: '))
n4 = str(input('Digite o nome do quarto aluno a ser sorteado: '))

randomico = random.choice([n1, n2, n3, n4])

print('O aluno escolhido foi: {}'.format(randomico))
