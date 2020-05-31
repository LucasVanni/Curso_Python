## Teoria

frase = 'Curso em Video Python'

# fatiamento
print(frase[9])

print(frase[9:14])

print(frase[9:21])

print(frase[9:21:2])

print(frase[:5])

print(frase[15:])

print(frase[9::3])

# Análise

print(len(frase)) # imprime o comprimento da string

print(frase.count('o')) # Conta quantas vezes existe a letra na string

print(frase.count('o', 0, 13)) # Conta quantas vezes existe a letra, porém do caráctere 0 até o 12

print(frase.find('deo')) # Mostra em que momento começou a string desejada na frase

print(frase.find('Android')) # Retorna o valor -1 para string que não existe

print('Curso' in frase) # Existe a string na frase

# Transformação

print(frase.replace('Python', 'Android')) # substitui python por android no momento da execução do método

print(frase.upper()) # Deixa a frase em Maiúsculas

print(frase.lower()) # Deixa a frase em Minúsculas

print(frase.capitalize()) # Só o primeiro caractére fica em maiúsculo, o resto em minúsculo

print(frase.title()) # Deixa as primeiras letras de cada palavra em maiúsculo

print(frase.strip()) # Remove todos os espaços inúteis no início e no final da string

print(frase.rstrip()) # Remove os espaços inúteis a direita

print(frase.lstrip()) # Remove os espaços inúteis a esquerda

# Divisão

print(frase.split())

# Junção

print('-'.join(frase))


### Prática

print(frase[::2])

print('''\nmxklsdnasjkdnasjidnsajndf
dspoadmsaopmdsoa
dpasmdpamfpas
dasmpdsap''')

print(frase.upper().count('O'))

print(len(frase.strip()))

print(frase.split())
