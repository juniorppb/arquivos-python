import math
num = float(input('Digite o valor de um ângulo: '))
se = math.sin(num)
cos = math.cos(num)
tan = math.tan(num)
print('Para o ângulo {:.2f}, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(num, se, cos, tan))
