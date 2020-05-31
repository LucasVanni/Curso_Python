V1 = int(input('Primeiro valor: '))
V2 = int(input('Segundo valor: '))
V3 = int(input('Terceiro valor: '))

# Verificando quem é o menor
menor = V1

if V2 < V1 and V2 < V3:
    menor = V2
if V3 < V1 and V3 < V2:
    menor = V3

# Verificando quem é o maior
maior = V1

if V2 > V1 and V2 > V3:
    maior = V2
if V3 > V1 and V3 > V2:
    maior = V3

print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
