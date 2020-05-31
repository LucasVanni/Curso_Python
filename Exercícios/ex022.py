nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))

separado = nome.split()
print('O seu primero nome é {} e tem {} letras'.format(separado[0], len(separado[0])))
