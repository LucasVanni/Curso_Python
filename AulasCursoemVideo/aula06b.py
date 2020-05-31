n = float(input('Digite um valor: '))
print(n)

print(type(n))

n = str(input('Digite um valor: '))
print(n)

print(type(n))

n = bool(input('Digite um valor: '))
print(n)

print(type(n))

n = input('Digite algo ')
print(n.isnumeric())  # Verifica se é um número
print(n.isalnum())  # Verifica se é um valor com letras e números
print(n.isalpha())  # Verifica se é uma letra alfabética
print(n.isupper())    # Verifica se está apenas com letras maiúsculas
print(n.islower())  # Verifica se está em letras minúsculas
print(n.isprintable())  # Verifica se pode ser impresso
print(n.isspace())  # Verifica se é um espaço

