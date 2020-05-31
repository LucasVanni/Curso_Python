'''nome = str(input('Qual é o seu nome? '))
if nome == 'Lucas':
    print('Que nome lindo vc tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

print('A sua média foi {:.1f}'.format(m))

if m < 5:
    print('Aluno Reprovado!')
else:
    if m >= 5 and m < 7:
        print('Aluno de exame!')
    else:
        print('Aluno Aprovado!')
