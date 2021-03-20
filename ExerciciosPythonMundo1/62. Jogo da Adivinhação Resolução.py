from random import randint
num = randint(0, 5)
print('='*100)
print('Olá! Vamos nos divertir. Vou pensar em um número de 0 a 5, e você tentar adivinhar...')
print('='*100)
n = int(input('Em que número eu pensei? '))
if n == num:
    print('Parabéns! Você conseguiu, eu pensei no número {}, o mesmo que o seu {}.'.format(num, n))
else:
    print('Não foi dessa vez. Eu pensei no número {}, e não no {}. Mas não desista.'.format(num, n))

