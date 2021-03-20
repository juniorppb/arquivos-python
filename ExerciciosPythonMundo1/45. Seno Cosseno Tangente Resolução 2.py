from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
print('Para o ângulo {} o SENO é {:.2f}.'.format(angulo, seno))
cos = cos(radians(angulo))
print('Para o ângulo {} o COSSENO é {:.2f}.'.format(angulo, cos))
tan = tan(radians(angulo))
print('Para o ângulo {} a TANGENTE é {:.2f}.'.format(angulo, tan))