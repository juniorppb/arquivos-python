from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {:.3f}.'.format(num, raiz))
print('_' * 25)

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}.'.format(num, floor(raiz)))
print('_'* 25)

from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}.'.format(num, ceil(raiz)))

