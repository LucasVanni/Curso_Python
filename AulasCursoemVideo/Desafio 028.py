numero = int(input('Adivinhe o número! (Entre 0 e 5)'))

import random

numAL = random.randint(0, 5)

if numAL == numero:
    print('Parabéns você acertou o número, que é {}'.format(numAL))
else:
    print('Que pena errou o número, o correto seria {}'.format(numAL))
