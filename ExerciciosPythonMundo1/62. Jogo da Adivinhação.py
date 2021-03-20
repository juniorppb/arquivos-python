import random
print('='*100)
print('Olá! Vamos nos divertir. Vou pensar em um número de 0 a 5, e você tentar adivinhar...')
n = int(input('Em que número eu pensei? '))
num = random.randint(0, 5)
print(num)
if n == num:
    print('Parabéns! Você conseguiu.')
else:
    print('Não foi dessa vez. Mas não desista.')
