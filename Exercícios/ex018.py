#import math

from math import radians, cos, sin, tan

ângulo = float(input('Digite o ângulo que você deseja: '))

Sen = sin(radians(ângulo))
Cos = cos(radians(ângulo))
Tang = tan(radians(ângulo))

# Sen = math.sin(math.radians(ângulo))
# Cos = math.cos(math.radians(ângulo))
# Tang = math.tan(math.radians(ângulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, Sen))
print('O ângulo de {} tem o COS de {:.2f}'.format(ângulo, Cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, Tang))
