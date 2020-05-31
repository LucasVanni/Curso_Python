import math

angulo = float(input('Digite o valor de um angulo: '))

sen = math.sin(angulo)

cos = math.cos(angulo)

tan = math.tan(angulo)

print('O ângulo {:.2f}° tem o valor {:.2f} de seno, {:.2f} de cosseno e {:.2f} de tangente.'.format(angulo, sen, cos, tan))
