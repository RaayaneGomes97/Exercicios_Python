# 1° Método - Importando apenas funções necessáiras 
from math import radians, sin, cos, tan

ang = float(input('Digite o valor do ângulo: '))

# Utilizamos então a função math.radians para converter para grau
sen  = sin(radians(ang))
cos  = cos(radians(ang))
tan  = tan(radians(ang))

print(' O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print(' O ângulo de {} tem o SENO de {:.2f}'.format(ang, cos))
print(' O ângulo de {} tem o SENO de {:.2f}'.format(ang, tan))


# 
# 2° Método - Importando  TODA a biblioteca math
#
# import math
# ang = float(input('Digite o ângulo: '))
# 
# sen  = math.sin(math.radians(ang))
# cos  = math.cos(math.radians(ang))
# tan  = math.tan(math.radians(ang))
# 
# print(' O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
# print(' O ângulo de {} tem o SENO de {:.2f}'.format(ang, cos))
# print(' O ângulo de {} tem o SENO de {:.2f}'.format(ang, tan))
#
