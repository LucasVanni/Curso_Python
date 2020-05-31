salario = float(input('Digite o valor do salário: '))

if salario >= 1250.00:
    aumento = (salario * 10/100)

else:
    aumento = (salario * 15/100)

print('Com o salário de R${}, irá ter um aumento de R${}'.format(salario, aumento))