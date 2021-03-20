import math
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
print('Para o ângulo {} o SENO é {:.2f}.'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('Para o ângulo {} o COSSENO é {:.2f}.'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('Para o ângulo {} a TANGENTE é {:.2f}.'.format(angulo, tan))