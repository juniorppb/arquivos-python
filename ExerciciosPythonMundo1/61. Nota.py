n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
soma = (n1 + n2) / 2
print('A sua média foi {}.'.format(soma))
#if soma <= 5.0:
 #   print('Você precisa estudar mais!')
#else:
 #   print('Excelente!! Você foi fantástiso.')
print('PARABÉNS' if soma >=5 else 'ESTUDE MAIS!')
