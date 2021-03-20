import math
co = float(input('Qual é o comprimento do cateto oposto?'))
ca = float(input('QUal é o comprimento do cateto adjascente?'))
hi = math.hypot(co, ca)
print('O valor de hipotenusa é {:.2f}.'.format(hi))